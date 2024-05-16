import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()

a_table = [0] * 26
b_table = [0] * 26

for c in a:
    a_table[ord(c) - ord("a")] += 1

for c in b:
    b_table[ord(c) - ord("a")] += 1

difference = 0

for i in range(26):
    difference += abs(a_table[i] - b_table[i])

print(difference)
