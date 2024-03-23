l = [int(input()) for _ in range(9)]

d = sum(l) - 100
l.sort()

p1, p2 = 0, len(l) - 1

while True:
    my_sum = l[p1] + l[p2]
    if my_sum > d:
        p2 -= 1
    elif my_sum < d:
        p1 += 1
    else:
        l[p1], l[p2] = None, None
        break

for i in l:
    if i != None:
        print(i)