import requests
import tkinter as tk
from tkinter import messagebox
from APIkey import TMDB_API_KEY

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
        print("\n 선택된 키워드:")
        for kw in selected_keywords:
            print(f"- {kw}")

    btn = tk.Button(window, text="선택 완료", command=submit_selection)
    btn.pack(pady=10)

    window.mainloop()
    return selected_keywords
