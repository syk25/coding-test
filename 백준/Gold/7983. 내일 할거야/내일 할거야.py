from heapq import heappush, heappop

import sys

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    d, t = map(int, input().split())
    heappush(heap, (-t, d))  # 마지막 날짜 기준으로 힙큐 생성

start, work = heappop(heap)
start *= -1
start -= work
# print("시작:", start)

while heap:
    x, work = heappop(heap)
    x *= -1
    start = min(start, x) - work
    # print("시작:", start)

print(start)
