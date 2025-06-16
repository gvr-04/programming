class QuizBrain:
    def __init__(self, question_lst):
        self.question_numer = 0
        self. questions_list = question_lst
        self.correct = 0

    def still_has_questions(self):
        return self.question_numer < len(self.questions_list)

    def next_question(self):
        obj = self.questions_list[self.question_numer]
        self.question_numer += 1
        user = input(f"\nQ.{self.question_numer}: {obj.text} (True/False)?: ")

        if user == obj.answer:
            self.correct += 1
            print(f"You got it right!\nThe correct answer was: {user}.\nYour current"
                  f" score is: {self.correct}/{self.question_numer}.")

        else:
            print("You got it wrong!")
            print(f"the correct answer was: {obj.answer}.")
            print(f"your score is {self.correct}/{self.question_numer}.")

