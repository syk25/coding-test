my_list = [int(input()) for _ in range(9)]

my_max = 0
my_max_idx = 0

for i in my_list:
    if i > my_max:
        my_max = i
        my_max_idx = my_list.index(i)

print(my_max)
print(my_max_idx + 1)