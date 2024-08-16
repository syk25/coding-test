n = int(input())
answer = 0

for i in range(n):
    check, temp = i, i
    while check > 0:
        r = check % 10
        temp += r
        check //= 10
    if temp == n:
        answer = i
        break

print(answer)



