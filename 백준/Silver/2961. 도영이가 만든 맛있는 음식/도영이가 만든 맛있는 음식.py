import sys

input = sys.stdin.readline
MAX = 1e9

n = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(n)]

answer = MAX
for set in range(1, 1<< n):
    sour = 1
    bitter = 0
    for j in range(n):
        if(set & ( 1<< j)) != 0:
            sour *= ingredients[j][0]
            bitter += ingredients[j][1]
    answer = min(answer, abs(sour - bitter))
print(answer)
