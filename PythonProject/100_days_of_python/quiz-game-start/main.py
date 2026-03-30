from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for question in question_data:
    questions =Question(question["text"], question["answer"])
    question_bank.append(questions)
quiz = QuizzBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"\n\nyou've completed the quiz!\nyour final score is:{quiz.score}/{quiz.number_of_questions}")


