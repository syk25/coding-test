from typing import Any
from collections import deque
import sys

class Stack:
    def __init__(self):
        self.stk = deque()
    
    def push(self, value:int):
        self.stk.append(value)
    
    def pop(self):
        try:
            my_item = self.stk.pop()
            print(my_item)
        except:
            print(-1)
    
    def size(self):
        print(len(self.stk))
    
    def empty(self):
        if len(self.stk) == 0:
            print(1)
        else:
            print(0)
    
    def top(self):
        if len(self.stk) == 0:
            print(-1)
        else:
            print(self.stk[len(self.stk) - 1])

N = int(input())
stk = Stack()

while N > 0:
    my_command = sys.stdin.readline()
    if 'push' in my_command:
        my_list = my_command.split()
        stk.push(my_list[len(my_list) - 1])
    elif 'top' in my_command:
        stk.top()
    elif 'pop' in my_command:
        stk.pop()
    elif 'size' in my_command:
        stk.size()
    elif 'empty' in my_command:
        stk.empty()
    N -= 1


        
        