import tkinter as tk
from tkinter import messagebox

def run_ui():
    window = tk.Tk()
    window.title("영화와 어울리는 음악 추천")
    window.geometry("600x300")
    window.config(bg="#1a0000")

    entry_label = tk.Label(window, text="영화 제목을 입력하세요:", bg="#1a0000", fg="white")
    entry_label.pack(pady=10)

    input_frame = tk.Frame(window, bg="#1a0000", width=560, height=30)
    input_frame.pack(pady=10)
    input_frame.pack_propagate(False)

    movie_entry = tk.Entry(input_frame)
    movie_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))

    def show_recommendations_in_new_window(tracks):
        if not tracks:
            messagebox.showinfo("추천 결과 없음", "추천된 곡이 없습니다.")
            return

        popup = tk.Toplevel(window)
        popup.title("추천된 음악 리스트")
        popup.geometry("500x300")
        popup.config(bg="#1a0000")

        title = tk.Label(popup, text="🎵 추천 음악 리스트 🎵", bg="#1a0000", fg="white")
        title.pack(pady=10)

        text_box = tk.Text(popup, height=15, width=60, wrap="word", bg="#1a0000", fg="white", borderwidth=0)
        text_box.pack(pady=10)

        for track in tracks:
            text_box.insert(tk.END, f"{track}\n")

        text_box.config(state="disabled")  

    def recommend_music():
        #추천트랙리스트넣어주기
        tracks = []  
        show_recommendations_in_new_window(tracks)

    search_btn = tk.Button(input_frame, text="영화 검색", width=12, command=recommend_music)
    search_btn.grid(row=0, column=1)

    input_frame.grid_columnconfigure(0, weight=1)
    input_frame.grid_columnconfigure(1, weight=0)

    synopsis_text = tk.Text(window, height=10, width=70, wrap="word")
    synopsis_text.pack(pady=10)

    keyword_frame = tk.Frame(window, bg="#1a0000")
    keyword_frame.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    run_ui()
