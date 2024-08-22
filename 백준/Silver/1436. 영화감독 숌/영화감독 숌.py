n = int(input())

pat ='666'
count = 1
check = 666

while count < n:
    check += 1
    if pat in str(check):
        count += 1

print(check)