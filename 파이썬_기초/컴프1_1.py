# 1주차
print("Hello")
print("'안녕하세요?'")
print(2+3)
print(2*3)
print(2/3)
print(7//3) # 몫
print(7%3) # 나머지

print("반가워요" * 20)
print("100"+"200") # 문자열+문자열
print(100+200) # 숫자+숫자

import turtle
t = turtle.Turtle()
t.shape("turtle")

t.forward(100)
t.left(120)  # 진행방향의 왼쪽으로 120도 회전
t.circle(100) # 반지름이 100인 원을 그림
t.width(10) # 선 굵기 10  t.pensize(굵기)

print("너무", "반짝"*2, "눈이 부셔", "No "*5)


# 2주차
import turtle
t = turtle.Turtle()
t.shape("square")  # 모양 square(arrow, turtle, circle, triangle, classic)
t.color("blue")   # 색깔 or #000000 ~ #ffffff

t.down()  # 펜을 내림  t.pendown(), t.pd()
t.goto(100,0)  # (100,0)까지 선을 그리며 이동
t.up()  # 펜을 올림  t.penup(), t.pu()
t.goto(0,200) # (0,200)까지 선을 그리지 않고 이동
t.down()   # 펜을 내림
t.goto(100,200)  # (100,200)까지 선을 그리며 이동

# 출력 형태 정리
# 1. ,(콤마) : print("학과 :", "컴퓨터공학"), print("학번 :", 2021)
# 2. format함수 : print("학과 : {}".format("컴퓨터공학")), print("학과 : {}, 학번 : {}".format("컴퓨터공학", 2021))
#    format함수 변수의 순서 사용 : print("학과 : {0}, 학번 : {1}".format("컴퓨터공학", 2021))
#                            print("학과 : {0}, 전공 : {0}, 학번 : {1}".format("컴퓨터공학, 2021"))
#
# 4. % 사용 : print("학과 : %s"%("컴퓨터공학")), print("학과 : %s, 학번 : %s"%("컴퓨터공학", 2021))
#           %d : 정수, %f : 실수, %s : 문자열
# 5. - + 연산자 이용 : print("학과 : "+"컴퓨터공학"), print("학과 : "+"컴퓨터공학, "+"학번 : "+str(2021))

# 변수
x = 100
y = 200
sum1 = x+y
print(sum1)
print(x, "과", y, "의 합은", sum1, "입니다.")
print("{}과 {}의 합은 {}입니다.".format(x, y, sum1))
print("%s과 %s의 합은 %s입니다."%(x, y, sum1))
print(str(x)+"과 "+str(y)+"의 합은 "+str(sum1)+"입니다.")


# 1. 변수의 이름은 영문자와 숫자, 밑줄 문자(_)로 이뤄진다.
# 2. 변수의 이름은 중간에 공백이 들어가면 안 된다.
# 3. 변수의 이름은 숫자로 시작할 수 없다.
# 4. 변수의 이름에 쓰이는 영문자는 대문자와 소문자로 구별한다.

# input은 문자열로 인식함 / int() 문자열 정수로 변환, float() 문자열을 실수로 변환
x = int(input("첫 번째 정수를 입력하시오: "))
y = int(input("두 번째 정수를 입력하시오: "))
sum = x + y
print(x,"과",y,"의 합은",sum,"입니다.")

x, y = input("수 2개 입력: ").split(" ")   # input을 여러개 받을 때 .split(" ") 사용
print(type(x))  # x의 타입 확인
print(type(y))
x, y = int(x), int(y)

import turtle
t = turtle.Turtle()
t.shape("turtle")

radius = int(input("원의 반지름을 입력하시오: "))
color = input("원의 색깔을 입력하시오: ")

t.color(color)
t.begin_fill()   # 채우기
t.circle(radius)
t.end_fill()


# 3주차

#오륜기 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(5)

t.up()
t.goto(-150, 0)
t.down()
t.color("blue")
t.circle(80)

t.up()
t.goto(0, 0)
t.down()
t.color("black")
t.circle(80)

t.up()
t.goto(150, 0)
t.down()
t.color("red")
t.circle(80)

t.up()
t.goto(-80, -100)
t.down()
t.color("yellow")
t.circle(80)

t.up()
t.goto(80, -100)
t.down()
t.color("green")
t.circle(80)

# 줄바꾸기
print("신재훈\n"*20, end="")

# 수 3개 입력, 입력한 수 평균, 4가지 출력형태
num1 = int(input("첫 번째 수를 입력하시오.: "))
num2 = int(input("두 번째 수를 입력하시오.: "))
num3 = (input("세 번째 수를 입력하시오.: "))
num3 = int(num3)

num1, num2, num3 = input("수 3개 입력: ").split(" ")
num1, num2, num3 = int(num1), int(num2), int(num3)

print(num1, num2, num3, "의 평균은", ((num1+num2+num3)/3,"입니다."))
print("{} {} {}의 평균은 {}입니다.".format(num1, num2, num3, (num1+num2+num3)/3))
print("%s %s %s의 평균은 %s입니다."%(num1,num2,num3,(num1+num2+num3)/3))
print(str(num1)+" "+str(num2)+" "+str(num3)+"의 평균은"+str((num1+num2+num3)/3)+"입니다.")

# 삼각형 한 변의 길이 입력, 삼각형 그리기, 색상 입력, 삼각형 채우기
import turtle
t = turtle.Turtle()
t.shape("turtle")

side = int(input("한 변의 길이 입력: "))
color_name = input("색상명 입력: ")
t.color(color_name)
t.begin_fill()
t.fd(side)
t.lt(120)
t.fd(side)
t.lt(120)
t.fd(side)
t.lt(120)
t.end_fill()

# 원의 반지름 입력, 원 3개 반지름 20씩 증가, 색상 입력, 원 색상 채우기
import turtle
t = turtle.Turtle()
t.shape("turtle")

radius = int(input("반지름을 입력하시오: "))
color_name = input("색상명 입력: ")
t.up()
t.goto(-100,0)
t.down()
t.color(color_name)
t.begin_fill()
t.circle(radius)
t.end_fill()

color_name = input("색상명 입력: ")
t.up()
t.goto(0,0)
t.down()
t.color(color_name)
t.begin_fill()
t.circle(radius+20)
t.end_fill()

color_name = input("색상명 입력: ")
t.up()
t.goto(100,0)
t.down()
t.color(color_name)
t.begin_fill()
t.circle(radius+40)
t.end_fill()

# 문자열 숫자 하나씩 입력, 입력한 문자열이 숫자만큼 반복 출력
str1 = input("문자열 입력: ")
num1 = int(input("반복 횟수 입력: "))

print(str1*num1)

# 리본 크기를 입력, 입력 값을 통해 리본 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")

size = int(input("리본 크기 입력: "))
t.lt(90)
t.fd(size)
t.rt(120)
t.fd(size*2)
t.lt(120)
t.fd(size)
t.lt(120)
t.fd(size*2)

# 산술 연산자
** : 지수(제곱)
/ : 나누기
// : 몫
% : 나머지

sec = 1000
min = sec // 60
remainder = sec % 60
print(min,'분',remainder,'초')

# 복합 대입 연산자
x += 2 와 x = x+2 같음
x += y, x = x+y
x = x*2+3과  x *= 2+3은 다름 (복합 대입 연산자 우선순위가 가장 낮음)

# 화씨 온도
f = int(input("화씨온도: "))
c = (f-32)*5/9
print("섭씨온도: %s"%(c))

# 소수점 제한
print("%.2f"%(3.7452))  # 3.75
print("{}".format(round(3.7452, 2))) # 3.75
print("%.0f"%(3.7452)) # 4
print("{}".format(round(3.7452, 0))) # 4.0
print("{}".format(int(3.7452))) # 3

# 거리 계산
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

distance = ((x2-x1)**2 + (y2-y1)**2)**0.5

print("두 점 사이의 거리= "+str(round(distance, 2)))


# 4주차

# 현재 한국 시간
import time
fseconds = time.time()  # 1970.1.1.~ 현재까지 초
print(fseconds)
total_sec = int(fseconds)
total_min = total_sec // 60  # 전체 분
minute = total_min % 60
print(minute)
total_hour = total_min // 60
print(total_hour)
hour = total_hour % 24 + 9
print(hour)
print("현재 한국 시간: "+str(hour)+"시 "+str(minute)+"분")

# 계산대 프로그램
money = int(input("투인한 돈: "))
price = int(input("물건가격: "))

change = money - price
print("거스른돈: ", change)

coin500 = change // 500
change = change % 500

coin100 = change // 100

print("500원 동전 개수:", coin500)
print("100원 동전 개수:", coin100)

# 수를 3개 입력, (덧셈, 뺄셈, 곱셈, 나눗셈(2), 나머지(2), 지수(2)) 연산
n1 = int(input("수1 입력: "))
n2 = int(input("수2 입력: "))
n3 = int(input("수3 입력: "))

print("덧셈(+) : ", end="")
print("%s + %s + %s = %s"%(n1,n2,n3,n1+n2+n3))
print("뺄셈(-) : ", end="")
print("%s - %s - %s = %s"%(n1,n2,n3,n1-n2-n3))
print("곱셈(*) : ", end="")
print("%s * %s * %s = %s"%(n1,n2,n3,n1*n2*n3))
print("나눗셈(/) : ", end="")
print("%s / %s = %s"%(n1,n2,n1/n2))
print("나머지(%) : ", end="")
print("%s %% %s = %s"%(n1,n2,n1%n2))  # %s %s 사이에 %를 쓰려면 %%
print("지수(**) : ", end="")
print("%s ** %s = %s"%(n1,n2,n1**n2))
print("%s,%s,%s 중 최댓값 : %s"%(n1,n2,n3,max(n1,n2,n3)))
print("%s,%s,%s 중 최솟값 : %s"%(n1,n2,n3,min(n1,n2,n3)))

# 돈의 액수를 입력 / 만원짜리, 천원짜리, 백원짜리, 십원짜리 개수를 각각 계산하여 출력
money = int(input("돈의 액수 : "))
m = money
m10000 = m//10000
m %= 10000
m1000 = m//1000
m %= 1000
m100 = m//100
m %= 100
m10 = m//10

print("%s원은"%(money))
print("만원 : %s장"%(m10000))
print("천원 : %s장"%(m1000))
print("백원 : %s개"%(m100))
print("십원 : %s개"%(m10))

# 원기둥의 부피를 계산 / 반지름과 높이를 각각 입력 받음
r = float(input("반지름 : "))
h = float(input("높이 : "))
vol = 3.141592 * r**2 * h

print("원기둥의 높이 : " + str(vol))

# 정수를 하나 입력받음(4자리) / 입력한 정수의 각 자릿수의 합을 출력
num = int(input("정수 입력 네 자리 : ")) #1234
sum1 = 0
sum1 += (num%10)  # 4
num //= 10   # 123
sum1 += (num%10) # 4 + 3
num //= 10 # 12
sum1 += (num%10) # 4 + 3 + 2
num //= 10 # 1
sum1 += (num%10) # 4 + 3 + 2 + 1

print("자릿수의 합 : "+str(sum1))

# 물체의 무게 속도 입력받음 / 운동 에너지 계산 후 출력
w = float(input("무게 : "))
s = float(input("속도 : "))
e = 0.5 * w * s**2

print("물체의 에너지 : "+str(e))

# 두 점을 입력 / 터틀 그래픽으로 두 점을 연결하는 직선을 그림 / 길이 계산
import turtle
t = turtle.Turtle()
t.shape("turtle")

x1 = int(input("x1값 : "))
y1 = int(input("y1값 : "))
x2 = int(input("x2값 : "))
y2 = int(input("y2값 : "))

dist = ((x2-x1)**2 + (y2-y1)**2)**0.5

t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)
t.write("선의 길이 = "+str(dist))

# 자료
정수(int) : ...-2,-1,0,1,2...
실수(float) : 3.2, 3.14, 01234
문자열(str) : "Hello world", "123"

type() : 타입 함수

# 줄바꿈 : \n , ''', """

poem ='''이렇게 정다운
너 하나 나 하나는
어디서 무엇이 되어
다시 만나랴'''

p1 = """tes1
test2 "end" """

# 인덱스
01234567891011
Hello Python
-12-11-10-9-8-7-6-5-4-3-2-1

# 슬라이싱
s[a:b:c] a<b 이고 c>0 이면 a부터 b-1까지의 c간격
         a>b 이고 c<0 이면 a부터 b+1까지의 c간격
s[0::1] : s[0]에서부터 문자열 끝까지 1간격의 문자열
s[-1::-1] : s[-1]에서부터 문자열 처음까지 -1간격의 문자열


# 5주차

# 소금물의 농도
salt = int(input("소금의 양: "))
salt_water = int(input("소금물의 양: "))
density = salt / (salt+salt_water) * 100

print("소금물의 농도: %.2f%%"%(desity))  # %를 쓰고 싶을 때는 %% / print("소금물의 농도: {}%".format(round(density,2)))

# 챗봇 프로그램


# 터틀 텍스트입력
import  turtle
t = turtle.Turtle()
t.shape("turtle")

str1 = turtle.textinput("테스트", "입력 테스트입니다.")
print(str1)
t.write("안녕하세요?",True,"center",("", 15, "bold"))

# 글자 25, 기울임꼴, 가운데 정렬, 거북이 이동여부 없음
import  turtle
t = turtle.Turtle()
t.shape("turtle")

t.write("안녕하세요?",False,"center",("", 25, "italic"))

# 이름 입력 받아 출력, 네모 그림
import  turtle
t = turtle.Turtle()
t.shape("turtle")

str1 = turtle.textinput("", "이름을 입력하시오.")
t.write("안녕하세요?"+str1+"씨", False, "left", ("", 15, "italic"))
t.write("안녕하세요? %s씨"%(str1), False, "left", ("", 15, "italic"))
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)

# 이름 입력 받음, 화면 상단 가운데 이름 출력, 길이 100 사각형, 사각형 정가운데 위치 헤드방향 위쪽
import turtle
t = turtle.Turtle()
t.shape("turtle")
str1 = turtle.textinput("", "이름을 입력하시오.")
t.up()
t.goto(0,200)
t.write("안녕하세요?"+str1+"씨, 터틀 인사드립니다.", False, "center", ("", 20, "bold"))

t.goto(-50,-50)
t.down()
t.goto(50,-50)
t.goto(50,50)
t.goto(-50,50)
t.goto(-50,-50)
t.up()
t.goto(0,0)
t.seth(90)

# 암호프로그램 만들기
plane_txt = input("평문 입력: ")
crypt_txt1 = plane_txt[-1: :-1]
print("암호문1: "+crypt_txt1)
crypt_txt2 = plane_txt[0] + plane_txt[-2: -len(plane_txt): -1] + plane_txt[-1]
print("암호문2: "+crypt_txt2)

# 현재 년도 출력, 현재 나이와 년도 입력받아 입력한 년도에 나이가 어떻게 되는지 출력
import time
now = time.time()
thisYear = int(1970 + now//(365*24*3600))
print("올해는"+str(thisYear)+"년 입니다.")

age = int(input("현재 나이: "))
year = int(input("년도 입력: "))

print("%s년에는 "%(year) + str(age+year-thisYear)+"살 입니다.")

# 터틀 그래픽에서 이름과 반지름 입력 받음, ~씨 원을 그려봅시다 상단 가운데 출력, 글자크기 20 굵게 거북이 이동 없음
# 원의 반지름 길이를 절반씩 줄여가면서 3개를 그림(화면 중간에 그려지도록 함)
import  turtle
t = turtle.Turtle()
t.shape("turtle")

str1 = turtle.textinput("", "이름을 입력하시오.")
radius = int(input("반지름을 입력하시오. "))
t.up()
t.goto(0,300)
t.write(str1+"씨, 원을 그려봅시.", False, "center", ("", 20, "bold"))

t.up()
t.goto(0,0)
t.down()
t.circle(radius)

t.up()
t.goto(0,50)
t.down()
t.circle(radius/2)

t.up()
t.goto(0,75)
t.down()
t.circle(radius/4)

# 조건문
score = 90
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")
print("수고하셨습니다.")


lang = int(input("언어를 선택(1:한국어, 2:영어, 3:프랑스어, 4:독일어): "))

if lang == 1:
    print("안녕")
if lang == 2:
    print("Hello")
if lang == 3:
    print("bonjour")
if lang == 4:
    print("Guten morgen")


num = int(input("정수를 입력하시오: "))
if num %2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")


a,b = input("변 a,b 길이를 각각 입력: ").split(" ")
a,b = int(a),int(b)
c = int(input("변 c 길이를 입력: "))

if (a**2 + b**2) == c**2:
    print("직각삼각형입니다.")
else:
    print("직각삼각형이 아닙니다.")

# 정수를 입력 받아 그에 따라 터틀 양의 정수(100,100), 0(100,0), 음의 정수(100,-100)으로 이동
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.up()
t.goto(100,100)
t.write("입력된 정수는 양의 정수입니다.")
t.goto(100,0)
t.write("입력된 정수는 0입니다.")
t.goto(100,-100)
t.write("입력된 정수는 음의 정수입니다.")

t.goto(0,0)
t.down()

s = int(turtle.textinput("", "숫자를 입력하시오: "))

if s > 0:
    t.goto(100,100)
elif s == 0:
    t.goto(100,0)
else:
    t.goto(100,-100)

if s >= 0:
    if s > 0:
        t.goto(100,100)
    else:
        t.goto(100,0)
else:
    t.goto(100,-100)


# 6주차

# 주민번호 뒷자리 첫 번째 번호를 랜덤 생성, 뒷자리 첫 번째 번호 남(1,3), 여(2,4) 판별에 사용
import random
print("주민 번호 뒷자리의 첫 번째 번호를 생성합니다.")
gender = random.randint(1,4)
gender = random.randrange(1,5)  # 1 ~ (5-1)
gender = random.randrange(1,5,1)  # 1 ~ (5-1), 간격 1
gender = random.randrange(4) + 1  # 0 ~ 3 / + 1

print("생성번호: " +str(gender))
if gender == 1 or gender == 3:  # if gender == 1 or 3: (x)  0:거짓, 0 이외의 값:참
    print("남성입니다.")
else:
    print("여성입니다.")

# 동전 던지기 게임
import turtle, random
t = turtle.Turtle()
t.shape("turtle")

scr1 = turtle.Screen()   ######## 이미지 호출에 필요한 것들
front = "front.gif"
back = "back.gif"
scr1.addshape(front)
scr1.addshape(back)

t1 = turtle.Turtle()
coin = random.randint(0,1)

if coin == 0:
    t1.shape(front)
    t1.up()
    t1.goto(-200,0)
    t1.stamp()
    t1.goto(200,0)
else:
    t1.shape(back)
t1.stamp()

# 전기회로
a = input("1번 전지가 있습니까?(y/n): ")
b = input("2번 전지가 있습니까?(y/n): ")

if a.upper() == "Y":  # if a == "y" or a == "Y" or if a.lower() == "y":
    if b.upper() == "Y":
       print("직렬연결": 전구에 불이 켜집니다.)
    else:
       print("직렬연결: 전구에 불이 꺼집니다.")
else:
    print("직렬연결: 전구에 불이 꺼집니다.")
    if b.upper() == "Y":
        print("병렬연결: 전구에 불이 켜집니다.")
    else:
        print("병렬연결: 전구에 불이 꺼집니다.")

# 윤년 판단
year = input("년도를 입력: ")

if (year%4==0 and year%100 != 0) or (y%400 == 0):
    print("{}년은 윤년입니다.".format(year))
else:
    print("%s년은 윤년이 아닙니다."%(year))

# 이차방정식의 판별식
a, b, c = input("a, b, c 값을 순서대로 입력: ").split(" ")
a, b, c = float(a), float(b), float(c)
d = b**2 -4*a*c

if d > 0:
    print("방정식의 근은 서로 다른 두 실근입니다.")
elif d == 0:
    print("방정식의 근은 서로 같은 두 실근(중근)입니다.")
else:
    print("방정식의 근은 서로 다른 두 허근입니다.")

# 사용자가 원하는 도형 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.hideturtle()

s = turtle.textinput("","지울까요?(y/n): ")

if s.upper() == "Y":
    t.clear()
    t.showturtle()
t.home()

# 동전 던지기 문제 / 동전 2개 같은면 성공 다른 면 실패 / 상단에 결과 출력
import turtle, random
scr1 = turtle.Screen()
front = "front.gif"
back = "back.gif"
scr1.addshape(front)
scr1.addshape(back)
t1 = turtle.Turtle()
coin1 = random.randint(0,1)
t1.up() # turtle이 움직일 때 선을 그리지 않도록 하기 위해
t1.goto(-150,0)
if coin1 == 0:
    t1.shape(front)
else:
    t1.shape(back)
t1.stamp() # 화면에 동전 이미지를 남기기 위해

t1.goto(150,0)
coin2 = random.randint(0,1)
if coin2 == 0:
    t1.shape(front)
else:
    t1.shape(back)
t1.stamp()

t1.hideturtle()
t1.goto(0,150)
if coin1 == coin2:
    t1.write("성공", False, "center", ("", 20, "bold"))
else:
    t1.write("실패", False, "center", ("", 20, "bold"))

# 도형 종류 입력 받음 / 직사각형 가로 세로 각각 입력 / 정삼각형 한 변의 길이 입력 / 원은 반지름 입력
import turtle, random
t = turtle.Turtle()
t.shape("turtle")

figure = turtle.textinput("", "도형을 입력하세요: ")

if figure == "직사각형":
    w = int(turtle.textinput("", "가로 길이 입력: "))
    h = int(turtle.textinput("", "세로 길이 입력: "))
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
elif figure == "정삼각형":
    w = int(turtle.textinput("", "한 변의 길이 입력: "))
    t.fd(w)
    t.lt(120)
    t.fd(w)
    t.lt(120)
    t.fd(w)
elif figure == "원":
    r = int(turtle.textinput("", "반지름 입력: "))
    t.circle(r)
else:
    t.hideturtle()
    t.write("%s 도형을 그릴 수 없습니다."%(figure), False, "center", ("",25,"bold"))

# 앞 문제 추가 / 사각형으로 입력 받고 가로 세로 같으면 정사각형 다르면 직사각형 이라고 출력
if figure == "사각형":
    w = int(turtle.textinput("", "가로 길이 입력: "))
    h = int(turtle.textinput("", "세로 길이 입력: "))
    t.up()
    t.goto(0,250)
    t.down
    if w == h:
        t.write("정사각형", False, "center", ("", 20, "italic"))
    else:
        t.write("직사각형", False, "center", ("", 20, "italic"))
    t.up()
    t.home()
    t.down()
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)
    t.fd(w)
    t.lt(90)
    t.fd(h)
    t.lt(90)

# 두 원의 위치 관계 시뮬레이션

# up, down 입력 받음 / 육면체 주사위를 던져 눈값을 하나 얻음(랜덤) / 1~3 그리고 down이면 성공 출력
# 4~6 그리고 up이면 성공 출력 / 다른 경우 실패 출력 / up, down 아닌 다른 값은 잘못 입력 출력
import random
ud = input("'up', 'down' 중 하나 입력: ")
dice = random.randint(1,6)

if ud == "up" or ud == "down":
    if (dice >= 1 and dice <= 3) and ud == "down" :
        print("주사위 눈값: %s"%(dice))
        print("성공")
    elif 4 <= dice <= 6 and ud == "up":
        print("주사위 눈값: %s"%(dice))
        print("성공")
    else:
        print("주사위 눈값: %s"%(dice))
        print("실패")
else:
    print("잘못 입력하였습니다.")

# for 반복문 (반복 횟수를 알 때)
for i in range(5): # 0 ~ 4
    print("%s 번째 방문을 환영합니다."%(i+1))

for i in range(10, 0, -1):  # 10 ~ 1
    print(i, end="")


# 7주차

# 키보드를 5개 이상 사면 10% 할인 / 키보드 구매 개수 입력 받음 / 키보드 가격 8500원
# 5개 이상 하면 10퍼 할인된 금액, 5개 미만이면 할인되지 않은 금액 출력
keyb = 8500
num = int(input("키보드 구매 개수를 입력: "))
totla_price = keyb * num

if num >= 5:
    totla_price *= 0.9

print("총 가격은 %.0f원"%(totla_price))

# 문자열을 하나 입력받음 / 입력된 문자열의 길이가 8 이상이 되면 길이만큼 각 라인별로 출력
# 입력된 문자열의 길이가 8미만인 경우 길이만큼 한 라인에 문자열을 출력
# 단, 한 라인에 출력될 때는 문자열 사이에 공백이 들어가도록 함
str1 = input("문자열을 입력: ")
str_len = len(str1)

if str_len >= 8:
    print((str1+"\n")*str_len, end="")
else:
    print((str1+" ")*str_len)

# 키보드 구매 개수를 입력 받음 / 키보드 가격은 8500원 / 키보드 5개이상 10개미만 사면 5%할인
# 10개 이상 20개 미만은 경우 10%할인, 20개이상 30개 미만 15%, 30개 이상 20%
# 구매개수 50개를 초과할 수 없음
keyb = 8500
num = int(input("키보드 구매 개수를 입력: "))
total_price = keyb * num

if num < 5:
    print("총 가격은 %.0f원"%(total_price))
elif 5 <= num < 10:  # num >= 5 and num < 10
    print("총 가격은 %.0f원" % (total_price*0.95))
elif 10 <= num < 20:
    print("총 가격은 %.0f원" % (total_price*0.9))
elif 20 <= num < 30:
    print("총 가격은 %.0f원" % (total_price*0.85))
elif 30 <= num < 50:
    print("총 가격은 %.0f원" % (total_price*0.8))
else:
    print("50개를 초과할 수 없습니다.")

# ver2
if num < 5:
    totla_price *= 1
elif 5 <= num < 10:  # num >= 5 and num < 10
    totla_price *= 0.95
elif 10 <= num < 20:
    totla_price * 0.9
elif 20 <= num < 30:
    totla_price * 0.85
elif 30 <= num:
    totla_price * 0.8
else:
    flag = False

if flag:   # flag == True
    print("총 가격은 %.0f원"%(totla_price))
else:
    print("50개를 초과할 수 없습니다.")

# 주사위 이미지를 이용하여 랜덤으로 주사위 눈값 이미지가 나오도록 하시오
import turtle, random

scr = turtle.Screen()

dice1 = "dice1.gif"
dice2 = "dice2.gif"
dice3 = "dice3.gif"
dice4 = "dice4.gif"
dice5 = "dice5.gif"
dice6 = "dice6.gif"

scr.addshape(dice1)
scr.addshape(dice2)
scr.addshape(dice3)
scr.addshape(dice4)
scr.addshape(dice5)
scr.addshape(dice6)

t = turtle.Turtle()
dice = random.randint(1,6)

if dice == 1:
    t.shape(dice1)
elif dice == 2:
    t.shape(dice2)
elif dice == 3:
    t.shape(dice3)
elif dice == 4:
    t.shape(dice4)
elif dice ==5:
    t.shape(dice5)
else:
    t.shape(dice6)

# 로그인 프로그램 / 올바른 아이디가 입력됐을 때 패스워드를 입력 받음
# 패스워드가 일치하면 "환영합니다."출력 아니면 "패스워드가 틀렸습니다."출력
# 올바른 아이디가 입력되지 않으면 "아이디를 찾을 수 없습니다."출력

id_1 = "sjhh0105"
passward_1 = "1234"

s = input("아이디를 입력: ")
if s == id_1:
    p = input("패스워드 입력: ")
    if p == passward_1:
        print("환영합니다.")
    else:
        print("패스워드가 틀렸습니다.")
else:
    print("아이디를 찾을 수 없습니다.")

# 특수 문자 하나를 입력받음 / 높이가 5인 삼각형을 만든다
s = input("특수 문자: ")

for i in range(5):  # 시퀀스 0 ~ 4
    print(s*(i+1))

# 문자열 하나를 입력받음 / 입력한 문자들 사이사이에 공백문자를 넣어 출력한다.
s = input("문자열 입력: ")

for i in s:
    print(i, end=" ")

# 터틀 그래픽을 이용해 별을 그려라(144도) / 한 변의 길이는 50~200 랜덤
import turtle, random
t = turtle.Turtle()
t.shape("turtle")

s = random.randint(50,200)

for i in range(5):
    t.fd(s)
    t.rt(144)

# 횟수 제어 반복
sum = 0
for i in range(1,101): # 1, 2, ... 99, 100
    sum += i
print("1부터 100까지의 합은", sum, "입니다.")

# 문자열
for i in "string test":
    print(i)

# 팩터리얼 계산 프로그램
n = int(input("정수를 입력하시오: "))
fact = 1

for a in range(1, n+1):
    fact = fact * a
print(n,"!은",fact,"이다.")

# 조건 제어 반복 - while (어떤 조건이 만족되는 동안 반복, 반복의 횟수는 모르지만, 반복 조건을 알고 있는 경우에 사용)
count = 1 # 초기식
sum = 0 # 합을 구하기 위해

while count <= 100: # 조건식
    sum = sum + count
    count = count + 1 # 증감식
print("1부터 100까지의 합은", sum, "입니다")

# 로그인 프로그램
password = ""
while password != "pythonisfun":
    password = input("암호를 입력: ") # 증감식
print("로그인 성공")

# 단을 입력 받아 구구단을 출력
dan = int(input("단을 입력: "))

for i in range(9):
    print("%s x %s = %s"%(dan, (i+1), (i+1)*dan))

# 두 수를 랜덤으로 결정 / 하나는 1~10, 다른 하나는 30~50 / 결정된 두 수 사이의 모든 수를 더하여 합을 출력
import random

num1 = random.randint(1,10)
num2 = random.randint(30,50)
sum1 = 0

for i in range(num1, num2+1):
    sum1 += i
print("%s~%s까지의 총합은 %s"%(num1,num2,sum1))

# 수를 하나 입력받음 / 두 수 사이에 있는 수들 중 입력한 수의 배수에 해당하는 수들을 모두 출력
import random

num1 = random.randint(1,10)
num2 = random.randint(30,50)
sum1 = 0
n = int(input("수 하나 입력: "))

for i in range(num1, num2+1):
    if i % n == 0: # n배수인지 확인
        print("%s "%(i), end="")
    sum1 += i
print()
print("%s~%s까지의 총합은 %s"%(num1,num2,sum1))

# 랜덤으로 수 2개를 결정(10~100) / 두 수 사이에 있는 수들을 화면에 출력 / 단, 두 수가 동일한 수가 나온 경우 그대로 종료
# 한 라인에 5개씩 출력
import random

n1 = random.randint(10,100)
n2 = random.randint(10,100)
cnt = 0

if n1 != n2:
    if n1 > n2: # n1이 더 크면 n1과 n2 값을 교환
        temp = n1
        n1 = n2
        n2 = temp
    for i in range(n1, n2+1):
        print("%4s"%(i), end="") # 공백 4
        cnt += 1
        if cnt % 5 == 0:
            print()
    print()
else:
    print("랜덤 값이 %s로 동일"%(n1))

# 문자열 하나 입력받음 / 입력된 문자열의 길이만큼 반복하면서 문자열이 한 글자씩 추가되는 모습으로 출력
str1 = input("문자열 하나 입력: ")
str_len = len(str1)
i = 1 # 초기식
while i <= str_len:
    print(str1[:i])
    i += 1 # 증감식

# 중첩반복문 / 한줄에 *이 10개씩 총 5줄을 출력
for i in range(5):  # 2 수행
    for j in range(10):  # 1 수행
        print("*", end="")
    print("")

# *을 이용하여 직각삼각형을 출력
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print("")