# attributes = text, answer ex) new_q = Question("2+3=5", "True")

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# question_data 에서 키 (text), 밸류 (answer) 저장
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank) # quiz 변수에 QuizBrain 초기화

while quiz.still_has_question(): # QuizBrain 클래스 내의 계속 질문을 이어가게 해주는 메소드 실행 (Fals 나오면 멈춤)
    quiz.next_question() # quiz.still_has_question() 이 False 가 나올때 까지 이 메소드 실행


print("You've completed the quiz")
print(f"Your final score was : {quiz.score} / {quiz.question_number}")