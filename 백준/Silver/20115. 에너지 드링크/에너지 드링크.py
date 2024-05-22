import sys
from collections import deque

input = sys.stdin.readline


def sol():
    N, drinks = inputs()
    shinla_tensei = logic(N, drinks)
    print(shinla_tensei)


def inputs():
    N = int(input())
    drinks = [x for x in map(int, input().split())]
    drinks.sort()
    return N, drinks


def logic(N, drinks):
    
    for i in range(N-1):
        drinks[-1] = drinks[-1] + drinks[i] / 2
    
    return drinks[-1]


sol()
