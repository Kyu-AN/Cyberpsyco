from id_search import get_movie_id
from Keyword_search import show_keywords_selector

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

if __name__ == "__main__":
    main()
