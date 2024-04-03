import sys

input = sys.stdin.readline

c= int(input())
cases = [[x for x in map(int, input().strip().split())] for _ in range(c)]

for case in cases:
    population = case[0] 
    scores = case[1:len(case)]
    score_avg = sum(scores) / population
    
    above_avg = 0
    for score in scores:
        if score > score_avg:
            above_avg += 1
    
    result = above_avg * 100 / population
    print("{0:6.3f}%".format(result))
        
