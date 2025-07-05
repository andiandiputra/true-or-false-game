from data import question_data, logo
from question_model import Question
from quiz_brain import Quiz
import os

question_list = []
for question in question_data:
    text = question["questions"]
    answer = question["answer"]
    questions = Question(text, answer)
    question_list.append(questions)

def clear():
        os.system('cls')

def play():
    quiz = Quiz(question_list)
    clear()
    print(logo)
    while quiz.still_continue():
        quiz.next_questions()
    print(f"\nYou have completed the quiz, Your final score is: {quiz.score}")
    play_again = input("Play Again ? y/n").lower()
    if play_again == "y":
         play()
    else:
         print("GGWP!")

play()
    




