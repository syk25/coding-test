from functools import reduce
from sys import stdin

input = stdin.readline


n = int(input().strip())


def round(my_avg):
    return int(my_avg) if my_avg - int(my_avg) < 0.5 else int(my_avg) + 1


def find_avg(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return int(input().strip())
    if n < 4:
        notion = [int(input().strip()) for x in range(n)]
        my_sum = reduce(lambda x, y: x + y, notion)
        return round(my_sum / n)

    notion = [int(input().strip()) for x in range(n)]

    percent_15 = round(n * 15 / 100)
    percent_30 = 2 * percent_15

    notion.sort()
    my_sum = 0
    for i in range(percent_15, n - percent_15):
        my_sum += notion[i]

    return round(my_sum / (n - percent_30))


print(find_avg(n))
