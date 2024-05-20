# 2024.05.21(화)
# 백준 13300: 방 배정
# 주제: 배열

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# 학생 정보 받기
students = [[0, 0] for x in range(6)]

for i in range(N):
    s, g = map(int, input().split())
    students[g - 1][s] += 1

# print(students)
# 필요한 방의 개수 구하기
room = 0
count = 0

for grade in students:
    for s in grade:
        if s % K == 0:
            room += s / K
        else:
            room += s // K + 1

print(int(room))
