class quiz_brain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0


    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        self.question_number += 1
        question = self.question_list[self.question_number - 1]
        
        user_answer = input(f"Q.{self.question_number}: {question.text} True/False: ")
        self.check_answer(user_answer, question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Yah! You got it right.")
            
        else:
            print("Oops! You are wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your score is: {self.score}/{self.question_number}")
        print("\n")
    

