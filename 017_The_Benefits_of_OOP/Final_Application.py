import data
import question_model
import quiz_brain
from replit import clear

clear()
x = data.question_data
question_bank = []
for item in x:
    n_question = item["text"]
    n_answer = item["answer"]
    y = question_model.Question(n_question, n_answer)
    new_question = y
    question_bank.append(new_question)
z = quiz_brain.QuizBrain(question_bank)
quiz = z
while quiz.still_has_questions():
    quiz.next_question()
clear()
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")