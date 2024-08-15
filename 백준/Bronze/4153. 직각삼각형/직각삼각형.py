a, b, c = map(int, input().split())

while not (a == 0 and b == 0 and c == 0):
    my_list = sorted([a,b,c])
    a,b,c = my_list[0], my_list[1], my_list[2]
    if a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")
    a, b, c = map(int, input().split())
