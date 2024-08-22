members = [list(input().strip().split()) for x in range(int(input()))]


members = sorted(members, key=lambda x: int(x[0]))

for member in members:
    print(" ".join(member))