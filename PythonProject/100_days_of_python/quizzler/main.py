from quiz_brain import QuizBrain
from ui import UI
from question_model import QuestionModel # Import your API class
import html

# 1. Fetch fresh data using your model
model = QuestionModel()
question_data = model.get_questions() # Let's create this method

question_bank = []
for question in question_data:
    question_bank.append({"text":html.unescape(question["question"]), "answer": question["correct_answer"]})

# 2. Setup the Brain
quiz = QuizBrain(question_bank)

# 3. Setup the UI (Pass 'quiz', which is your QuizBrain instance)
quiz_ui = UI(quiz)
quiz_ui.mainloop()