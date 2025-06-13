import requests
import tkinter as tk
from tkinter import simpledialog, messagebox
from APIkey import TMDB_API_KEY

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
    movie_title = top.get('title', '제목 없음')
    release_date = top.get('release_date', '출시일 없음')
    overview = top.get('overview', '줄거리 정보 없음')

    confirm = messagebox.askyesno(
        "영화 확인",
        f"검색된 영화: {movie_title} ({release_date})\n\n줄거리:\n{overview}\n\n이 영화가 맞습니까?"
    )

    if confirm:
        return top["id"]
    else:
        messagebox.showinfo("취소", "선택이 취소되었습니다.")
        return None
    
def get_movie_id():
    window = tk.Tk()
    window.withdraw() 
    title = simpledialog.askstring("영화 제목 입력", "영화 제목을 입력하세요:")
    if not title:
        messagebox.showinfo("입력 없음", "영화 제목이 입력되지 않았습니다.")
        return None
    return search_movie(title)

if __name__ == "__main__":

    movie_id = get_movie_id()
    
    if movie_id:
        print("선택된 영화 ID: %s" %movie_id)
    else:
        print("영화 ID를 가져오지 못했습니다.")
