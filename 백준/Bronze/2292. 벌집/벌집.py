t = int(input())

n, start, end = 1, 1, 2

while start < t and end <= t:
    start = end
    end += 6 * n
    n += 1

print(n)