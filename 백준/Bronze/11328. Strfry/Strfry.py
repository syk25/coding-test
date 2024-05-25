import sys
input = sys.stdin.readline

def sol():
    N = int(input())
    my_strings = [input().rstrip() for _ in range(N)]
    for my_string in my_strings: check_alphabet(my_string)
    
        
def check_alphabet(test:str):
    a,b = test.split()
    alphabet = [0] * 26
    for c in a[:]: alphabet[ord(c) - ord('a')] += 1
    for c in b[:]: alphabet[ord(c) - ord('a')] -= 1
    
    print("Possible") if max(alphabet) == 0 and min(alphabet) == 0 else print("Impossible")
    

sol()

