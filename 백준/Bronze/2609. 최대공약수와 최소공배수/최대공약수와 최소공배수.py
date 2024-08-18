n, m = map(int, input().split())

my_max = max(n, m)
my_min = min(n, m)

"""
두개의 수 중 큰수를 작은 수로 나눈다

나머지가 0이 아닌 경우에 작은 수를 큰수로 갱신하고 나머지를 작은수로 갱신한다
나머지가 0인 경우에 작은 수가 최대공약수다

"""

r = my_max % my_min

while r != 0:
    my_max = my_min
    my_min = r
    r = my_max % my_min

my_gcd = my_min
my_lcm = n * m // my_gcd

print(my_gcd)
print(my_lcm)