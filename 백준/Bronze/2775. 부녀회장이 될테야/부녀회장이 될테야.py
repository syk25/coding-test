t = int(input())
my_list = []
for i in range(t):
    k = int(input())
    n = int(input())
    my_list.append([k,n])



for k, n in my_list:
    floor = [x for x in range(n + 1)] # 0호부터 k호까지 틀 만듬
    for i in range(k):
        for j in range(1, n):
            floor[j + 1] += floor[j]
    print(floor[-1])