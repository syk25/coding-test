N = int(input())

for i in range(N):
    a,b = input().split()
    a = int(a)
    print(''.join([a * j for j in b]))