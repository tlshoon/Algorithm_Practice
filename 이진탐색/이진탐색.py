# 순차 탐색 소스코드
# def sequential_search(n,target,array):
#     for i in range(n): # 각 원소를 하나씩 확인
#         if array[i] == target:  # 현재의 원소가 찾고자 하는 원소와 동일한 경우
#             return i+1 # 현재의 위치 반환
#
# print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
# input_data = input().split()
# n = int(input_data[0]) # 원소의 개수
# target = input_data[1] # 찾고자 하는 문자열
#
# print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
# array = input().split()
#
# print(sequential_search(n,target,array))

# 재귀 함수로 구현한 이진 탐색
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start+end) // 2 # 찾은 경우 중간점 인덱스 반환
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid + 1, end)
#
# n, target = list(map(int,input().split()))
# array = list(map(int,input().split()))
#
# result = binary_search(array,target,0,n-1)
#
# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result+1)

# 반복문으로 구현한 이진 탐색
# def binary_search(array,target,start,end):
#     while start <= end:
#         mid = (start+end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None
#
# n, target = list(map(int,input().split()))
# array = list(map(int,input().split()))
#
# result = binary_search(array,target,0,n-1)
#
# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result+1)

# 한 줄 입력받아 출력하는 소스코드
# import sys
# input_data = sys.stdin.readline().rstrip()
#
# print(input_data)

# 부품 찾기
# def binary_search(array,target,start,end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return None
#
# n = int(input())
# array = list(map(int,input().split()))
# array.sort()
#
# m = int(input())
# x = list(map(int,input().split()))
#
# for i in x:
#     result = binary_search(array,i,0,n-1)
#     if result != None:
#         print("yes", end= ' ')
#     else:
#         print('no', end=' ')

# 떡볶이 떡 만들기
# n, m = list(map(int,input().split(' ')))
# array = list(map(int,input().split()))
#
# stat = 0  # 이진 탐색을 위한 시작점과 끝점 선점
# end = max(array)
#
# result = 0
# while(stat<=end):
#     total = 0
#     mid = (stat+end) // 2
#     for x in array:
#         if x > mid: # 잘랐을 때 떡의 양 계산
#             total += x - mid
#     if total < m: # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
#         end = mid - 1
#     else: # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
#         result = mid  # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
#         stat = mid + 1
# print(result)

######################## 3장 문제 ########################

# 정렬된 배열에서 특정 수의 개수 구하기

