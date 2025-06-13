from id_search import get_movie_id
from Keyword_search import show_keywords_selector
from keyword_cleaner import clean_keywords
from ai_helper import generate_query
from spotify_search import get_access_token,search_spotify_by_query

import tkinter as tk
from tkinter import messagebox


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

    X=generate_query(cleaned_keywords)
    tracks=search_spotify_by_query(X,token)

    if tracks:
        result_window = tk.Toplevel()
        result_window.title("추천 음악 결과")
        result_window.geometry("400x300")

        tk.Label(result_window, text="Spotify 추천 결과", font=("Arial", 14, "bold")).pack(pady=10)

        frame = tk.Frame(result_window)
        frame.pack(padx=10, pady=10)

        for i, track in enumerate(tracks, start=1):
            label = tk.Label(frame, text=f"{i}. {track}", anchor="w", justify="left", font=("Arial", 11))
            label.pack(fill="x", padx=5, pady=2)

    else:
        messagebox.showinfo("결과 없음", "추천된 트랙이 없습니다.") 

def gui_launcher():
    def on_start():
        root.destroy()
        main()

    root = tk.Tk()
    root.title("영화 기반 음악 추천기")

    tk.Label(root, text="🎬 영화 기반 음악 추천 프로그램 🎵").pack(pady=20)
    tk.Button(root, text="실행하기", command=on_start, width=20, height=2).pack(pady=10)
    tk.Button(root, text="종료", command=root.destroy, width=20, height=2).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    gui_launcher()
