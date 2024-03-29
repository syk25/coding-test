import sys
first = int(sys.stdin.readline())
second = sys.stdin.readline().split()
my_list = [first * int(x) for x in second[0][::-1]]
print(*my_list, end='\n')
print(first * int(second[0]))
