import turtle                             # 터틀 함수를 불러온다 
t = turtle.Turtle()                       # 변수 t를 터틀 함수와 같다고 정한다
t.shape("turtle")                         # t의 모양을 거북이 모양으로 정한다
t.color("black", "white")                 # t의 색깔은 검은색과 하얀색이다
s = turtle.Screen(); s.bgcolor('skyblue');# s에 화면에 해당하는 값을 설정하고 bgcolor인 배경값으로 skyblue색으로 칠한다는 뜻
def draw_snowman(x, y):                   # draw_snowman 함수를 설정한다, 눈사람 모양을 그리는 함수이다
    t.up()                                # 눈사람 머리를 그리는 문장들. 펜을 들어올린다. 
    t.goto(x, y)                          # 거북이를 x,y좌표로 이동시킨다
    t.down()                              # 펜을 내린다
    t.begin_fill()                        # 도형의 색을 칠하기 시작한다
    t.circle(20)                          # 20의 크기인 원을 그린다
    t.end_fill()                          # 도형의 색을 칠하기를 멈춘다
    t.goto(x, y-25)                       # x좌표는 그대로, y좌표는 아래쪽으로 25만큼 이동시킨다

    t.setheading(135)                     # 눈사람의 팔을 그리는 문장들이다. 거북이의 머리방향을 135도로 설정한다
    t.forward(50)                         # 앞으로 50만큼 이동시킨다
    t.backward(50)                        # 뒤로 50만큼 이동시킨다
    t.setheading(30)                      # 거북이의 머리방향을 130도로 설정한다
    t.forward(50)                         # 앞으로 50만큼 이동시킨다
    t.backward(50)                        # 뒤로 50만큼 이동시킨다
    t.setheading(0)                       # 거북이의 머리방향을 0도로 설정한다

    t.begin_fill()                        # 눈사람의 몸통을 그리는 문장이다. 도형의 색을 칠하기 시작한다
    t.circle(15)                          # 15의 크기인 원을 그린다
    t.end_fill()                          # 도형의 색을 칠하기를 멈춘다
    t.goto(x, y-70)                       # x좌표는 그대로 두고 아래쪽으로 70만큼 이동시킨다
    t.begin_fill()                        # 눈사람의 아랫부분을 그리는 문장이다. 도형의 색을 칠하기 시작한다          
    t.circle(30)                          # 30의 크기인 원을 그린다
    t.end_fill()                          # 도형의 색을 칠하기를 멈춘다

draw_snowman(0, 0)                        #draw_snowman함수를 (0,0)에 그린다     
draw_snowman(100, 0)                      #draw_snowman함수를 (100,0)에 그린다     
draw_snowman(200, 0)                      #draw_snowman함수를 (200,0)에 그린다     
