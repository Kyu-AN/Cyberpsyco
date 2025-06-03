import requests
import base64
import tkinter as tk
from tkinter import messagebox
import re

TMDB_API_KEY = "TMDB API 키 입력" #API키 입력해야함

SPOTIFY_API_KEY = "Spotify API 키 입력" #API 키 입력해야함
SPOTIFY_API_SECRET = "Spotify API 암호 입력" #API 암호 입력해야함

def search_movie(title):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": title,
        "language": "ko-KR"
    }
    response = requests.get(url, params=params)
    data = response.json()
    results = data.get("results", [])
    
    if not results:
        print("검색 결과가 없습니다.")
        return None
    
    top = results[0]
    print("검색된 영화: %s(%s)" % (top['title'], top.get('release_date', '출시일 없음')))
    print("줄거리: ", top.get("overview", "줄거리 정보 없음"))
    
    confirm = input("이 영화가 맞습니까? (Y/N): ").strip().lower()
    if confirm == "y":
        return top["id"]
    else:
        print("취소되었습니다.")
        return None

def get_movie_id():
    title = input("영화 제목을 입력하세요: ")
    return search_movie(title)

def get_movie_keywords(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/keywords"
    params = {
        "api_key": TMDB_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        keywords = [kw["name"] for kw in data.get("keywords", [])]
        return keywords
    else:
        print("키워드 불러오기 실패")
        return []

def show_keywords_selector(movie_id):
    keywords = get_movie_keywords(movie_id)
    if not keywords:
        print("키워드가 없습니다.")
        return []

    window = tk.Tk()
    window.title("키워드 선택")

    label = tk.Label(window, text="검색에 사용할 키워드를 선택하세요:")
    label.pack(pady=10)

    selected_keywords = []
    keyword_vars = []
    for kw in keywords:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(window, text=kw, variable=var)
        chk.pack(anchor='w')
        keyword_vars.append((kw, var))

    def submit_selection():
        selected_keywords.clear()
        selected_keywords.extend([kw for kw, var in keyword_vars if var.get()])
        window.destroy()
        print("\n선택된 키워드:")
        for kw in selected_keywords:
            print(f"- {kw}")

    btn = tk.Button(window, text="선택 완료", command=submit_selection)
    btn.pack(pady=10)

    window.mainloop()
    return selected_keywords

def clean_keywords(keywords):
    cleaned = []
    for kw in keywords:
        kw = kw.lower()
        kw = re.sub(r"[^a-z0-9\s]", "", kw)
        kw = kw.strip()
        if len(kw) < 2:
            continue
        cleaned.append(kw)
    cleaned = list(dict.fromkeys(cleaned))
    return cleaned

def get_access_token():
    auth_str = f"{SPOTIFY_API_KEY}:{SPOTIFY_API_SECRET}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    headers = {
        "Authorization": f"Basic {b64_auth_str}"
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    result = response.json()
    return result["access_token"]

def search_spotify_tracks(keyword, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": keyword,
        "type": "track",
        "limit": 5
    }
    response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
    if response.status_code != 200:
        print(f"[{keyword}] 검색 실패: {response.status_code}")
        return []

    results = response.json().get("tracks", {}).get("items", [])
    track_info = [f"{track['name']} - {track['artists'][0]['name']}" for track in results]
    return track_info

def main():
    movie_id = get_movie_id()
    if not movie_id:
        print("영화 ID를 가져오지 못해 종료합니다.")
        return

    selected_keywords = show_keywords_selector(movie_id)
    if not selected_keywords:
        print("선택된 키워드가 없습니다.")
        return

    print("\n[다음 작업을 위한 선택된 키워드 목록]")
    for kw in selected_keywords:
        print(f"- {kw}")

    cleaned_keywords = clean_keywords(selected_keywords)

    print("\n[정제된 키워드 목록]")
    for kw in cleaned_keywords:
        print("-", kw)

    token = get_access_token()

    print("\n[Spotify 검색 결과]")
    for kw in cleaned_keywords:
        tracks = search_spotify_tracks(kw, token)
        if tracks:
            print(f"\n'{kw}' 관련 노래:")
            for track in tracks:
                print("🎵", track)
        else:
            print(f"\n'{kw}' 관련 노래를 찾을 수 없습니다.")

if __name__ == "__main__":
    main()
