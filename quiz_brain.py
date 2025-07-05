import random

class Quiz:

    def __init__(self,questions_list):
        self.questions = questions_list
        self.score = 0
        self.numbering = 0
        self.index = random.randint(0, len(self.questions)-1)
        self.used_question = []
        self.is_quiz_active = True

    def still_continue(self):
        return self.numbering < 10 and self.is_quiz_active

    def next_questions(self):
        while self.index in self.used_question:
            self.index = random.randint(0, len(self.questions)-1)
        current_question = self.questions[self.index]
        self.used_question.append(self.index)
        self.numbering += 1
        user_answer = input(f"Q{self.numbering}: {current_question.text} True/False :").capitalize()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == "Exit":
            self.is_quiz_active = False
        elif user_answer == correct_answer:
            self.score += 1
            print(f"Right!")
        else:
            print(f"Wrong!")
        print(f"current score : {self.score}\nthe correct answer : {correct_answer}")

