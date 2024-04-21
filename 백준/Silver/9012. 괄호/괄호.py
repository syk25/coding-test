import sys
input = sys.stdin.readline

N = int(input())

def check(line: str):
    stack = []
    for character in line:
        if character == '(':
            stack.append('(')
        else:
            if(len(stack) > 0):
                stack.pop()
            else:
                print('NO')
                return
    if len(stack) > 0:
        print('NO')
        return
    else:
        print('YES')
        return

for i in range(N):
    check(input().strip())