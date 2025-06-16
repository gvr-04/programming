from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

questions = []
for question in question_data:
    questions.append(Question(question["text"], question["answer"]))
#    print(question["answer"], end=' ')
# UNCOMMENT ABOVE LINE TO REVEAL ALL ANSWERS


quiz_brain = QuizBrain(questions)
quiz_brain.next_question()

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("\n\nYou Have Completed The Quiz")
print(f"Your Final Score Is: {quiz_brain.correct}/{quiz_brain.question_numer}.")
