from sys import stdin

input = stdin.readline

n = int(input())
participants = [x for x in map(int, input().split())]
t,p = map(int, input().split())

total = 0

for shirts in participants:
    adding = shirts // t
    num = 1 + adding if shirts % t != 0 else adding
    total += num

print(total)
print(n // p, n % p)