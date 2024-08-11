from sys import stdin
input = stdin.readline

my_words = set()
for i in range(int(input())):
    my_words.add(input().strip())

for i in sorted(sorted(list(my_words)), key=lambda x:len(x)):
    print(i)