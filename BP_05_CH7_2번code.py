import turtle                       # 터틀 함수를 불러온다 
t = turtle.Turtle()                 # 변수 t를 터틀 함수와 같다고 정한다
t.shape("turtle")                   # t의 모양을 거북이 모양으로 정한다
t.speed(0)                          # 그려지는 속도를 빠르게 하는 문장
def hexagon():                      # 육각형을 그리는 hexagon이라는 이름의 함수를 설정.
  for i in range(6):                # 아래의 문장들을 6번 반복한다
    turtle.forward(100)                  # 거북이를 앞으로 100만큼 이동시킨다
    turtle.left(360/6)                   # 거북이를 왼쪽으로 120만큼 회전시킨다

for i in range (6):                 # 아래의 문장들을 6번 반복한다
    hexagon()                         # hexagon함수를 출력한다
    turtle.forward(100)               # 거북이를 앞으로 100만큼 이동시킨다
    turtle.right(60)                  # 거북이를 오른쪽으로 60만큼 회전시킨다
