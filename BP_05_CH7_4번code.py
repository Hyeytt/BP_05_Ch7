import turtle                        # turtle 함수를 불러온다
t = turtle.Turtle()                  # 변수 t를 turtle값으로 인식한다
t.shape("turtle")                    # 커서 모양을 거북이의 모양으로 한다
t.speed(0)                           # 프로그램 작동속도를 빠르게 한다
def draw_line():                     # draw_line 함수를 설정한다
    t.forward(100)                   # 거북이를 앞으로 100만큼 이동시킨다
    t.backward(100)                  # 거북이를 뒤로 100만큼 이동시킨다
for x in range(12):                  # 아래 문장들을 12번 반복한다 
    t.right(30)                      # 거북이를 오른쪽으로 30도 회전시킨다
    draw_line()                      # draw_line함수를 출력시킨다
