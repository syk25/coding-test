N = int(input())

my_list = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(N-1, i, -1):
        if my_list[j - 1] > my_list[j]:
            my_list[j-1], my_list[j] = my_list[j], my_list[j-1]

for i in my_list:
    print(i)
