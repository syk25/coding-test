n = int(input())
def find_constructor(n):
    start = max(1, n - 54)
    for i in range(start, n):
        if i + sum(int(digit) for digit in str(i)) == n:
            return i
    return 0

print(find_constructor(n))