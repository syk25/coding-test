import sys
input = sys.stdin.readline

cases = int(input())

quizzes = [input().strip() for _ in range(cases)]

points = []

tp = 0

for quiz in quizzes:
    cp = 0
    for result in quiz:
        if result == 'O':
            cp += 1
            tp += cp
        else:
            cp = 0
    points.append(tp)
    tp = 0

for i in points:
    print(i)