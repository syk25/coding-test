n = int(input())
my_list = [list(input().strip().split()) for x in range(n)]


for j in range(len(my_list)):
    for i in range(len(my_list[j])):
        print((my_list[j][i])[::-1], end=" ")
    print()



