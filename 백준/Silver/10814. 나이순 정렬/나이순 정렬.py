members = []

for i in range(int(input())):
    member = input()
    age = int(list(member.split())[0])
    members.append((age, member))

members.sort(key=lambda x:x[0])

for member in members:
    print(member[1])