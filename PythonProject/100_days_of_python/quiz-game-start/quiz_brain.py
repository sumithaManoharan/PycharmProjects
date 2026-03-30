class QuizzBrain:
    def __init__(self, q_list):self.number_of_questions,self.question_list,self.score = 0, q_list,0

    def still_has_questions(self):
        if self.number_of_questions < len(self.question_list):
            return True
        else: return False


    def next_question(self):
        current_question = self.question_list[self.number_of_questions]
        self.number_of_questions += 1
        ans = input(f"Q. {self.number_of_questions} : {current_question.questions}. (TRUE/FALSE)").lower()
        if ans.lower() == current_question.answers.lower():
            self.score += 1
            print("you got it right!\nthe correct answer was:" + current_question.answers )
            print(f"your current score is: {self.score}/{self.number_of_questions}")
        else:
            print("you got it wrong!\nthe correct answer was:" + current_question.answers )
            print(f"your current score is: {self.score}/{self.number_of_questions}")



