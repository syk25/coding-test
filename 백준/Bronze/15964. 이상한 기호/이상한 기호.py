def calc(a, b):
    return (a + b) * (a - b)

a,b = map(int, input().split())

print(calc(a,b))