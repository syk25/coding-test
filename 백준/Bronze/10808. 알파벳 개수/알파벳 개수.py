import sys
input = sys.stdin.readline

word = input().strip()

alphabet = [0]*26

for c in word:
    alphabet[ord(c) - ord('a')] += 1

print(*alphabet, end= ' ')