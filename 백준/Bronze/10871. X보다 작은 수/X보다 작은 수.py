import sys

input = sys.stdin.readline

N, X = map(int, input().split())

numbers = [int(x) for x in input().split()]

for number in numbers:
    if X > number:
        print(number, end=' ')

