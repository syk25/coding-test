# 2024.05.16(목)
# 백준1475: 방 번호
# 주제: 배열

import sys
input = sys.stdin.readline

N = input().strip()

numbers = [0]*10

for n in N:
    numbers[ord(n) - ord('0')] += 1
    

check = (numbers[6] + numbers[9] + 1) // 2

max_number = 0

for i in range(10):
    if i == 6 or i == 9:
        continue
    if max_number < numbers[i]:
        max_number = numbers[i]
    
print(max(max_number, check))