n = int(input())

pat ='666'
count = 1
check = 666
while count < n:
    check += 1
    my_str = str(check)
    if pat in my_str:
        count += 1

print(check)