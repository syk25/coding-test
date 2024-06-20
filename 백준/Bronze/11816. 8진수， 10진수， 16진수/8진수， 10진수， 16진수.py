s = input().strip()

print(s) if s[0] != '0' else print(int(s, 16)) if s[1] == 'x' else print(int(s, 8))