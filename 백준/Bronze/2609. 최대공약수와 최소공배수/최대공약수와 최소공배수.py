n, m = map(int, input().split())

gcd = 1

for i in range(1, max(n,m) + 1):
    if n % i == 0 and m % i == 0:
        gcd = i
lcm = n * m // gcd

print(gcd)
print(lcm)