my_list = []
while True:
    my_list.append(input())
    if my_list[-1] == "0":
        break


for i in range(len(my_list) - 1):
    check = True
    for j in range((len(my_list[i]) // 2) + 1):
        if my_list[i][j] != my_list[i][len(my_list[i]) - 1 - j]:
            print("no")
            check = False
            break
    if check:
        print("yes")
