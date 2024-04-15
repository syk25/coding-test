import sys

input = sys.stdin.readline

N = int(input())

n_list = [x for x in map(int, input().split())]

n_list.sort()

# print(n_list)

if N < 3:
    print(0)
else:
    count, sum = 0, 0
    target, left, right = 0 ,1 , N -1
    while target< len(n_list):
        sum = n_list[left] + n_list[right]
        if left == right:
            target += 1
            left = 0
            right = N-1
        elif left == target or sum < n_list[target]:
            left += 1
        elif right == target or sum > n_list[target]:
            right -= 1
        elif sum == n_list[target]:
            count += 1
            target += 1
            left = 0
            right = N-1
    print(count)
            




