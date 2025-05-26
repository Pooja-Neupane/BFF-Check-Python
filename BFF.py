import tkinter as tk
from tkinter import messagebox

# Questions for each friend
friend1_questions = [
    ("What is my favorite snack?", "Momo"),
    ("What’s my favorite Netflix show?", "Stranger Things"),
    ("Who is my celebrity crush?", "Shah Rukh Khan"),
    ("When is my birthday?", "November 15"),
    ("What’s my hidden talent?", "Singing")
]

friend2_questions = [
    ("What's my favorite subject?", "Web Technology"),
    ("What's my dream job?", "Software Developer"),
    ("What’s my biggest fear?", "Heights"),
    ("Where did we first meet?", "Campus"),
    ("What do I always order when we go out?", "Cold Coffee")
]

# GUI App Class
class BestFriendQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("💛 Best Friend Quiz Game 💛")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.f1_name = ""
        self.f2_name = ""
        self.score = 0
        self.turn = 1
        self.index = 0

        self.questions = []
        self.answers = []

        self.create_name_input()

    def create_name_input(self):
        self.clear_screen()
        tk.Label(self.root, text="Best Friend Quiz 💫", font=("Helvetica", 18, "bold")).pack(pady=20)

        tk.Label(self.root, text="Enter Friend 1 Name:").pack()
        self.name1_entry = tk.Entry(self.root)
        self.name1_entry.pack(pady=5)

        tk.Label(self.root, text="Enter Friend 2 Name:").pack()
        self.name2_entry = tk.Entry(self.root)
        self.name2_entry.pack(pady=5)

        tk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=20)

    def start_game(self):
        self.f1_name = self.name1_entry.get()
        self.f2_name = self.name2_entry.get()

        if not self.f1_name or not self.f2_name:
            messagebox.showwarning("Input Error", "Please enter both names!")
            return

        self.turn = 1
        self.index = 0
        self.scores = {self.f1_name: 0, self.f2_name: 0}
        self.questions = friend2_questions  # Friend 1 answers Friend 2's questions
        self.show_question()

    def show_question(self):
        self.clear_screen()
        current_friend = self.f1_name if self.turn == 1 else self.f2_name
        tk.Label(self.root, text=f"{current_friend}, it's your turn!", font=("Helvetica", 14)).pack(pady=10)

        q, _ = self.questions[self.index]
        tk.Label(self.root, text=f"Q{self.index+1}: {q}", wraplength=450, font=("Helvetica", 12)).pack(pady=20)

        self.answer_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.answer_entry.pack(pady=10)

        tk.Button(self.root, text="Submit Answer", command=self.check_answer).pack(pady=10)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.questions[self.index][1].strip().lower()

        current_friend = self.f1_name if self.turn == 1 else self.f2_name
        if user_answer == correct_answer:
            self.scores[current_friend] += 1
            messagebox.showinfo("Correct!", "✅ That's right!")
        else:
            messagebox.showinfo("Oops!", f"❌ The correct answer was: {self.questions[self.index][1]}")

        self.index += 1
        if self.index >= len(self.questions):
            if self.turn == 1:
                self.turn = 2
                self.index = 0
                self.questions = friend1_questions  # Friend 2 answers Friend 1's questions
                self.show_question()
            else:
                self.show_result()
        else:
            self.show_question()

    def show_result(self):
        self.clear_screen()
        score1 = self.scores[self.f1_name]
        score2 = self.scores[self.f2_name]

        tk.Label(self.root, text="🎉 Game Over 🎉", font=("Helvetica", 18, "bold")).pack(pady=10)
        tk.Label(self.root, text=f"{self.f1_name}'s Score: {score1}", font=("Helvetica", 12)).pack()
        tk.Label(self.root, text=f"{self.f2_name}'s Score: {score2}", font=("Helvetica", 12)).pack()

        result = "It's a tie! 🤝" if score1 == score2 else f"{self.f1_name if score1 > score2 else self.f2_name} knows better! 💛"
        tk.Label(self.root, text=result, font=("Helvetica", 14, "italic"), fg="darkgreen").pack(pady=15)

        tk.Button(self.root, text="Play Again", command=self.create_name_input).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Run the GUI App
if __name__ == "__main__":
    root = tk.Tk()
    app = BestFriendQuizApp(root)
    root.mainloop()
