tests = int(input())
my_list = [list(map(int, input().split()))for x in range(tests)] # 층수, 방수, 손님 번호

for height, width, number in my_list:
    y_count = number % height if number % height != 0 else height
    x_count = (number + height - 1) // height
    print(f"{y_count}{x_count:02}")