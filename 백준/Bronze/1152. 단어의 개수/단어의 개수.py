import sys

input = sys.stdin.readline

check = input().strip()


if not check:
    print(0)
else:
    words = check.split(" ")
    print(len(words))
