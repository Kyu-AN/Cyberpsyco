import requests
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
    print("검색된 영화: %s(%s)"%(top['title'],top.get('release_date','출시일 없음')))
    print("줄거리: ",top.get("overview", "줄거리 정보 없음"))
    
    confirm = input("이 영화가 맞습니까? (Y/N): ").strip().lower()
    if confirm == "y":
        return top["id"]
    else:
        print("취소되었습니다.")
        return None
    
def get_movie_id():
    title = input("영화 제목을 입력하세요: ")
    return search_movie(title)


if __name__ == "__main__":

    movie_id = get_movie_id()
    
    if movie_id:
        print("선택된 영화 ID: %s" %movie_id)
    else:
        print("영화 ID를 가져오지 못했습니다.")
