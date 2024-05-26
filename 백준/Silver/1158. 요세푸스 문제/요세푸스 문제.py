# 2024.05.26(일)
# 백준 1158: 요세푸스
# 주제: 구현

import sys
from collections import deque

input = sys.stdin.readline

# 입력받기
N, K = map(int, input().split())
q = deque([x for x in range(1, N + 1)])  # 큐
p = [0] * N  # 순서를 담는 배열

# 요세푸스 순열 구하기
while len(q) > 1:
    for _ in range(K - 1):
        q.append(q.popleft())
    p[N - len(q) - 1] = q.popleft()

p[N - 1] = q.popleft()

# 출력하기
print("<", end="")
for i in range(N - 1):
    print(p[i], ", ", sep="", end="")
print(p[N - 1], ">", end="", sep="")
