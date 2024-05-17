import sys

input = sys.stdin.readline


def sol():
    N, arr, x = inputs()
    count = logic(N, arr, x)
    print(count)


def inputs():
    N = int(input())
    arr = [i for i in map(int, input().split())]
    x = int(input())
    return N, arr, x


def logic(N, arr, x):
    count, l, r = 0, 0, len(arr) - 1
    arr.sort()
    
    while(l < r):
        now = arr[l] + arr[r]
        if now == x:
            count += 1
            l += 1
            r -= 1
        elif now < x:
            l += 1
        else:
            r -= 1
    
    return count
        

sol()
