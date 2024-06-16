n = int(input())

temp = n

if n != 1:
    for i in range(2, n + 1):
        while temp % i == 0:
            print(i)
            temp /= i
        if temp == 1:
            break