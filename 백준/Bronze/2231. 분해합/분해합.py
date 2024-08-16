n = int(input())
def find_constructor(n):
    for i in range(n):
        if i + sum(int(digit) for digit in str(i)) == n:
            return i
    return 0

print(find_constructor(n))