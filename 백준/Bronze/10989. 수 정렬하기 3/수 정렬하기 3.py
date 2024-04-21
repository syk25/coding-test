import sys
input = sys.stdin.readline

N = int(input())

numbers = [0]*100001

for i in range(N):
    number = int(input())
    numbers[number] += 1

for i in range(1, 10001):
    if numbers[i] > 0:
        for k in range(numbers[i]):
            print(i)