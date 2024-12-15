class QuizBrain:
    # 질문 번호
    # 점수
    # 질문 리스트
    def __init__(self, q_list):
        self.question_number = 0 # 질문 번호 기본값 0
        self.score = 0 # 점수 기본값 0
        self.question_list = q_list # 질문 리스트는 main.py 에서 data 불러와 저장한 데이터를 넣움

    # 질문을 계속 지속하는 메소드
    def still_has_question(self):
        return self.question_number < len(self.question_list) # 질문 번호가 질문 리스트의 크기보다 작은경우 = True
    # while 문에서 True 면 계속 유지된다
    # False 가 나오면 While 문 정지


    # 다음 질문 메서드
    def next_question(self):
        current_question = self.question_list[self.question_number] # 현재 질문 = 변수로 받은 질문 리스트[질문 번호]
        self.question_number += 1 # 질문 번호에 1 더한다
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True / False):") # 사용자의 답을 받는다
        self.check_answer(user_answer, current_question.answer) # 답을 확인하는 매소드 호출. (사용자답, 현재질문의 답)

    # 답을 확인하는 메소드
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower(): # 사용자의 답 소문자화 == 정답 소문자화
            self.score += 1 # 점수 1 더하기
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was : {correct_answer}") # 올바른 정답 출력문
        print(f"Your current score is : {self.score} / {self.question_number}") # 현재 점수 3/10 형태로 출력
        print("\n")
