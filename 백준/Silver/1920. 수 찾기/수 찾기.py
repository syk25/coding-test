import sys
N = int(sys.stdin.readline())
numbers = [int(x) for x in sys.stdin.readline().split()]
M = int(sys.stdin.readline())
my_list = [int(x) for x in sys.stdin.readline().split()]

numbers.sort()

def bs(a: list, b: int) -> int:
    l = 0
    r = len(a) - 1

    while l <= r:
        c = (l + r) // 2
        if b > a[c]:
            l = c + 1
        elif b < a[c]:
            r = c -1
        elif b == a[c]:
            return 1
    return 0

for i in range(M):
        print(bs(numbers, my_list[i]))

