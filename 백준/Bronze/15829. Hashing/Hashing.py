n = int(input())
my_list = [x for x in input()]

result = 0

for i in range(n):
    result += (ord(my_list[i]) - ord('a') + 1) * pow(31,i)

print(result % 1234567891)