my_list = list(map(int, input().split()))

if my_list == sorted(my_list):
    print("ascending")
elif my_list == sorted(my_list, reverse=True):
    print("descending")
else:
    print("mixed")