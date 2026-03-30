from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
RIGHT_COLOR = "#75B06F"
WRONG_COLOR = "#F96E5B"


class UI(Tk):
    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()
        self.quiz = quiz_brain
        self.title("Quizzler")
        self.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=500, height=400, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            250, 200, text="Question Area", width=450, fill=THEME_COLOR, font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.pressed_true)
        self.true_btn.image = true_img
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.pressed_false)
        self.false_btn.image = false_img
        self.false_btn.grid(row=2, column=1)

        self.reset_btn = Button(text="Play Again", command=self.restart_game, font=("Arial", 10, "bold"))

        # --- CRITICAL LINE: Start the first question ---
        self.get_next_question()

        # Start the window
        self.mainloop()

    def pressed_true(self):  # Changed from true_pressed to pressed_true
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def pressed_false(self):  # Add this missing function
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # 3. Wait 1 second, then reset and get the next question
        self.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # 1. Display the FINAL SCORE on the canvas
            final_message = f"Quiz Finished!\nFinal Score: {self.quiz.score}/{len(self.quiz.question_list)}"
            self.canvas.itemconfig(self.question_text, text=final_message)

            # Disable buttons
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

            # Show the reset button
            self.reset_btn.grid(row=3, column=0, columnspan=2, pady=20)

    def restart_game(self):
        # 2. Fetch NEW questions from the API
        from question_model import QuestionModel
        import html

        new_data = QuestionModel().get_questions()
        new_bank = []
        for question in new_data:
            new_bank.append({
                "text": html.unescape(question["question"]),
                "answer": question["correct_answer"]
            })

        # 3. Update the QuizBrain with the new list and reset score
        self.quiz.question_list = new_bank
        self.quiz.reset_quiz()

        # 4. Refresh UI State
        self.true_btn.config(state="normal")
        self.false_btn.config(state="normal")
        self.reset_btn.grid_forget()
        self.get_next_question()

