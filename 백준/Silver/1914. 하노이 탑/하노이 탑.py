import sys

N = int(sys.stdin.readline())


def hanoi(n: int, x: int, y: int) -> None:
    if n > 1:
        hanoi(n - 1, x, 6-x-y)

    print(f'{x} {y}')

    if n > 1:
        hanoi(n-1, 6-x-y, y)


print(2 ** N -1)
if N <= 20:
    hanoi(N, 1, 3)