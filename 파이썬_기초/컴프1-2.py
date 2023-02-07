# 9주차

# 랜덤으로 숫자를 하나 결정 / 문자 하나 입력받음 / 삼각형 문자, 숫자

import random

ch = input("문자 입력: ")
rn = random.randint(5, 10)

for i in range(1, rn+1):
    print("%s"%(i), end=" ")
    print(ch*i)

# 원을 랜덤으로 여러 개를 그리는 프로그램 / 랜덤으로 반지름 결정(20~100) / 랜덤으로 그려질 원의 개수 결정(5~10)
# 원이 그려지는 위치도 랜덤으로 결정(x:-200~200, y:-200~200)

import random, turtle
t = turtle.Turtle()
t.shape("turtle")

cir_num = random.randint(5, 10)

for i in range(cir_num):
    t.up()
    t.goto(random.randint(-200,200), random.randint(-200,200))
    t.down()
    t.circle(random.randint(20,100))

# 육면체 주사위를 던져 눈값을 구하여 더함 / 합이 30을 초과할 때까지 반복 / 몇 번 만에 30을 초과했는지 출력
# 주사위를 던져 나오는 눈값도 합도 출력하도록 함

import random

sum1 = 0
cnt = 0

while sum1 <= 30:
    n = random.randint(1, 6)
    cnt += 1
    sum1 += n
    print("수: %s(합: %s)"%(n,sum1))

print("주사위를 던진 횟수는 총 %s번"%(cnt))

# 주사위 이미지를 이용 / 내가 던진 주사위 눈값과 컴퓨터의 주사위 눈값이 터틀 그래픽 화면에 나오도록 함
# 아무 키나 입력하면 계속 진행하고 0을 입력하면 게임이 종료
# 내가 던진 주사위 눈값이 컴퓨터의 주사위 눈값보다 크면 승리라고 화면 상단에 출력
# 그렇지 않으면 패배라고 화면 상단에 출력 (왼쪽 주사위가 내가 던진 주사위, 오른쪽 주사위가 컴퓨터 주사위로 간주)
# 비긴 경우 무승부 출력

import random,turtle
t= turtle.Turtle()
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

dice = turtle.textinput("", "Enter를 치세요")
while dice != 0:
    t.clear()
    com = random.randint(1, 6)
    me = random.randint(1, 6)

    t.up()
    t.goto(-200,0)

    if me == 1:
        t.shape(dice1)
    elif me == 2:
        t.shape(dice2)
    elif me == 3:
        t.shape(dice3)
    elif me == 4:
        t.shape(dice4)
    elif me == 5:
        t.shape(dice5)
    else:
        t.shape(dice6)
    t.stamp()
    t.ht()
    t.goto(200,0)
    t.st()
    if com == 1:
        t.shape(dice1)
    elif com == 2:
        t.shape(dice2)
    elif com == 3:
        t.shape(dice3)
    elif com == 4:
        t.shape(dice4)
    elif com == 5:
        t.shape(dice5)
    else:
        t.shape(dice6)
    t.stamp()
    t.ht()
    t.goto(0,200)
    if me > com:
        t.write("승리", False, "center", ("",20,"bold"))
    elif com > me:
        t.write("패배", False, "center", ("",20,"bold"))
    else:
        t.write("무승부", False, "center", ("", 20, "bold"))

    dice = turtle.textinput("", "종료하려면 0을 입력: ")

# * 삼각형
for i in range(5):
    for j in range(i+1) :
        print("*", end = "") # '*'을 출력
    print()  # 줄바꿈을 위해 사용되는 print

# * 역삼각형
for i in range(5):
    for j in range(5, i, -1):
        print("*", end="")  # '*'을 출력
    print()  # 줄바꿈을 위해 사용되는 print

# 오른쪽 정렬 * 삼각형
for i in range(5):
    for j in range(4, i, -1):
        print(" ", end="")
    for k in range(i+1):
        print("*", end = "")
    print()

# 오른쪽 정렬 * 역삼각형
for i in range(5):
    for j in range(i):
        print(" ", end="")
    for k in range(5, i, -1):
        print("*", end = "")
    print()

# 1 / 22 / 333 / 4444 / 55555 / 삼각형
for i in range(1,6):
    for j in range(i):
        print(i, end="")
    print()

# 55555 / 4444 / 333 / 22 / 1 / 역삼각형
for i in range(5,0,-1):
    for j in range(i):
        print(i, end="")
    print()

# 공백 오른쪽 정렬 1 / 22 / 333 / 4444 / 55555
for i in range(1,6):
    for j in range(5, i, -1):
        print(" ", end="")
    for k in range(i):
        print(i, end="")
    print()

# 공백 오른쪽 정렬 55555 / 4444 / 333 / 22 / 1
for i in range(5,0,-1):
    for j in range(5, i, -1):
        print(" ", end="")
    for k in range(i):
        print(i, end="")
    print()

# 무한 반복
sign = True  # 초기식

while sign:  # 조건식
    light = input("신호등 색상을 입력하시오: ")
    if light == 'blue':  # 탈출 조건
        sign = False  # 증감식 / break(강제로 반복을 중지할 때, 항상 반복문하고 같이 사용해야함)
print("전진")

# break
for i in range(1,11):
    if i%2 == 0:
        break
    print(i)
print("종료")

# continue
num = 0
for i in range(1,11):
    if i%2 == 0:
        continue  # 바로 조건으로 다시 올라감
        num += 1
    print(i)
print(num)

# 1~100까지의 수들 중 짝수만 출력하는 코드 작성 / continue 반드시 사용
for i in range(1,101): # continue 사용 x
    if i % 2 == 0:
        print(i, end=" ")

for i in range(1,101): # continue 사용
    if i % 2 != 0:
        continue
    print(i, end=" ")

# 구구단을 출력하는 프로그램 / 단을 입력받아 해당 단의 구구단을 출력 / 계속 반복하도록 하고 0을 입력하면 종료
# 출력할 때 구구단 계산 모습이 출력되도록 한다
while True:
    dan = int(input("단 입력(0은 종료): "))
    if dan == 0:
        break
    for i in range(1,10):
        print("%s x %s = %s"%(dan, i, dan*i))

# 앞 문제를 이용 / 입력되는 단을 1~9사이로 제한
while True:
    dan = int(input("단 입력(0은 종료): "))
    if dan == 0:
        break
    elif dan > 9 or dan < 1: # elif not(1 <= dan <= 9):
        continue

    for i in range(1,10):
        print("%s x %s = %s"%(dan, i, dan*i))

# 원의 반지름은 100~250 중 랜덤으로 결정 / 원의 개수는 3,4,5,6 중 하나를 입력받음
# 잘못 입력한 경우 다시 입력받음
import turtle, random
t = turtle.Turtle()

radius = random.randint(100,250)
while True:
    cir_n = int(turtle.textinput("","3,4,5,6 중 하나를 입력: "))
    if 3 <= cir_n <= 6:
        for i in range(cir_n):
            t.circle(radius)
            t.left(360/cir_n)
        break

# 도돌이표 c-d-c-d
print("A-B-", end="")
for i in range(2):
    print("C", end="")
    print("-", end="")
    print("D", end="")
    if i != 1:
        print("-", end="")

# n각형 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")

polyn = int(turtle.textinput("", "몇각형을 원하시나요?"))

for i in range(polyn):
    t.fd(100)
    t.lt(360/polyn)

# 앞 문제 이용 / 한 변의 길이는 랜덤값이 적용되도록 함(50~250) / 다각형 3,4,5,6
# 잘못 입력한 경우 다시 입력받도록 함
import turtle, random
t = turtle.Turtle()
t.shape("turtle")

n = random.randint(50, 250)

while True:
    polyn = int(turtle.textinput("", "몇각형을 원하시나요?"))
    if not(3<=polyn<=6):  # 3~6이 아니라면 계속
        continue
    for i in range(polyn):
        t.fd(100)
        t.lt(360/polyn)
    break

# 랜덤 워크 시뮬레이션 / 반복횟수 랜덤(30~50) / 각도 회전 시 왼쪽으로 회전할 지 오른쪽으로 회전할 지 랜덤으로 결정
import turtle, random
t = turtle.Turtle()
t.shape("turtle")

n = random.randint(30, 50)
print("반복횟수: %s"%(n))
for i in range(n):
    length = random.randint(1, 100)
    t.fd(length)
    angle = random.randint(1,100)
    a = random.randint(0,1)
    if a == 0:
        t.left(angle)
        print("왼쪽")
    else:
        t.right(angle)
        print("오른쪽")

# 10주차

# 범인 맞추기 / 방 번호
import random
score = 0
while True:
    criminal = random.randint(1,3)
    room = int(input("방 번호 입력:"))

    if not(1 <= room <= 3):
        print("해당 방 번호는 없습니다.")
        continue
    if criminal == room:
        print("범인 검거!")
        score += 100
        break
    else:
        print("범인이 없습니다.")
        score -= 10

print("최종 점수: %s"%(score))


# 초기 점수 100 / 한 번 틀릴때마다 10점씩 감점 / 두 번 틀릴때마다 범인 위치는 랜덤
# 범인 검거 or 점수 0이 되면 게임 종료

import random
score = 100
wrong = 0
criminal = random.randint(1,3)

while True:
    room = int(input("방 번호 입력:"))

    if not(1 <= room <= 3):
        print("해당 방 번호는 없습니다.")
        continue
    if criminal == room:
        print("범인 검거!")
        break
    else:
        print("범인이 없습니다.")
        score -= 10
        if score <= 0:
            break
        wrong += 1
        if wrong == 2:
            criminal = random.randint(1,3)
            wrong = 0

print("최종 점수: %s"%(score))

# random 정리
import random
n = random.random() # 0.0 ~ 1.0 사이의 난수 값을 생성
print(n)

# 터틀그래픽 몬드리안 그림 / 다양한 크기와 다양한 위치에서 20개의 사각형 그리기
# 선 굵기는 3 선색과 채우기 색은 동일하게 하며 랜덤으로 결정
# 크기는 10~300 사이 값 중 랜덤으로 결정
# 사각형 위치는 각각 -300~300 사이의 값 중 랜덤으로 결정
import turtle, random
t = turtle.Turtle()
t.speed(0)
t.width(3)
for i in range(20):
    r = random.random()   # 색상 랜덤
    g = random.random()
    b = random.random()
    t.color(r, g, b)

    length = random.randint(10,300)
    x = random.randint(-300,300)
    y= random.randint(-300,300)

    t.up()
    t.goto(x,y)
    t.down()

    t.begin_fill()
    for i in range(4):
        t.fd(length)
        t.lt(90)
    t.end_fill()

# t.speed(속도) : 0(가장 빠름), 10(빠름), 6(보통), 3(느림), 1(가장 느림)

# 랜덤 도형, 랜덤 색깔, 랜덤 위치 그리기
import turtle, random
t = turtle.Turtle()
t.speed(0)
t.width(3)
pnum = random.randint(10,20)
for i in range(20):
    r = random.random()
    g = random.random()
    b = random.random()
    t.color(r, g, b)

    length = random.randint(10,300)
    x = random.randint(-300,300)
    y= random.randint(-300,300)

    t.up()
    t.goto(x,y)
    t.down()

    poly = random.randint(3,12)

    t.begin_fill()
    for i in range(poly):
        t.fd(length)
        t.lt(360/poly)
    t.end_fill()

# 모든 약수 구하기


# 최대공약수 구하기


# 숫자 맞추기 게임
# 1~100 사이의 수 중 랜덤으로 수를 하나 결정 / 사용자로부터 숫자를 하나 입력받음
# 정답을 맞출 때까지 반복 / 입력한 숫자와 랜덤숫자를 비교하여 숫자가 높은지 낮은지 출력
# 정답을 몇 번 만에 맞췄는지 시도 횟수를 출력한다.

import random
answer = random.randint(1,100)
guess = 0
tries = 0
while guess != answer:
    guess = int(input("수 입력:"))
    tries += 1
    if answer < guess:
        print("높음")
    elif answer > guess:
        print("낮음")

if guess == answer:
    print("시도횟수 %s번 만에 정답!!"%(tries))
else:
    print("정답은:", answer)

# 리스트 (여러 개의 데이터를 의미 있게 묶어서 저장하려고)
# 인덱스 : 리스트의 항목의 위치를 알려주는 번호 (인덱스는 0번부터 시작)
slist = ["영어", "수학", "사회", "과학"]
print(slist[0])
print(slist[1])
print(slist[1][0]) # 수
print(slist[1][1]) # 학
print(slist)

# 리스트의 생성과 추가
cart = []
cart.append("사과")
cart.append("세제")
print(cart)

# 슬라이싱
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[0:3])
print(letters[:3])
print(letters[3:])
print(letters[:])   # 항목 전체를 추출
print(letters[0:1])

copy = letters[:]
copy2 = letters
print(copy)
print(copy2)
copy[1] = "B" # 항목 내용 변경, 추가가 아님
print(copy)
print(letters)
print(copy2)
copy2[0] = "A"
print(copy)
print(letters)
print(copy2)

# 리스트 항목의 변경과 추가
cart = ["사과", "세제", "화장지", "치약"]
cart[1] = "섬유 유연제"  # 교체
print(cart)

cart.insert(1,"건전지")  # 주어진 위치에 추가
print(cart)

cart = ["사과", "세제", "화장지", "치약"] # 리스트 삭제
cart.remove("화장지")
print(cart)

if "칫솔" in cart:  # 에러 안남
    cart.remove("칫솔")
print("칫솔")

cart = ["사과", "세제", "화장지", "치약"] # 리스트 삭제
del cart[2]
print(cart)
del(cart[3])


cart = ["사과", "세제", "화장지", "치약"]
item = cart.pop()  # 마지막 원소를 삭제, 삭제하는 요소를 반환
print(cart)
print(item)

car = []
if len(car) != 0:
    item = car.pop()
    print(item)

# 리스트 항목 탐색
cart = ["사과", "세제", "화장지", "치약", "화장지"]
print(cart.index("화장지"))

if "비누" in cart:
    print(cart.index("비누"))

# 리스트 정렬하기
heores = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
heores.sort() # 오름차순 정렬
print(heores)

heores.sort(reverse=True) # 내림차순 정렬
print(heores)


heores = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
new_heroes = sorted(heores) # 정렬 함수
print(heores)
print(new_heroes)

heores = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
new_heroes = sorted(heores, reverse=True) # 정렬해서 저장하되 내림차순으로 정렬 저장
print(heores)
print(new_heroes)

# 리스트와 반복문

for i in[1,2,3]:
    print("i=", i)

# 반복문을 이용해서 리스트 추가하기
heores = []
for i in range(5):
    name = input("영웅들의 이름 입력: ")
    heores.append(name)
for i in heores:
    print(i, end=" ")

# 홀수 프린트
num = [100, 96, 209, 22, 30, 117]
for i in num:
    if i%2 == 1:
        print(i, end=" ")


for i in num
    print(i, end=" ")


for i in range(len(num)):  # len(num) = 6 / range(len(num)) = 5
    print(num[i], end=" ")  # 인덱스로 불러오기


# 11주차
list1 = []
list2 = [1,2,3]
list3 = list()
list4 = list(range(3))  # 시퀀스 / [0,1,2]
list5 = list("string")   # ['s', 't', 'r', 'i', 'n', 'g']
print(list1, list2, list3, list4, list5)


list1 = list(range(3))
list2 = [10,20,30,40]
list1.append(10)
list2.insert(2,50)
print(list1, list2)
list1.extend(list2)  # 리스트 붙이기
print(list1)
list3 = list1 + list2  # 리스트 + 리스트
print(list3)


alist = [1,2,3,4,5,6,7,8]
alist[2:4] = [10,20,30]
print(alist) # [1, 2, 10, 20, 30, 5, 6, 7, 8]
blist = [1,2,3,4,5,6,7,8]
blist[2] = [10,20,30]  # [1, 2, [10, 20, 30], 4, 5, 6, 7, 8]
print(blist)
print(alist[2])  # 10
print(alist[2:3])  # [10]


alist = ["사과", "오렌지", "딸기", "메론", "오렌지"]
print(alist)
if "오렌지" in alist:
    alist.remove("오렌지") # 앞에 것만 제거
print(alist)
del alist[1]
print(alist)
blist = ["사과", "딸기", "오렌지", "메론", "오렌지"]
del blist[1:3]  # blist[1:3] = []
print(blist)
f = blist.pop()
print(f, blist)  # 오렌지 ['사과', '메론']
f2 = blist.pop(0)
print(f2, blist) # 사과 ['메론']
alist.clear()  # del alist[:], alist[:] = [], alist = [] / del alist 안됨
print(alist)


alist = ["사과", "딸기", "오렌지", "메론", "오렌지", "배"]
print(alist)
if "오렌지" in alist:
    print(alist.index("오렌지"))
if "오렌지" in alist:
    print(alist.index("오렌지", 3, 5))  # 범위지정을 해서 찾기


alist = ["사과", "딸기", "오렌지", "메론", "오렌지", "배"]
blist = [19,98,45,28,77,63]
clist = sorted(alist)  # 오름차순 정렬
print(alist)
alist.reverse()  # 정렬x 순서만 역순
print(alist)
print(clist)
dlist = sorted(blist, reverse= True) # 내림차순 정렬
print(blist)
print(dlist)
alist.sort()  # 원본 리스트가 오름차순
blist.sort(reverse= True)  # 내림차순 정렬 원본 리스트 변경
print(alist)
print(blist)
alist.reverse()
print(alist)


alist = ["사과", "딸기", "오렌지", "메론", "오렌지", "배"]
blist = [19,98,45,28,77,63]
print(alist.count("오렌지")) # 리스트 갯수 세기
print(blist.count(45))
print(alist.count("파인애플"))
clist = alist.copy()
print(clist)
dlist = alist
print(dlist)
clist[0] = "바나나"
print(clist)
print(alist)  # 안바뀜
dlist[0] = "아보카도"
print(dlist)
print(alist) # 바뀜 / 대입연산자를 사용하면 원본도 바뀜
print(alist*3)

# 사고자 하는 품목을 8개 이상 입력하여 리스트에 저장 / 키보드로 구매한 품목을 하나 입력받 구매 예정 리스트에 있으면 삭제하고 출력하여 확인
# 해당 품목(입력한 품목)이 없으면 에러메시지를 출력


# 리스트 2차원 구조
nlist = [[10,20,30], [40,50,60]]
print(nlist)
print(nlist[0])
print(nlist[0][0])


import random
alist = [random.randint(1,10) for i in range(5)]
print(alist)
print(random.choice(alist))   # 하나 뽑기
print(random.sample(alist,1))  # 뽑기
print(random.sample(alist,3))
print(random.sample(alist,6))  # 오류


# 해야 할 일을 5개 입력받음 / 입력한 할 일을 리스트에 저장
# 할 일 리스트를 한 번 섞어줌 / 할 일 리스트 중 항목 하나를 랜덤으로 추출하여 출력
# 할 일 리스트 중 항목 2개를 랜덤으로 추출하여 출력
import random
dolist = []
for i in range(5):
    do = input("해야 할 일 입력(%s): "%(i+1))
    dolist.append(do)

random.shuffle(dolist)   # 리스트 섞기
print(dolist)
print("해야 할 일 하나 선택: ", end="")
print(random.choice(dolist))
print("해야 할 일 2개 선택: ", end="")
print(random.sample(dolist,2))
#for i in range(2):       윗 문장 대신 이걸 쓰면 중복이 출력됨
#    print(random.choice(dolist), end= "")


# 다음 명언들으르 리스트에 저장한다. / 프로그램을 실행할 때 마다 오늘의 명언이 랜덤으로 출력되도록 한다.
# "꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다."
# "분노는 바보들의 가슴속에서만 살아간다."
# "고생 없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다."
# "사람은 사랑할 때 누구나 시인이 된다."
# "시작이 반이다."
import random
quotes = []
quotes.append("꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.")
quotes.append("분노는 바보들의 가슴속에서만 살아간다.")
quotes.append("고생 없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.")
quotes.append("사람은 사랑할 때 누구나 시인이 된다.")
quotes.append("시작이 반이다.")

dailyQuotes = random.choice(quotes)
print("#"*28)
print("#      오늘의 명언")
print("#"*28)
print()
print(dailyQuotes)


# 스파이럴 그리기
import turtle
t = turtle.Turtle()
t.speed(0)
t.width(3)
length = 10
colors = ["red", "purple", "blue", "green", "yellow", "orange"]

while length < 500:
    t.fd(length)
    t.color(colors[length%6])  # 나머지가 0,1,2,3,4,5 중에 나옴 / 나머지 연산자
    t.right(89)
    length += 5


# 오륜기 그리기
import turtle
t = turtle.Turtle()
positions = [[0,0,"green"], [-120,0,"yellow"], [60,60,"red"], [-60,60,"black"], [-180,60,"blue"]]
t.pensize(5)

for p in positions:
    x = p[0]
    y = p[1]
    c = p[2]
    t.up()
    t.goto(x,y)
    t.pendown()
    t.color(c,c)
    t.circle(60)
# 방법 2
for x,y,c in positions:
    t.up()
    t.goto(x,y)
    t.pendown()
    t.color(c,c)
    t.circle(60)


# 습도 구하기
temp_list = [0,10,20,30]
vapor_list = [4.8,9.4,17.3,30.4]

vapor = float(input("현재 수중기량 입력: "))
temp = int(input("현재 온도 입력: "))

if temp in temp_list:
    humidity = (vapor/vapor_list[temp_list.index(temp)]) * 100
    print("현재 습도는",humidity,"% 입니다. ")


# 함수
def print_address():
    print("서울특별시 종로구 1번지")
    print("파이썬 빌딩 7층")
    print("홍길동")

print_address()


# 12주차
# 가위, 바위, 보 프로그램 / 컴퓨터는 랜덤으로 가위, 바위, 보 중 하나 / 게이머는 가위, 바위, 보 중 하나를 키보드로 입력
# 잘못 입력한 경우 올바른 값이 입력될 때까지 반복 / 랜덤으로 결정된 컴퓨터 값과 입력한 값을 비교하여 결과에 맞춰서
# 비김, 이김, 짐 출력
import random

srp = ["가위", "바위", "보"]
random.shuffle(srp) # 그냥 섞어줌

while True:
    my_srp = input("가위, 바위, 보 중 하나를 입력하세요: ")
    if my_srp in srp: # if my_srt == "가위" or my_srp == "바위"....
        break
    else:
        print("잘못 입력하였습니다. 다시 입력해주세요")

com_srp = random.choice(srp)
if my_srp == com_srp:
    print("비겼습니다.")
elif (my_srp == "가위" and com_srp == "보") or (my_srp == "바위" and com_srp == "가위") or (my_srp == "보" and com_srp == "바위"):
    print("컴:", com_srp)
    print("당신이 이겼습니다.")
else:
    print("컴:", com_srp)
    print("당신이 졌습니다.")

# 앞 문제 코드를 활용 / 가위, 바위, 보에서 비겼을 때 다시 가위, 바위, 보를 하도록 함
# 승부가 날 때까지 진행
import random

srp = ["가위", "바위", "보"]
random.shuffle(srp) # 그냥 섞어줌
my_srp = com_srp = "가위"  # 초기식
while my_srp == com_srp:
    while True:
        my_srp = input("가위, 바위, 보 중 하나를 입력하세요: ")
        if my_srp in srp: # if my_srt == "가위" or my_srp == "바위"....
            break
        else:
            print("잘못 입력하였습니다. 다시 입력해주세요")

    com_srp = random.choice(srp)
    if my_srp == com_srp:
        print("비겼습니다.")
    elif (my_srp == "가위" and com_srp == "보") or (my_srp == "바위" and com_srp == "가위") or (my_srp == "보" and com_srp == "바위"):
        print("컴:", com_srp)
        print("당신이 이겼습니다.")
    else:
        print("컴:", com_srp)
        print("당신이 졌습니다.")

# 2개의 주사위에서 같은 숫자 나오기 게임을 만듦 / 주사위는 2개 던질 것이고 2개의 주사위 눈 값이 동일한
# 값이 나오면 성공, 그렇지 않으면 동일한 눈 값이 나올때까지 진행
# 서로 다른 눈 값이 나왔을 때 다시 합니다.라고 입력창을 열어주고 확인을 누르면 다시 주사위를 던지게 됨
# 동일한 눈 값이 나왔을 때 몇 번 만에 성공했는지 출력
# 터틀 그래픽에서 입력받도록 하고 주사위 이미지를 이용하여 작성

import random, turtle
scr = turtle.Screen()
t = turtle.Turtle()
dice = []  # 주사위 사진 넣기
for i in range(6):
    dice.append("dice"+str(i+1)+".gif")
    scr.addshape(dice[i])

cnt = 1

while True:
    f_dice = random.randint(1,6)
    s_dice = random.randint(1,6)
    t.up()
    t.goto(-100,0)
    t.shape(dice[f_dice-1])  # -1 해줘야 함
    t.stamp()

    t.goto(100,0)
    t.shape(dice[s_dice-1])
    t.stamp()
    t.ht()

    if f_dice == s_dice:
        t.goto(0,250)
        t.write("%s번 만에 성공"%(cnt),False, "center", ("", 25, "bold"))
        break
    else:
        cnt += 1
        turtle.textinput("", "다시 합니다.")

# 함수
def get_sum(start, end):
    sum1 = 0
    for i in range(start, end+1):
        sum1 += i
    print("sum=", sum1)

get_sum(1,10)
get_sum(1,20)

# 함수의 값 반환하기
def calculate_area(radius):
    area = 3.14*radius**2
    return area

c_area = calculate_area(5.0)
print(c_area)


# 매개변수, 반환 모두 없음
def print_TF1():
    num = int(input("값 입력: ")) # 1
    if num == 0:  # 2
        print("거짓")
    else:
        print("참")
print_TF1() # 3

# 매개변수 있고, 반환 없음
def print_TF2(n): # 3
    if n == 0:
        print("거짓")
    else:
        print("참")

num = int(input("값 입력: "))  # 1
print_TF2(num) # 2

# 매개변수 없고, 반환 있음
def print_TF3():
    num = int(input("값 입력: "))  # 1
    return num  # 2

n = print_TF3()  # 3
if n == 0:  # 4
    print("거짓")
else:
    print("참")

# 매개변수 있고, 반환 있음
def print_TF4(n):  # 3
    if n == 0:
        return "거짓"
    else:
        return "참"

num = int(input("값 입력: "))  # 1
print(print_TF4(num))   # 2


# 1~100 중 20개의 값을 랜덤으로 저장하는 함수를 만든다. 저장할 때는 리스트에 저장하도록 한다.
# 리스트에 있는 내용을 출력하는 함수를 만든다. 한 라인에 10개씩 출력되도록 해야 하며, 4자리 확보하여 출력하는 것으로 한다.
# 리스트에 저장된 내용들의 합과 평균을 출력하는 함수를 만든다. 평균은 소수점 2째자리까지 출력되는 것으로 한다.
import random
num_list = []

def random_save(num, minn, maxn):
    for i in range(num):
        num_list.append(random.randint(minn,maxn))

def list_print(nlist):
    for i in range(len(nlist)):
        print("%4s"%(nlist[i]), end="") # 4자리 확보해서 출력
        if (i+1) % 10 == 0: # 한 라인에 10개씩
            print()

def sum_and_avg(nlist):
    nsum = 0
    for i in range(len(nlist)):
        nsum += nlist[i]
    avg = nsum/len(nlist)
    return nsum, avg

num_list = []
random_save(20,1,100)

list_print(num_list)
nsum, avg = sum_and_avg(num_list)
print("합: %s, 평균: %.2f"%(nsum, avg))


# 지역변수 전역변수
result = 0
def calculate_area():
    global result  # 전역변수
    result = 3.14 * r **2

r = float(input("원의 반지름 입력: "))
calculate_area()
print(result)


# 디폴트 인수
def greet(name, msg="잘 지내죠?"):
    print("안녕 ",name+", "+msg)

greet("영희")


# 키워드 인수
def calc(x,y):
    return x-y

print(calc(x=10,y=20))  ## 위치 키워드 키워드 가능 / 키워드 위치 위치, 위치 키워드 위치 불가능
print(calc(y=20,x=20))


# 전역변수 정리
# - 함수 안에서 생성되는 변수 : 지역변수
# - 함수 밖에서 생성되는 변수 : 전역변수

import random
def func1():
    print("in: %s"%(num)) # 전역변수

def func2(num):  # num이라는 지역변수(매개변수)에 값을 전달
    print("in: %s"%(num)) # 지역변수

def func3(num):  # 전역변수 값을 인수로 전달
    num += 10 # 지역변수 값 변경
    print("in: %s"%(num))

def func4():
    global num # 전역변수로 사용
    num += 10 # 전역변수이므로 전역변수 값 변경
    print("in: %s"%(num))

def func5():
    num = random.randint(1,6) # global 사용 안할 시 지역변수
    print("in: %s"%(num))

num = 100 # 전역변수
func1()
print("out: %s"%(num))
func2(num)
print("out: %s"%(num))
func3(num)
print("out: %s"%(num))
func4()
print("out: %s"%(num))
func5()
print("out: %s"%(num))


# 13주차
def func1(p1, p2, p3):
    print("func1 => p1: %s, p2: %s, p3: %s"%(p1,p2,p3))

def func2(p1, p2=10, p3=10):
    print("func2 => p1: %s, p2: %s, p3: %s"%(p1,p2,p3))

def func3(p1=10, p2=10, p3=10):
    print("func3 => p1: %s, p2: %s, p3: %s"%(p1,p2,p3))

def func4(p1=10, p2): # 안 됨. 디폴트 인수 뒤에 위치인수가 오면 안 됨
    print("func4 => p1: %s, p2: %s"%(p1,p2))

func1(10,10,10)
func2(20)
func2(20,20)
func2(20,20,20)
func3()
func3(30)
func3(30,30)
func3(30,30,30)
func4(40,40) # 안 됨


# 랜덤으로 삼각형, 사각형, 오각형, 육각형, 원이 그려지도록 한다.
# 그려지는 시작 위치는 랜덤으로 결정한다(-200~200 사이로 제한)
# 각 다각형의 크기도 랜덤으로 결정한다(50~100 사이로 제한)
# 그려지는 개수는 키보드로 입력받아야 하며 최소 10개, 최대 20개로 제한한다.
# 잘못 입력한 경우 올바른 값이 입렬될 때까지 반복해서 입력받아야 한다.
# 각 내용들을 함수로 만들어 사용한다.
# 각 도형은 역삼각형 등으로 표현해도 된다.

import random,turtle
t = turtle.Turtle()
t.shape("turtle")

def poly_num():
    msg = ""
    while True:
        num = int(turtle.textinput("",msg+"다각형 개수를 입력하세요.: "))
        if 10 <= num <= 20:
            break
        else:
            msg = "10~20 사이의 수를 입력하세요.\n"
    return num # 다각형 개수 반환

def poly_size():
    size = random.randint(50,100)
    return size # 다각형 크기(한 변의 길이 또는 반지름) 반환

def random_position():
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    t.up()
    t.goto(x,y)
    t.down()

def draw_polygon(size):
    p = [3,4,5,6,9]
    s = random.choice(p)
    if s == 9:
        t.circle(size)
    else:
        t.circle(size, steps= s) # extent는 생략

for i in range(poly_num()) : # 다각형 개수 입력받고 개수 반환
    s = poly_size() # 랜덤으로 다각형 크기 결정하여 반환
    random_position() # 랜덤으로 위치 설정
    draw_polygon(s)  # s크기의 다각형을 그려줌(다각형 모양은 랜덤)


# 사용자로부터 키와 몸무게를 입력받는다. / bmi를 구하여 bmi값이 18.5 미만이면 저체중
# 18.5~22.9 사이면 정상, 23~24.9 사이면 과체중, 25~29.9사이면 경도비만, 30 이상이면 고도비만이라고 출력
def getvalue():
    weight = float(input("몸무게 입력(kg): "))
    height = float(input("키 입력(m): "))
    return weight, height

def bmifunc(weight, height):
    bmi = weight/(height*height)
    return bmi

def result_print(bmi):
    if bmi < 18.5:
        print("저체중입니다.")
    elif 18.5 <= bmi <= 22.9:
        print("정상입니다.")
    elif 23.0 <= bmi <= 24.9:
        print("과체중입니다.")
    elif 25.0 <= bmi <= 29.9:
        print("경도비만입니다.")
    elif 30.0 <= bmi:
        print("고도비만입니다.")

w, h = getvalue()
result_print(bmifunc(w,h))


# 사용자로부터 한화 금액과 환전 국가를 입력받고 해당 국가의 환전금액을 출력하려 한다.
# 입력한 국가가 리스트에 없을 때는 다시 입력받도록 한다.
# 국가 리스트는["미국","중국","유럽","일본"]이며, 금액 단위는["달려","위안","유로","엔"]이다
# 국가별 환율 리스트는[1182.5,169.22,1286.74,1078.14]이다.
# 환전을 구하는 공식은 다음과 같다
# 환전금액 = 한국돈/매매기준율
# 환전금액을 출력할 때는 소수점 둘째자리까지 출력하도록한다.

country_list = ["미국","중국","유럽","일본"]
unit_list = ["달려","위안","유로","엔"]
rate = [1182.5,169.22,1286.74,1078.14]

def inputinfo():
    money = int(input("환전 금액(원)을 입력: "))
    while True:
        c = input("국가 입력: ")
        if c not in country_list:
            print("해당 국가가 없습니다. 다시 입력하세요.")
        else:
            break
    return c, money

def exchange(c, m):
    indx = country_list.index(c)
    result = round(m/rate[indx], 2)
    print("%s원은 %s %s"%(m, result, unit_list[indx]))

country, money = inputinfo()
exchange(country,money)


# 마우스 화면 클릭 사각형 그리기
import turtle
t = turtle.Turtle()
s = turtle.Screen()

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("green")
    square(50)
    t.end_fill()

##main part##
s.onscreenclick(drawit)


# 한붓그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")
s = turtle.Screen()

def draw(x,y):
    t.goto(x,y)

##main part##
t.pensize(10)
s.onscreenclick(draw)
s.onkey(t.up, "u")
s.onkey(t.down, "d")
s.listen()  # 필수


# 이차함수 그래프 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")

def f(x):
    return x**2 + 1

t.goto(200,0)
t.goto(0,0)
t.goto(0,200)
t.goto(0,0)

for x in range(150):
    t.goto(x, int(0.01*f(x)))


# 테세우스 터틀 미로 탈출 게임
import turtle

def draw_maze(x,y):
    for i in range(2):
        t.penup()
        if i == 1:
            t.goto(x+100, y+100)
        else:
            t.goto(x,y)
        t.pd()
        t.fd(300)
        t.rt(90)
        t.fd(300)
        t.lt(90)
        t.fd(300)

def turn_left():
    t.left(10)
    t.forward(10)

def turn_right():
    t.right(10)
    t.fd(10)

t = turtle.Turtle()
scr = turtle.Screen()
t.shape("turtle")
t.speed(0)

draw_maze(-300,200)
scr.onkey(turn_left, "Left")
scr.onkey(turn_right, "Right")

t.pu()
t.goto(-300,250)
t.pd()
scr.listen()  # 키보드 입력 때 꼭 써야함
scr.mainloop()


# l을 누르면 선분의 길이를 입력받는다.(초기값은 10, 10~100사이)
# s를 누르면 펜의 굵기를 입력받는다.(초기값은 1, 1~10사이)
# a를 누르면 각도를 입력받는다. (초기값은 0, 0~360)
# 방향키를 이용하여 선을 그린다.(Up, Down: 앞 뒤로 진행)
# 마우스를 이용하면 선의 위치를 변경할 수 있다.(위치 변깅 시 선이 그려지면 안됨)

import turtle
t = turtle.Turtle()
t.shape("turtle")
s = turtle.Screen()  # 스크린 객체 생성

def input_line():
    global length
    msg = ""
    while True:
        length = int(turtle.textinput("", msg+"선분의 길이를 입력하세요."))
        if length >= 10 and length <= 100:
            break
        else:
            msg = "10~100 사이 값을 입력하세요.\n"

def input_ps():
    msg = ""
    while True:
        ps = int(turtle.textinput("", msg+"선 굵기를 입력하세요."))
        if 1 <= ps <= 10:
            break
        else:
            msg: "10~100 사이 값을 입력하세요.\n"
    t.width(ps)

def input_angle():
    msg = ""
    while True:
        ag = int(turtle.textinput("", msg+"각도를 입력하세요."))
        if -360 <= ps <= 360:
            break
        else:
            msg = "-360~360 사이 값을 입력하세요.\n"
    t.left(ag)

def forward_turtle():
    t.forward(length)

def backward_turtle():
    t.backward(length)

def pos_move(x,y):
    t.up()
    t.goto(x,y)
    t.down()


## main part ##
ag = 0 # 각도
ps = 1
length = 10
s.onkey(input_line, 'l')
s.onkey(input_ps, 's')
s.onkey(input_angle, 'a')
s.onkey(forward_turtle, 'Up')
s.onkey(backward_turtle, 'Down')
s.onscreenclick(pos_move)
s.listen()


# 재귀호출
def rec_num(n):
    if n > 0:
        print("%3s"%(n), end="")
        rec_num(n-1)

## main part ##
rec_num(10)


# 14주차

# 딕셔너리
phone_book = {}
print(phone_book)
phone_book["홍길동"] = "010-1234-5678"
print(phone_book)


dict1 = {"Name" : "홍길동", "나이" : 7, "클래스" : "초급", "클래스" : "일반"}  # 키값 중복 안됨!!
print(dict1["Name"])  # 키값으로 찾으면 결과는 벨류값이 나온다.
print(dict1.keys())  # 키값
print(dict1.values())  # 벨류값


phone_book = {"홍길동" : "010-1234-5678",
              "강감찬" : "010-1111-2222",
              "이순신" : "010-4131-9676"}
print(phone_book.keys())

for key in sorted(phone_book.keys()): # 정렬
    print(key,phone_book[key])


phone_book["홍길동"] = "010-3232-4324"  # 추가 / 키값이 있으면 수정
del phone_book["홍길동"]  # 키와 벨류 삭제
print(phone_book.pop("이순신"))  # 해당 키 삭제 + 해당 벨류 반환
phone_book.clear()  # 모든 항목 삭제


# 영단어 입력
eng_dict = {}
eng_dict["one"] = "하나"
eng_dict["two"] = "둘"
eng_dict["three"] = "셋"

word = input("영단어를 입력: ")
if word in eng_dict:
    print(eng_dict[word])
else:
    print("해당 단어는 없습니다.")


eng_dict = dict()  # 공백 딕셔너리를 만듬

# 편의점 재고 관리 프로그램
items = {"커피" : 7, "펜" : 3, "종이컵" : 10, "우유" : 5, "콜라" : 4, "라면" : 11}
print("판매 전 재고:", items)

sell = input("판매한 물건을 입력하세요.: ")

if sell in items:
    items[sell] -= 1  # [sell]은 key / 리스트 아님
else:
    print("판매 제품이 아닙니다.")
print("판매 후 재고:", items)


# 딕셔너리와 반복문의 궁합
phone_book = {"홍길동" : "010-1234-5678",
              "강감찬" : "010-1111-2222",
              "이순신" : "010-4131-9676"}

for i in phone_book.keys():
    print(i)

for i in phone_book.values():
    print(i)

for k,v in phone_book.items(): # 키, 벨류 반
    print("{}의 전화번호는 {}입니다.".format(k,v))


# 집합 (중복된 데이터를 가질 수 없으며 순서가 없음)
s = set()  # 공집합 / s = {} (x)
print(s)
s.add(10)
s.add(3)
s.add(1)
s.add(5)
print(s)
s.discard(1)  # 원소 삭제
print(s)
s.remove(3) # 원소 삭제 / 원소가 없으면 에러가 남 / if문과 같이 사용하면 좋음
print(s)
s.clear()  # 모든 원소를 삭제
print(s)

# 중복제거
math = [10,9,9,8,6,10,6,7,5,8]
print("학생 전체 점수:", math)
math_set = set(math)
print(math_set)
math_set = list(math_set)
print("학생들이 받은 점수:", math_set)


# key로 번호, value로 혈액형을 갖는 혈액형 정보 딕셔너리를 만든다
# 번호의 형태는 emp로 시작하는 문자열로 emp1, emp2,..로 저장된다.
# 혈액형은 A,B,O,AB 중 하나이다.
# key의 개수는 랜덤으로 결정하도록 한다.(30~50)
# 혈액형도 랜덤으로 결정되도록 한다.
# 딕셔너리를 만든 후 키보드로 혈액형을 입력받고 입력한 혈액형의 개수가 총 몇 개인지 출력한다.(혈액형을 잘못 입력하면 다시 입력)
import random
blood = ["A", "B", "O", "AB"]


def make_blood_info(empb, empn):
    for i in range(empn):
        empb["emp" + str(i + 1)] = random.choice(blood)  # key와 value 쌍 추가

def blood_count(empb):
    b_list = list(empb.values())  # count 함수를 사용하려면 list로 변환해야 함
    print(b_list)
    while True:
        b = input("찾을 혈액형을 입력하세요.: ")
        if b in blood:
            break
        else:
            print("올바른 혈액형이 아닙니다. 다시 입력하세요.")
    print("%s 혈액형을 가진 사람 수는 총 %s명" % (b, b_list.count(b)))  # list로 변환했기 때문에 count 함수 사용 가능

emp_blood = {}  # 혈액형 정보 딕셔너리
emp_num = random.randint(30, 50)
make_blood_info(emp_blood, emp_num)  # 딕셔너리 생성 함수
print(emp_blood)  # 생성된 딕셔너리 확인
blood_count(emp_blood)  # 혈액형 입력받고 해당 혈액형 개수 출력함수


# 합집합, 교집합, 차집합
alist = [1, 1, 2, 2, 3, 3, 4, 4]
alist = set(alist)
print(alist)
blist = {3,4,5,6}

print(alist | blist)
print(alist & blist)
print(alist - blist)


# 가위, 바위, 보 게임
import random

def match(c,m):
    if c == m:
        return "비겼습니다."
    elif match_table[c] == m:
        return "졌습니다."
    else:
        return "이겼습니다."

rps_dic = {1:"가위", 2:"바위", 3:"보"}
match_table = {"가위":"보", "바위":"가위", "보":"바위"}

computer = rps_dic[random.randint(1,3)]
mine = input("가위,바위,보 입력: ")
result = match(computer, mine)
print(result)


# 행성까지의 여행 시간
planet_dict = {"수성": 91700000, "금성": 41400000, "화성": 78400000,
               "목성": 628700000, "토성": 1277400000, "천왕성": 275400000,
               "해왕성": 4347400000}
planet = input("행성 이름: ")
speed = int(input("이동 속도(km/h): "))
distance = planet_dict[planet]

time = distance/speed

year = int(time)//(365*24)
month = int(time - (year*365*24)) // (30*24)
day = int(time - (year*365*24) - (month*30*24)) // 24
hour = int(time - (year*365*24) - (month*30*24) - (day*24))

print("이동시간: 약", time, "시간")
print("이동시간: 약", year, "년", month, "월", day, "일", hour, "시간")


# 멘델의 유전 법칙
import random
descendant = []

def make_descendant():
    h1 = random.randint(0,2)
    h2 = random.randint(0,2)
    if h1 == 0 and h2 == 0:
        h = "RR"
    elif h1 == 0 and h2 == 1:
        h = "Rr"
    elif h1 == 1 and h2 == 0:
        h = "rR"
    else:
        h = "rr"
    descendant.append(h)

def count_descendant(d):
    d_dict = {}
    for n in d:
        if n in d_dict:
            d_dict[n] += 1
        else:
            d_dict[n] = 1
    print(d_dict)
    cal_rate(d_dict)

def cal_rate(d):
    rate = (d["RR"] + d["Rr"] + d["rR"]) /d["rr"]
    print(rate, ":1")

for n in range(100):
    make_descendant()

count_descendant(descendant)


# 튜링상 수상자 데이터 분석
awards = []
awards.append({"이름":"팀 버너스리", "수상년도":2016, "국적":"영국", "대표업적":"월드 와이드 웹의 하이퍼텍스트 시스템을 고안하여 개발"})
awards.append({"이름":"리처드 해밍", "수상년도":1968, "국적":"미국", "대표업적":"오류 검출 부호 및 오류 정정 부호"})

for award in awards:
    print(award)

print("====수상자 명단====")
for award in awards:
    print(award["이름"])

print()
print("===수상자 명단과 수상년도===")
for award in awards:
    if award["수상년도"] <= 1990:
        print(award["이름"], award["수상년도"])

print()
print("===수상자 국가===")
nationlity = set()
for award in awards:
    nationlity.add(award["국적"])

print(nationlity)


# 어느 학급의 학생 수는 34명이고, 국어, 영어, 수학 시험을 봤다
# 학생들의 아이디는 stud1, stud2,.. stud34로 되어있다.
# 각 과목별 점수는 0~100 사이의 랜덤값으로 저장한다.
# 이를 딕셔너리로 만들어보시오.
# 영어 점수 중 최고점을 구해서 출력하시오.
# 평균이 가장 높은 학생의 아이디와 평균값(정수)을 구하여 출력하시오.
import random
classdic = {}

for i in range(34):
    classdic["stud"+str(i+1)] = [random.randint(0,100) for i in range(3)]
print(classdic)

jlist = list(classdic.values())
print(jlist)
ejumsu = []
for i in classdic.values(): # jlist:
    ejumsu.append(i[1])
print(ejumsu)
print("영어 점수 최고점: %s"%(max(ejumsu)))

avglist=[]
for k,e,m in classdic.values():
    avg = (k+e+m)//3
    avglist.append(avg)
print(avglist)

for i, j in classdic.items():
    sum1 = 0
    for k in j:
        sum1 += k
    if sum1//3 == max(avglist):
        print("아이디:", i, "평균:", sum1//3)


# 한 판매회사에서 판매실적 점수와 고객 평가 점수를 통해 우수 제품을 선발하려 한다.
# {"세제","비누","락스","칫솔","샴푸","치약","린스","로션"}
# 판매실적 점수가 4점 이상인 제품은 {"비누","칫솔","샴푸","치약","로션"}이고,
# 고객 평가 점수가 4점이 이상인 제품은 {"샴푸","린스","치약"}이다.
# 판매 실적 점수와 고객 평가 점수가 모두 4점 이상인 제품은 우수제품이 되며, 두 점수 모두 4점 미만인 제품은 판매 중지 목록에 들어간다.
# 우수제품과 판매 중지 제품을 출력하시오.

product = {"세제","비누","락스","칫솔","샴푸","치약","린스","로션"}
sale = {"비누","칫솔","샴푸","치약","로션"}
customer = {"샴푸","린스","치약"}

# 우수제품
eprod = sale & customer

# 판매중지 제품
ssale = product - (sale | customer)

print("우수제품: ", eprod)
print("판매중지 제품: ", ssale)