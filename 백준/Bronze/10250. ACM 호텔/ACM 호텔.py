tests = int(input())
my_list = [list(map(int, input().split()))for x in range(tests)] # 층수, 방수, 손님 번호

for test in my_list:
    height, width, number = test
    x_count, y_count = 1, 0
    while number > height:
        number -= height
        x_count += 1
    y_count = number
    print(str(y_count) + str(x_count).zfill(2))
