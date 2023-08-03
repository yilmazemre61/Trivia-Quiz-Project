from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    category = question["category"]
    question_bank.append(Question(text=text, answer=answer, category=category))


quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():

    quiz_brain.next_question()

print("You've completed the Quiz")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")
