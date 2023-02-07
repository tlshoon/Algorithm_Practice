# 숫자형
print(5)
print(3+5)

# 문자형
print("hello world")
print("hello world" * 9)

# 참거짓
print(5>10)
print(5<10)
print(not (5>10))

# 변수
animal = '고양이'
name = '해피'
age = 4
hobby = '산책'
is_adult = age >= 3

print("우리집 "+ animal +"의 이름은 "+ name +"에요")
print(""+ name +"는 "+ str(age)+ "살이며, "+ hobby +"을 좋아해요")
print(""+ name +"는 어른일까요? "+ str(is_adult) +"")

# 주석
'''이렇게 하면 
여러문장
한번에 주석처리, 커맨드 + / '''
# print("우리집 "+ animal +"의 이름은 "+ name +"에요")
# print(""+ name +"는 "+ str(age)+ "살이며, "+ hobby +"을 좋아해요")
# print(""+ name +"는 어른일까요? "+ str(is_adult) +"")

# quiz 1

station_1 = "사당"
station_2 = "신도림"
station_3 = "인청공항"

print(""+ station_3 +"행 열차가 들어오고 있습니다" )
print(station_1 + "행 열차가 들어오고 있습니다")

# 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)
print(5%3) # 나머지 구하기
print(5//3) # 몫 구하기

print(10>3)
print(10<3)
print(3 == 3)

print(1 != 3)
print(not (1 != 3))
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))
print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))

# 간단한 수식
print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 5 #나머지
print(number)

# 숫자 처리 함수
print(abs(-5)) #절대값
print(pow(4, 2)) #제곱
print(max(5, 12))
print(min(5, 12))
print(round(3.14)) #반올림
print(round(4.99))

from  math import *
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근

# 랜덤 함수
from  random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의  임의의 값 생성

# quiz 2
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 "+ str(date) +"일로 선정 되었습니다")

# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"
print("성 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리(뒤에부터) : " + jumin[-7:])

# 문자열 처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Python"))
print(python.index("Amazing"))

# 문자열 포맷
print("a" + "b")
print("a", "b")

print("나는 %d살입니다." % 20) # 방법 1
print("나는 %s을 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요" % "A")
print("나는 %s살입니다." % 20) # %s
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨강"))

print("나는 {}살입니다.".format(20)) # 방법 2
print("나는 {}색과 {}을 좋아해요".format("파란", "빨강"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨강"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨강"))

print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨강")) # 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(color = "빨강", age = 20))

age = 20 # 방법 4
color = "빨강"
print(f"나는 {age}살이며, {color}색을 좋아해요")

# 탈출문자
# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")
# \"\' : 문장 내에서 따움
# 저는 "나도코딩"입니다.
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")
# \\ : 문장 내에서 \
# \r : 커서를 맨앞으로 이동
print("Red Apple\rPine")
# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")
# \t : 탭
print("Red\tApple")

# quiz 3

url = "http://naver.com"
my_str = url.replace("http://", "")
print(my_str) # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
# my_str[0:5] > 0~5 직전까지
print(my_str)
passward = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(url, passward))

# 리스트
# 지하철 칸별로 10명 20명 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호는 몇 번째 칸에 타고 있는가
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈을 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기도 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]

# 리스트 확장
num_list.extend((mix_list))
print(num_list)

# 사전
cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet)
print(cabinet[3])

print(cabinet.get(100))
print(cabinet.get(5))
print(cabinet.get(5, "사용가능"))

print(3 in cabinet)  # True
print(10 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

cabinet["C-20"] = "조세호"   # 새 손님
cabinet["A-20"] = "김종국"
print(cabinet)

del cabinet["A-20"]   # 간 손님
print(cabinet)

print(cabinet.keys())   # key만 출력

print(cabinet.values())  # value들만 출력

print(cabinet.items())   # key, value 쌍으로 출력

cabinet.clear()   # 목욕탕 폐점
print(cabinet)

# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "coding"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "coding")
print(name, age, hobby)

# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(java & python)  #교집합 (java와 python을 모두 할 수 있는 개발자)
print(java.intersection(python))

print(java | python)  #합집합 (java를 할 수 있거나 python을 할 수 있는 개발자)
print(java.union(python))

print(java - python)   # 차집합 (java를 할 수 있지만 python은 할 수 없는 개발자)
print(java.difference(python))

python.add("김태호")  # python을 할 수 있는 개발자가 늘어남
print(python)

java.remove("김태호") # java를 까먹음
print(java)

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu,type(menu))

# quiz 4
from  random import *
users = range(1,21)  # 1부터 20까지 숫자를 생성
print(type(users))

users = list(users)
print(type(users))

shuffle(users)
winners  = sample(users, 4)   # 4명중 1명은 치킨, 3명은 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

# if
weather = "비"
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요없어요")

'''weather = input("오늘 날씨 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요없어요")'''

'''temp = int(input("기온은 어때요? "))
if 30 <= temp :
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp < 30 :
    print("괜찮은 날씨에요")
elif 0 <= temp < 10 :
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")'''

# for
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5):  # 0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# while
customer = "토르"
index = 5
while index >= 1 :
    print("{0}, 커피가 준비되었습니다. {1}번 남았습니다".format(customer, index))
    index -= 1
    if index == 0 :
        print("커피는 폐기처분되었습니다")

'''customer = "아이언맨"   # 무한루
index = 1
while True :
    print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
    index += 1'''

'''customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")'''

# continue와 break
absent = [2, 5]
no_book = [7]
for student in range (1, 11):
    if student in absent:
        continue
    if student in no_book:
        print("오늘 수업 여기까지. {0} 교무실로 따라와".format(student))
        break
    print("{0}, 책 읽어봐".format(student))

# 한 줄 for
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# quiz 5
from  random import *
cnt = 0  # 총 탑승 승객
for i in range (1, 51):  # 1 ~ 50이라는 수 (승객)
    time = randrange(5, 51)  # 5 ~ 50분 소요시간
    if 5 <= time <= 15 : # 5분 ~ 15분 이내의 손님 (매칭 성공), 탑승 승객 수 증가 
        print("[O] {0}번째 손님 (소요 시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
        print("[ ] {0}번쨰 손님 (소요 시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))

# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account()

# 전달값과 반환값
def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):  # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료 되었습니다. 잔액은 {0}원입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다".format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다".format(commission, balance))

# 기본값
def profile(name, age, main_lang):
    print("이름 : {0}, 나이 : {1}, 언어 : {2}".format(name, age, main_lang))

profile("유재석", 25, "파이썬")
profile("김태호", 26, "자바")

def profile(name, age = 17, main_lang = "파이썬"):  # 같은 학년, 반, 수업
    print("이름 : {0}, 나이 : {1}, 언어 : {2}".format(name, age, main_lang))
profile("유재석")
profile("김태호")

# 키워드값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang= "파이썬", age = 20)
profile(main_lang = "자바", age = 21, name = "김태호")

# 가변인자
'''def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}, 나이 : {1}".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)'''

def profile(name, age, *language):
    print("이름 : {0}, 나이 : {1}".format(name, age), end=" ")
    for lang in  language:
        print(lang, end="")
    print()

profile("유재석", 25, "python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 20, "Kotlin", "Swift")

# 지역변수와 전역변수
gun = 10
def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soliders):
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2) # 2명이 경계근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

# quiz 6
def std_weight(height, gender): # 키 m 단위 (실수), 성별 남자 / 여
    if gender == "남자":
        return  height * height * 22
    else:
        return  height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}Kg입니다.".format(height, gender, weight))

# 표준입출력
print("Python", "Java", sep=",", end = "?")
print("무엇이 더 재밌을까요?")

'''import sys
print("Python", "Java", file=sys.stdout) # 표준출력
print("Python", "Java", file=sys.stderr) # 표준에'''

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subjects, score in scores.items():
    print(subjects.ljust(8), str(score).rjust(4), sep= ":")
    #print(subjects, score)

for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))

'''answer = input("아무 값이나 입력하세요 : ")
print(type(answer))   # 입력 받은 값은 항상 문자열 형태로 저
print("입력하신 값은 " + answer + "입니다.")'''

# 다양한 출력 포맷
# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<10}".format(500))
# 세자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000))
# 세자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))
# 세자리 마다 콤마를 찍어주기, 부호도 붙이고 자릿수 확보하기 빈자리는 ^
print("{0:^<+30,}".format(10000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시(소수점 세째 자리에서 반올림)
print("{0:.2f}".format(5/3))

# 파일 입출력