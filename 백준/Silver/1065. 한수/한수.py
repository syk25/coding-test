import sys

input = sys.stdin.readline

N = int(input())
count = N

if N < 100:
    print(count)
else:
    for number in range(100, N + 1):
        number = str(number)
        d = int(number[0]) - int(number[1])
        for i in range(1, len(number)-1):
            sub = int(number[i]) - int(number[i+1])
            if d != sub:
                count -= 1
                break
    print(count)

