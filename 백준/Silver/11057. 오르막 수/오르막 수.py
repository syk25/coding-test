N = int(input())
dp_table = [1] * 10

for i in range(0, N):
    for j in range(8, -1, -1):
        dp_table[j] = dp_table[j] + dp_table[j + 1]

print(dp_table[0] % 10007)
