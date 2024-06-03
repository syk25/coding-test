from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())

def foo(no:int, text:str):
    old_word = [x for x in text]
    new_word = deque()
    new_word.append(old_word[0])
    for i in range(1, no):
        new_word.appendleft(old_word[i]) if ord(new_word[0]) - ord(old_word[i]) >= 0 else new_word.append(old_word[i])
    print(''.join(new_word))

for i in range(N):
    no = int(input())
    my_word = input().strip().split(' ')
    foo(no, my_word)