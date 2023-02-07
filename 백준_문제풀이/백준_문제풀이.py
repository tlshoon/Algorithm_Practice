# 2588
# a = int(input("숫자1: "))
# b = input("숫자2: ")
#
# c = a*int(b[2])
# d = a*int(b[1])
# e = a*int(b[0])
#
# print(c,d,e,a*int(b[:]), end='=')

# 1330
# a = int(input("숫자1:"))
# b = int(input("숫자2:"))
#
# if a < b:
#     print("<")
# elif a > b:
#     print(">")
# else:
#     print("==")

# # 9498
# point = int(input("시험성적: "))
#
# if 90<=point<=100:
#     print("A")
# elif 80<=point<=89:
#     print("B")
# elif 70<=point<=79:
#     print("C")
# elif 60<=point<=69:
#     print("D")
# else:
#     print("F")

# 2753
# year = int(input("년도: "))
#
# if year % 4 == 0 and year % 400 == 0:
#     print("1")
# elif year % 4 == 0 and year % 100 != 0:
#     print("1")
# else:
#     print("0")

# 14681
# quadrant_x = int(input("x좌표: "))
# quadrant_y = int(input("y좌표: "))
#
# if quadrant_x > 0 and quadrant_y > 0:
#     print("1")
# elif quadrant_x < 0 and quadrant_y > 0:
#     print("2")
# elif quadrant_x < 0 and quadrant_y < 0:
#     print("3")
# else:
#     print("4")

# 2884
# h, m = map(int, input(" ").split())
# m -= 45
# if m < 0:
#     m += 60
#     h -= 1
#     if h < 0:
#         h = 23
# print(h, m)

# 2739
# n = int(input("숫자를 입력하시오: "))
# for i in range(1,10):
#     print(n, '*', i, '=', n*i)

# 10950
# t = int(input())
#
# for i in range(t):
#     a,b = map(int, input().split())
#     print(a+b)

# 8393
# n = int(input())
# sum = 0
#
# for i in range(n+1):
#     sum += i
# print(sum)

# 15552
# import sys
#
# t = int(input())
# for i in range(t):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)

# 2741
# n = int(input())
#
# for i in range(1, n+1):
#     print(i)

# 2742
# n = int(input())
#
# for i in range(n):
#     print(n-i)

# 11021
# n = int(input())
#
# for i in range(n):
#     a,b = map(int, input().split())
#     print("Case #%d: %d"%(i+1,a+b))

# 11022
# n = int(input())
#
# for i in range(n):
#     a,b = map(int, input().split())
#     print("Case #%d: %d + %d = %d"%(i+1,a,b,a+b))

# 2438
# n = int(input())
# for i in range(1,n+1):
#     print("*"*i)

# 2439
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)

# 10871
# n,x = map(int, input().split())
# a = list(map(int, input().split()))
#
# for i in range(n):
#     if a[i] < x:
#         print(a[i], end=" ")

# 10952
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)

# 10951
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except:
#         break

# 1110
# n = int(input())
# num = n
# cnt = 0
#
# while True:
#     a = num // 10
#     b = num % 10
#     c = (a+b) % 10
#     num = (b*10) + c
#
#     cnt = cnt + 1
#     if num == n:
#         break
# print(cnt)

# 10818
# n = int(input())
# num = list(map(int, input().split()))
# print(min(num),max(num))

# 2562
# num = []
# for i in range(9):
#     num.append((int(input())))
# print(max(num))
# print(num.index(max(num))+1)

# 2577
# A = int(input())
# B = int(input())
# C = int(input())
#
# D = list(str(A * B * C))
#
# for i in range(10):
#     print(D.count(str(i)))

# 3052
# num = []
# for i in range(10):
#     n = int(input())
#     num.append(n % 42)
# num = set(num)
# print(len(num))

# 1546
# n = int(input())
# test_list = list(map(int, input().split()))
# max_score = max(test_list)
#
# new_list = []
# for score in test_list:
#     new_list.append(score/max_score * 100)
# test_avg = sum(new_list) / n
# print(test_avg)

# 8958
# n = int(input())
#
# for i in range(n):
#     a = input()
#     score = 0
#     sum_score = 0
#     for j in a:
#         if j == 'o':
#             score += 1
#         else:
#             score = 0
#         sum_score += score
#     print(sum_score)

# 10773
# k = int(input())
#
# stack = []
#
# for i in range(k):
#     a = int(input())
#     if a == 0:
#         stack.pop()
#     else:
#         stack.append(a)
# print(sum(stack))

# 11399
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# cnt = 0
# s = 0
# for i in range(n):
#     cnt += data[i]
#     s += cnt
# print(s)

# 샤틀버스
# x,y= input().split()
# x = int(x)
# y = int(y)
#
# if x>y:
#     print(x+y)
# else:
#     a = y//x
#     b = a*x
#     print(y-b)

# 2606번
# from collections import deque
# n = int(input())  # 컴퓨터 개수
# v = int(input())  # 연결선 개수
#
# graph = [[] for _ in range(n+1)]  # 그래프 초기화
# visited = [0] * (n+1)  # 방문한 컴퓨터인지 표시
#
# for i in range(v):
#     a,b = map(int,input().split())
#     graph[a] += [b]  # a에 b연결
#     graph[b] += [a]  # b에 a연결  -> 양방향  // 이중리스트
#
# visited[1] = 1  # 1번부터 컴퓨터 시작이니 방문 표시
# q=deque([1])
#
# while q:
#     start = q.popleft()
#     for nx in graph[start]:
#         if visited[nx] == 0:시
#             visited[nx] = 1
#
# print(sum(visited)-1)

# 1260번
# from collections import deque
# n, m, v = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
#
#
# for i in range(m):
#     a,b = map(int,input().split())
#     graph[a] += [b]
#     graph[b] += [a]
#
# for i in range(m):
#     graph[i].sort()
#
#
# visited_bfs = [False] * (n+1)
# visited_dfs = [False] * (n+1)
#
# def dfs(graph, start, visited_dfs):
#     visited_dfs[start] = True
#     print(start,end=' ')
#     for i in graph[start]:
#         if visited_dfs[i] == False:
#             dfs(graph,i,visited_dfs)
#
# def bfs(graph, start, visited_bfs):
#     queue=deque([start])
#     visited_bfs[start] = True
#     while queue:
#         bfs_now = queue.popleft()
#         print(bfs_now,end=' ')
#         for i in graph[bfs_now]:
#             if visited_bfs[i] == False:
#                 queue.append(i)
#                 visited_bfs[i] = True
#
# dfs(graph,v,visited_dfs)
# print(sep='')
# bfs(graph, v, visited_bfs)

# 14716번
# n,m = map(int,input().split())
# data = []
# for i in range(n):
#     data.append(list(map(int,input().split())))
#
#
# def dfs(x,y):
#     if x<= -1 or x >=n or y <= -1 or y >=m:
#         return False
#     if data[x][y] == 1:
#         data[x][y] = 0
#         dfs(x-1,y)
#         dfs(x, y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#         dfs(x+1, y+1)
#         dfs(x-1, y+1)
#         dfs(x+1, y-1)
#         dfs(x-1, y-1)
#         return True
#     return False
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i,j) == True:
#             result += 1
# print(result)

# 11047번
## 1. 계산대 안에 있는 돈의 수와 거슬러 줄 돈을 구합니다.
# N, K = map(int, input().split()) # N : 화폐 종류수, K : 거슬러 줄 돈
#
# # 2. 계산대에 있는 화폐들을 리스트의 형태로 입력받습니다.
# coins = []
# for _ in range(N):
#     coins.append(int(input()))
# coins.sort(reverse=True)
# # coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
#
# # 3. 만약 '계산대 안에 있는 화폐'보다 '거슬러 줄 돈'이 크다면
# # 돈을 거슬러 줍니다.
# answer = 0
# for coin in coins:
#     if K >= coin:
#         answer += K // coin  # 몫만큼 더하기
#         K %= coin # 나머지 할당
#         if K <= 0: # 만약 K가 0이면 반복문을 탈출합니다.
#        		break
# print(answer) # 거슬러 준 동전 + 화폐의 수

# 1026번
# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
#
# a.sort()
# b.sort(reverse=True)
# s = 0
# for i in range(n):
#     s += a[i] * b[i]
# print(s)

# 4963번
# def bfs(x,y):
#     if 0<= x and x < h and 0 <= y and y < w:
#         if graph[x][y] == 1:
#             graph[x][y] = 2
#             bfs(x-1,y-1)
#             bfs(x-1,y)
#             bfs(x-1,y+1)
#             bfs(x,y+1)
#             bfs(x,y-1)
#             bfs(x+1,y-1)
#             bfs(x+1,y)
#             bfs(x+1,y+1)
#             return True
#         return False
#
# dx = [-1,-1,-1,0,0,1,1,1]
# dy = [-1,0,1,-1,1,-1,0,1]
#
# while True:
#     w, h = map(int, input().split())
#     if not w and not h:
#         break
#     graph = [list(map(int,input().split())) for _ in range(h)]
#     cnt = 0
#
#     for i in range(w):
#         for j in range(h):
#             if bfs(i,j) == True:
#                 cnt += 1
#     print(cnt)

# 1427번
# n = list(map(int,input()))
# n.sort(reverse=True)
# for i in n:
#     print(i,end='')

# 11656번
# s = input()
#
# dict = []
# for i in range(len(s)):
#     dict.append(s[i:])
#
# dict.sort()
#
# for i in dict:
#     print(i,sep='')

# 9237번
# n = int(input())
# t = list(map(int,input().split()))
# t.sort(reverse=True)
#
# for i in range(n):
#     t[i] = t[i] - (n-1-i)
#
# max_value = max(t)
# cnt = n + 1 + max_value
#
# print(cnt)

# 5585번

# n = int(input())
#
# coins = [500,100,50,10,5,1]
#
# change = 1000 - n
# cnt = 0
#
# for coin in coins:
#     cnt += change // coin
#     change %= coin
#
# print(cnt)

# 2752번
# n = list(map(int,input().split()))
# n.sort()
# for i in n:
#     print(i,end=" ")

# 10867번
# n = int(input())
#
# data = set(map(int,input().split()))
#
# a = sorted(data)
#
# print(a)
# for i in a:
#     print(i,end=" ")

# 1389번
# from collections import deque
#
# def bfs(graph,start):
#     num = [0] * (n+1)
#     visited = [start]
#     queue = deque()
#     queue.append(start)
#
#     while queue:
#         a = queue.popleft()
#         for i in graph[a]:
#             if i not in visited:
#                 num[i] = num[a] + 1
#                 visited.append(i)
#                 queue.append(i)
#     return sum(num)
#
# n,m = map(int,input().split())
#
# graph = [[] for _ in range(n+1)]
#
# for i in range(m):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# result = []
# for i in range(1,n+1):
#     result.append(bfs(graph, i))
#
# print(result.index(min(result))+1)

# 1302번
# book = dict()
# n = int(input())
# for _ in range(n):
#     name = input()
#     if name in book:
#         book[name] += 1
#     else:
#         book[name] = 1
#
# max = 0
# sbook = dict(sorted(book.items()))
#
# for i in sbook:
#     if (sbook[i]) > max:
#         max = sbook[i]
#         maxi = i
# print(maxi)

# 1920번
# import sys
#
# n = int(input())
# a = list(map(int,sys.stdin.readline().split()))
# a.sort()
# m = int(input())
# b =  list(map(int,sys.stdin.readline().split()))
#
# def binary_search(a,b):
#     start = 0
#     end = len(a) - 1
#
#     while start <= end:
#         mid = (start+end) // 2
#         if b == a[mid]:
#             return 1
#         elif b > a[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#
#     return 0
#
# for i in range(m):
#     print(binary_search(a,b[i]))

# 7795번
# def binary_search(B,a):
#     start = 0
#     end = len(B) - 1
#     res = -1
#     while start <= end:
#         mid = (start + end) // 2
#         if B[mid] < a:
#             res = mid
#             start = mid + 1
#         else:
#             end = mid - 1
#     return res
#
# for _ in range(int(input())):
#     n,m = map(int,input().split())
#     A = sorted(list(map(int,input().split())))
#     B = sorted(list(map(int,input().split())))
#     cnt = 0
#     for a in A:
#         cnt += (binary_search(B,a) + 1)
#     print(cnt)

# 2805번
# n, m = map(int,input().split())
# array = sorted(list(map(int,input().split())))
#
# start = 0
# end = max(array)
#
# result = 0
#
# while start <= end:
#     total = 0
#     mid = (start+end) // 2
#     for x in array:
#         if x > mid:
#             total += x - mid
#
#     if total < m:
#         end = mid - 1
#     else:
#         result = mid
#         start = mid + 1
#
# print(result)

# 2271번
# n = int(input())
# rope = []
# for _ in range(n):
#     rope.append(int(input()))
# rope.sort(reverse=True)
#
# value = []
#
# for num in range(n):
#     value.append(rope[num]*(num+1))
# print(max(value))

# 14916번
# n = int(input())
# cnt = 0
# i = 0
# while True:
#     if n%5 == 0:
#         cnt += n //5
#         break
#     else:
#         n -= 2
#         cnt += 1
#
#     if n < 0 :
#         break
# if n < 0:
#     print(-1)
# else:
#     print(cnt)

# 1753번
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# n,m = map(int,input().split())
# start = int(input())
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)
#
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))
#
#
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1,n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index
#
# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
# dijkstra(start)
#
# for i in range(1,n+1):
#     if distance[i] == INF:
#         print("INF")
#     else:
#         print(distance[i])

# 1916번
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# n = int(input())
# m = int(input())
#
# graph = [[] for _ in range(n+1)]
# visited = [False] * (n+1)
# distance = [INF] * (n+1)
#
# for _ in range(m):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))
#
# start, destination = map(int,input().split())
#
#
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1,n+1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index
#
#
# def dijkstra(start):
#     visited[start] = True
#     distance[start] = 0
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for i in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
# dijkstra(start)
#
# print(distance[destination])

# 1238번
# import heapq
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# v, e, x = map(int, input().split())
# graph = [[] for _ in range(v + 1)]
#
# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     graph[a].append((b, cost))
#
#
# def dijkstra(start):
#     q = []
#     distance = [INF] * (v + 1)
#
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#
#     while q:
#         dist, now = heapq.heappop(q)
#
#         if distance[now] < dist:
#             continue
#
#         for node_index, node_cost in graph[now]:
#             cost = dist + node_cost
#
#             if distance[node_index] > cost:
#                 distance[node_index] = cost
#                 heapq.heappush(q, (cost, node_index))
#
#     return distance
#
#
# result = 0
# for i in range(1, v + 1):
#     go = dijkstra(i)
#     back = dijkstra(x)
#     result = max(result, go[x] + back[i])
#
# print(result)

# 2725번
# t = int(input())
#
# for _ in range(t):
#     floor = int(input()) # 층
#     num = int(input()) # 호
#     f0 = [x for x in range(1,num+1)]  # 0층 리스트
#     for k in range(floor):
#         for i in range(1,num):
#             f0[i] += f0[i-1]
#     print(f0[-1])

# 2178번
# from collections import deque
#
# n,m = map(int,input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input())))
#
# dx = [-1,1,0,0]   # 이동할 네 방향 정의(상,하,좌,우)
# dy = [0,0,-1,1]
#
#
# def bfs(x,y):
#     queue = deque()  # 큐 구현을 위해 deque 라이브러리 사용
#     queue.append((x,y))
#     while queue:  # 큐가 빌 때까지 반복
#         x,y = queue.popleft()
#         for i in range(4):  # 현재 위치에서 네 방향으로의 위치 확인
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:  # 벽인 경우 무시
#                 continue
#             if graph[nx][ny] == 1:  # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx,ny))
#     return graph[n-1][m-1]
#
# print(bfs(0,0))

# 2748번
# d = [0] * 100
#
# d[1] = 1
# d[2] = 1
# n = int(input())
#
# for i in range(3,n+1):
#     d[i] = d[i-1] + d[i-2]
# print(d[n])

# 9095번
# T = int(input())
#
# def sol(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n == 3:
#         return 4
#     else:
#         return sol(n-1) + sol(n-2) + sol(n-3)
#
# for i in range(T):
#     n = int(input())
#     print((sol(n)))

# 1932번
# n = int(input())
#
# t = []
# for i in range(n):
#     t.append(list(map(int,input().split())))
#
# k = 2
# for i in range(1,n):
#     for j in range(k):
#         if j == 0:
#             t[i][j] = t[i][j] + t[i-1][j]
#         elif i == j:
#             t[i][j] = t[i][j] + t[i-1][j-1]
#         else:
#             t[i][j] = max(t[i-1][j-1],t[i-1][j])+t[i][j]
#     k += 1
# print(max(t[n-1]))

# 14720번
# n = int(input())
# milk = list(map(int,input().split()))
# cnt = 0
#
# for i in range(n):
#     if milk[i] == cnt % 3:
#         cnt += 1
# print(cnt)

# 16435번
# n, l = map(int,input().split())
# h = list(map(int,input().split()))
# h.sort()
#
# for i in range(n):
#     if l >= h[i]:
#         l += 1
# print(l)

# 7568번
# n = int(input())
#
# data = []
# for _ in range(n):
#     data.append(list(map(int,input().split())))
#
# cnt = 0
#
# for i in data:
#     rank = 1
#     for j in data:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank += 1
#     print(rank,end=' ')

# 10162번
# n = int(input())
#
# time = [300,60,10]
# cnt = 0
#
# for i in time:
#     if n % 10 == 0:
#         cnt = n // i
#         n %= i
#         print(cnt, end=" ")
#     else:
#         print(-1)
#         break

# 11508번
# n = int(input())
# data = []
# for i in range(n):
#     data.append(int(input()))
# data.sort(reverse=True)
#
# result = 0
# for i in range(2,len(data),3):
#     result += data[i]
#
# print(sum(data)-result)

# 1449번
# n, l = map(int,input().split())
# data = list(map(int,input().split()))
# data.sort()
#
# cnt = 1
#
# stat = data[0]
# end = data[0] + l
# cnt = 1
# for i in range(n):
#     if stat <= data[i] < end:
#         continue
#     else:
#         stat = data[i]
#         end = data[i] + l
#         cnt += 1
# print(cnt)

# 10026번
# from collections import deque
#
# n = int(input())
# graph = [list(map(str,input())) for _ in range(n)]
# visited = [[0] * n for _ in range(n)]
# queue = deque()
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# def bfs(x,y):
#     queue.append([x, y])
#     visited[x][y] = 1
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
#                     queue.append([nx,ny])
#                     visited[nx][ny] = 1
#
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if visited[i][j] == 0:
#             bfs(i,j)
#             cnt += 1
# print(cnt,end=' ')
#
#
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 'R':
#             graph[i][j] = 'G'
#
# cnt = 0
# visited = [[0] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if visited[i][j] == 0:
#             bfs(i,j)
#             cnt += 1
# print(cnt)

# 2667번
# from collections import deque
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# def bfs(graph,a,b):
#     n = len(graph)
#     queue = deque()
#     queue.append([a,b])
#     graph[a][b] = 0
#     count = 1
#
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append([nx,ny])
#                 count += 1
#     return count
#
# n = int(input())
# graph = [list(map(int,input())) for _ in range(n)]
#
# cnt = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             cnt.append(bfs(graph,i,j))
#
# cnt.sort()
# print(len(cnt))
# for i in range(len(cnt)):
#     print(cnt[i])

# 7562번
# from collections import deque
# queue = deque()
#
# dx = [2,1,2,1,-2,-2,-1,-1]
# dy = [1,2,-1,-2,1,-1,2,-2]
#
# def bfs(x,y):
#     visited[x][y] = 1
#     queue.append([x,y])
#     while queue:
#         x,y = queue.popleft()
#         for i in range(8):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= m or ny < 0 or ny >= m:
#                 continue
#             if visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append([nx,ny])
#     return graph[c][d]
#
# n = int(input())
# for i in range(n):
#     m = int(input())
#     graph = [[0] * m for _ in range(m)]
#     visited = [[0] * m for _ in range(m)]
#     a,b = map(int,input().split())
#     c,d = map(int,input().split())
#     print(bfs(a,b))


# 1743번
# from collections import deque
# n,m,k = map(int,input().split())
#
# queue = deque()
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# visited = [[0] * m for _ in range(n)]
#
# graph = [[0] * m for _ in range(n)]
#
# for i in range(k):
#     a,b = map(int,input().split())
#     graph[a-1][b-1] = 1
#
#
# def bfs(x,y):
#     cnt = 0
#     visited[x][y] = 1
#     queue.append([x,y])
#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if visited[nx][ny] == 1:
#                 continue
#             if graph[nx][ny] == 1:
#                 visited[nx][ny] = 1
#                 queue.append([nx,ny])
#                 cnt += 1
#     return cnt + 1
#
# max_food = 0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1 and visited[i][j] == 0:
#             max_food = max(max_food, bfs(i,j))
# print(max_food)

# 10815번
# n = int(input())
# array = sorted(list(map(int,input().split())))
# m = int(input())
# target_data = list(map(int,input().split()))
#
# def binary_search(array,target,start,end):
#     while start <= end:
#         mid = (start+end) // 2
#         if target == array[mid]:
#             return True
#         elif target > array[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return False
#
# for i in target_data:
#     if binary_search(array,i,0,n-1) == True:
#         print(1,end=' ')
#     else:
#         print(0,end=' ')
#
# 2847번
# n = int(input())
#
# score = []
# for i in range(n):
#     score.append(int(input()))
#
# cnt = 0
# for i in range(n-2,-1,-1):
#     if score[i] >= score[i+1]:
#         cnt += score[i] - score[i+1] + 1
#         score[i] = score[i+1]-1
# print(cnt)

# 11053번
# n = int(input())
# array = list(map(int,input().split()))
# dp = [0 for _ in range(n)]
#
# for i in range(n):
#     for j in range(i):
#         if array[i] > array[j] and dp[i] < dp[j]:
#             dp[i] = dp[j]
#     dp[i] += 1
# print(max(dp))

# 2839번
# sugar = int(input())
#
# bag = 0
#
# while sugar >= 0:
#     if sugar % 5 == 0:
#         bag += (sugar // 5)
#         print(bag)
#         break
#     sugar -= 3
#     bag += 1
# else:
#     print(-1)

# 2668번
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(float(input()))
#
# for i in range(1,n):
#     arr[i] = max(arr[i], arr[i]*arr[i-1])
#
# print('%0.3f'%max(arr))

# 1793번
# n = int(input())
#
# d = [0] * 251
#
# d[1] = 1
# d[2] = 3
#
# for i in range(3,n+1):
#     d[i] = d[i-1] + (2 * d[i-2])
#
# print(d[n])

# 11726번
# n = int(input())
#
# d = [0] * 1001
# d[1] = 1
# d[2] = 2
#
# for i in range(3,n+1):
#     d[i] = (d[i-1] + d[i-2]) % 10007
#
# print(d[n])

# 11497번
# t = int(input())
#
# for i in range(t):
#     n = int(input())
#     l = list(map(int, input().split()))
#     l.sort()
#
#     data_1 = []
#     data_2 = []
#
#     for i in range(len(l)):
#         if i % 2 == 0:
#             data_1.append(l[i])
#         else:
#             data_2.append(l[i])
#
#     data_2.sort(reverse=True)
#
#     for i in data_2:
#         data_1.append(i)
#
#     cnt = 0
#     for i in range(len(data_1)):
#         if i == len(data_1) - 1:
#             last_value = abs(data_1[len(data_1) - 1] - data_1[0])
#             break
#         abs_value = abs(data_1[i + 1] - data_1[i])  #
#         max_value = max(cnt, abs_value)
#         cnt = max_value
#
#     last_maxvalue = max(last_value, max_value)
#     print(last_maxvalue)