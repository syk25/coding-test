my_list = list(map(int, input().split()))

check = 0

if my_list[0] == 1:
    check = 1
    for i in range(8):
        if my_list[i] != i + 1:
            check = 0
            break
elif my_list[0] == 8:
    check = -1
    for i in range(8):
        if 8 - my_list[i] != i:
            check = 0
            break
else:
    check = 0

if check == 1:
    print("ascending")
elif check == -1:
    print("descending")
else:
    print("mixed")