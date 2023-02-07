# 상하좌우
# n = int(input())
# x, y = 1, 1
# plans = input().split()
#
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# move_tpyes = ['L','R','U','D']
#
# for plan in plans:
#     for i in range(len(move_tpyes)):
#         if plan == move_tpyes[i]:
#             nx = x + dx[i]
#             ny = x + dy[i]
#     if nx < 1 or ny <1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
#
# print(x,y)

# 시각
# h = int(input())
#
# count = 0
#
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
#
# print(count)

# 왕실의 나이트
# input_data = input()
# row = int(input_data[1])
# coloum = int(ord(input_data[0])) - int(ord('a')) + 1
#
# steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]
#
# result = 0
#
# for step in steps:
#     next_row = row + step[0]
#     next_coloum = coloum + step[1]
#     if next_row >= 1 and next_row <=8 and next_coloum >= 1 and next_coloum <=8:
#         result += 1
#
# print(result)


# 게임 개발
# n,m = map(int, input().split())
#
# check =[[0]*m for _ in range(n)] # 방문할 위치를 저장할 배열 선언
# A,B,d = map(int, input().split()) # 현재 캐릭터의 x,y 좌표, 방향 입력 받기
# check[A][B] = 1
#
# map_status = []  # 전체 맵 정보 입력 받기
# for i in range(n):
#     map_status.append(list(map(int, input().split())))
#
# dx = [-1,0,1,0]  # 북동남서 방향 선언
# dy = [0,-1,0,1]
#
# def left_turn(): # 왼쪽으로 회전하는 횟수
#     global d
#     d -= 1
#     if(d==-1):
#         d = 3
#
# count = 1 # 방문한 칸의 수(시작 칸 카운트)
# turn_time = 0 # 각 좌표별 회전한 횟수
#
# while True:
#     left_turn() # 왼쪽으로 회전
#     nx = A + dx[d] # 바라보는 방향의 좌표
#     ny = B + dy[d]
#
#     if (nx >= 0 and nx < n and ny >= 0 and ny < m): # 바라보는 방향이 맵 내부에 있는지 확인
#         if(check[nx][ny]==0 and map_status[nx][ny] ==0): # 해당 방향으로 방문할 수 있는지 확인
#             A = nx # 현재 위치 변경
#             B = ny
#             check[nx][ny] = 1 # 방문 체크
#             count += 1 # 방문 칸수 추가
#             turn_time = 0 # 회전 횟수 초기화
#             continue
#         else: # 해당 방향으로 방문할 수 없다면
#             turn_time += 1
#         if (turn_time == 4): # 회전 횟수가 찼다면
#             nx = A - dx[d] # 바라보는 방향은 그대로 두고, 위치만 뒤로 변경
#             ny = B - dy[d]
#             if (check[nx][ny] == 0 and map_status[nx][ny]==0): # 뒤로 갈 수 있다면
#                 A = nx
#                 B = ny
#                 turn_time = 0 # 횟수 초기화
#             else:  # 뒤로 갈 수 없다면
#                 break
# print(count)

######################## 3장 문제 ########################


# 럭키 스트레이트
# n = input
# length = len(n)
# summary = 0
#
# for i in range(length // 2):
#     summary += int(n[i])
#
# for i in range(length//2,length):  # 오른쪽 부분의 자릿수 합 빼기
#     summary -= int(n[i])
#
# if summary == 0:
#     print("LUCKY")
# else:
#     print("READY")

# 문자열 재정렬
# data = input()
# result = []
# value = 0
#
# for x in data:
#     if x.isalpha():  # 알파벳인 경우 리스트에 삽입
#         result.append(x)
#     else:
#         value += int(x)  # 숫자는 따로 더하기
#
# result.sort()
#
# if value != 0:
#     result.append(str(value))
#
# print(''.join(result))  # 요소 하나하나 합쳐서 반환
#
