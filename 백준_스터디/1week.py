#### 나이순 정렬 (10814번 / 실버5) ####
# n = int(input())
# members = []
#
# for _ in range(n):
#     age, name = input().split()
#     age = int(age)
#     members.append((age, name))
#
# sorted_members = sorted(members, key=lambda x:x[0])
#
# for member in sorted_members:
#     print(member[0], member[1])

#### 회사에 있는 사람 (7785번 / 실버5) ####
# n = int(input())
# data = set()
#
# for _ in range(n):
#     name, record = input().split()
#     if (record == 'enter'):
#         data.add(name)
#     else:
#         data.remove(name)
#
# sorted_data = sorted(data, reverse=True)
#
# for data in sorted_data:
#     print(data)

# ====================================================================================================================================

# 1. 리스트와 remove() 연산
# 리스트에서 remove() 메서드를 사용하면 최악의 경우 O(n)의 시간 복잡도를 가집니다. 왜냐하면 리스트 내부에서 특정 값을 제거할 때 해당 값을 찾기 위해 리스트 전체를 순회해야 할 수 있기 때문입니다.
# 문제에서 최대 입력 크기가 10^6이므로, 최악의 시나리오에서 리스트에서 값을 제거하는 데 걸리는 시간은 상당히 클 수 있습니다.
#
# 2. set과 값 추가/제거
# set은 기본적으로 해시 테이블을 기반으로 구현되어 있어서 특정 원소를 추가하거나 제거하는 연산은 평균적으로 O(1)의 시간 복잡도를 가집니다.
# 그래서 여러번의 추가/제거 연산을 할 때 set이 훨씬 빠른 성능을 보여줍니다.
#
# 3.리스트 vs. set
# 리스트는 순서가 있지만 set에는 순서가 없습니다. 그래서 set은 중복을 허용하지 않습니다.
# 리스트는 인덱싱을 지원하지만 set은 지원하지 않습니다. 예를 들어, list[3]과 같은 연산은 가능하지만, set에서는 이런 연산을 할 수 없습니다.
# 위에서 언급했듯이, 리스트의 remove() 연산은 O(n)이지만 set의 remove() 또는 discard() 연산은 O(1)입니다.

#### 베스트셀러 (1302번 / 실버 4) ####
# n = int(input())
# books = {}
#
# for _ in range(n):
#     book = input()
#     if book in books:
#         books[book] += 1  ## 이 부분 다시보기
#     else:
#         books[book] = 1
#
# sorted_books = sorted(books.items(), key=lambda x: (-x[1], x[0]))   ## 이 부분 다시보기
#
# print(sorted_books[0][0])

# ====================================================================================================================================
# 1. 딕셔너리란?
# 딕셔너리는 키(key)와 값(value)의 쌍을 항목(item)으로 갖는 컬렉션 타입입니다.
# 파이썬에서 딕셔너리는 중괄호 {}를 사용하여 생성됩니다.
#
# 2. 딕셔너리의 특징
# 순서가 없습니다. 인덱스로 값을 접근할 수 없습니다.
# 키는 변경할 수 없으며, 유일해야 합니다. 값은 변경 가능하고, 중복될 수 있습니다.
# 키에는 주로 문자열, 숫자, 튜플 등 변경 불가능한(immutable) 타입이 사용됩니다.
# 3. 딕셔너리 생성 및 값 접근
#
#
# # 딕셔너리 생성
# person = {"name": "John", "age": 30, "city": "New York"}
#
# # 값 접근
# print(person["name"])  # 출력: John
#
# # get()을 사용한 값 접근
# print(person.get("name"))  # 출력: John
#
# 4. 딕셔너리에 항목 추가/수정/삭제
# # 항목 추가
# person["job"] = "Engineer"
#
# # 항목 수정
# person["city"] = "Boston"
#
# # 항목 삭제
# del person["age"]
#
# 5. 딕셔너리 메소드들
# keys(): 딕셔너리의 모든 키를 반환
# values(): 딕셔너리의 모든 값을 반환
# items(): 딕셔너리의 모든 항목(키-값 쌍)을 반환
# pop(key): 지정된 키의 값을 반환하고, 해당 항목을 딕셔너리에서 삭제
# clear(): 딕셔너리의 모든 항목 삭제
#
# 6. 딕셔너리 순회
# for key, value in person.items():
#     print(key, value)
#
# 7. 딕셔너리 내포(Dictionary Comprehension)
# squared = {x: x*x for x in (2, 3, 4)}
# print(squared)  # 출력: {2: 4, 3: 9, 4: 16}

#### 중복빼고 정렬하기 (10867번 / 실버5) ####
# # 풀이 1
# n = int(input())
# data = sorted(set(map(int,input().split())))
#
# for i in data:
#     print(i, end=" ")
#
# # 풀이 2
# N = int(input())
# numbers = list(map(int, input().split()))
# unique_numbers = list(set(numbers))
#
# unique_numbers.sort()
#
# print(' '.join(map(str, unique_numbers)))  ## 이 부분 다시보기

# ====================================================================================================================================
# 1. end 파라미터:
# 기본값: '\n' (새 줄)
# print 함수는 기본적으로 출력한 후에 줄 바꿈을 합니다. 하지만, end 파라미터를 사용하면 이 동작을 변경할 수 있습니다.
# 예를 들어, end=" "를 설정하면, 출력된 후에 줄 바꿈 대신 공백이 출력됩니다.
# print("Hello", end=" ")
# print("World")
# # 결과: Hello World (한 줄에 출력됩니다)
#
# 2. sep 파라미터:
# 기본값: ' ' (공백)
# print 함수에 여러 아이템을 전달할 때, 각 아이템 사이에 어떤 문자열을 넣을지 결정합니다.
# 예를 들어, sep="-"를 설정하면, 아이템들 사이에 -가 출력됩니다.
# print("Hello", "World", sep="-")
# # 결과: Hello-World

# 문자열 집합 (14425번 / 실버3)
# n, m = map(int, input().split())
# s = set()
# cnt = 0
#
# for _ in range(n):
#     s.add(input())
#
# for _ in range(m):
#     if input() in s:   # 집합에서의 조회는 O(1)    ##이 부분 다시보기
#         cnt += 1
#
# print(cnt)

# ====================================================================================================================================
# 위의 코드는 s를 집합으로 선언하고, 입력 받는 문자열을 집합에 추가합니다.
# 이후, m번 문자열을 입력 받으면서 집합 s에 해당 문자열이 포함되어 있는지 확인합니다.
# 이 방법은 리스트를 사용한 방법보다 훨씬 빠르게 작동합니다.
#
# 내가 푼 방법 :
# for i in s:
#     if i in target:
# 의 경우, s의 각 문자열을 target 리스트와 비교합니다.
# in 연산자를 사용하여 리스트에서 항목을 찾을 때마다 전체 리스트를 탐색하게 되므로, 이는 비효율적입니다.