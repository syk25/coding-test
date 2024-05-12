import sys
input = sys.stdin.readline

def sol():
    numbers = [x for x in range(21)]
    for i in range(10):
        a, b = map(int, input().split())
        arrange(a, b, numbers)
    print(*numbers[1:21])

def arrange(a, b, numbers):
    reverse = numbers[a:b + 1][::-1]
    for i in range(a, b + 1):
        numbers[i] = reverse[i - a]

sol()
