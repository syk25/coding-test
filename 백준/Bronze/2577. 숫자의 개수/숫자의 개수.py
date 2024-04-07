import sys

input = sys.stdin.readline

result = 1

for i in range(3):
    result *= int(input())

numbers = [0] * 10

while result > 0:
    numbers[result % 10] += 1
    result //= 10

for i in numbers:
    print(i)
