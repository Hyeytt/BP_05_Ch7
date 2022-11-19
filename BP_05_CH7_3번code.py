import turtle                    # turtle 함수를 불러온다              
t = turtle.Turtle()              # 변수 t를 터틀 함수와 같다고 정한다
t.shape("turtle")                # 커서 모양을 거북이 모양으로 정한다
t.speed(0)                       # speed를 사용해 프로그램 작동속도를 빠르게 한다. 괄호 안의 0은 속도을 의미한다.
def f(x):                        # f(x)함수를 정의 내린다
  return x**2+1                  # 결괏값을 받는 return함수를 사용한다.

t.goto(200, 0)                   # 200,0의 좌표로 거북이를 이동시킨다
t.goto(0, 0)                     # 0,0의 좌표로 거북이를 이동시킨다 
t.goto(0, 200)                   # 0,200의 좌표로 거북이를 이동시킨다.
t.goto(0, 0)                     # 0,0의 좌표로 거북이를 이동시킨다.

for x in range(150):             # 아래의 문장을 150번 반복한다 
     t.goto(x, int(0.01*f(x)))   # 해당하는 좌표로 이동시킨다. x좌표에는 x의 값에 해당하는 만큼, y좌표에는 0.01에 함수 f(x)의 결괏값(return함수)를 곱한 값이 부여된다
