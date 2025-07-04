
class Quiz:

    def __init__(self,questions_list):
        self.questions = questions_list
        self.score = 0
        self.numbering = 0

    def still_continue(self):
        return self.numbering < len(self.questions)

    def next_questions(self):
        current_question = self.questions[self.numbering]
        self.numbering += 1
        user_answer = input(f"Q{self.numbering}: {current_question.text} True/False :")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print(f"Right!")
        else:
            print(f"Wrong!")
        print(f"current score : {self.score}")
        print(f"the correct answer : {correct_answer}")

