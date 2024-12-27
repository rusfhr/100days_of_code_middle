from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
timmy_the_turtle.speed(1)

# for i in range(0, 4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# 입력받은 수 만큼 도형 그리기
def draw_shape(num):
    angle = 360 / num # 각이 점점 줄어든다 (삼각형 -> 사각형 -> 오각형 ->...)

    for i in range(num):
        timmy_the_turtle.forward(100) # 100만큼 이동
        timmy_the_turtle.right(angle) # 오른쪽으로 angle만큼 회전

for n in range(3, 11):
    draw_shape(n)

screen = Screen()
screen.exitonclick()