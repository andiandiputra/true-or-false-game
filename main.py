from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_list = []
for question in question_data:
    text = question['question']
    answer = question['correct_answer']
    questions = Question(text, answer)
    question_list.append(questions)

quiz = Quiz(question_list)

while quiz.still_continue():
    quiz.next_questions()

print(f"You have completed the quiz, Your final score is: {quiz.score}")



