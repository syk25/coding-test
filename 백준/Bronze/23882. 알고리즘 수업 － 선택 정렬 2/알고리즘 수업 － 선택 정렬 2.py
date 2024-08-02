import sys

input = sys.stdin.readline

n, k = map(int, input().split())
my_list = [x for x in map(int, input().split())]


def swap(my_list, k):
    for last in range(len(my_list) -1, 0, -1):
        my_max = my_list[last]
        max_idx = last
        for j in range(last -1, -1, -1):
            if my_max < my_list[j]:
                max_idx = j
                my_max = my_list[j]
        if last != max_idx:
            my_list[last], my_list[max_idx] = my_list[max_idx], my_list[last]
            k -= 1
        if k == 0:
            return 0
                


k = swap(my_list, k)

if k == 0:
    print(*my_list)
else:
    print(-1)
