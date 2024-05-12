import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    calls = [x for x in map(int, input().split())]
    M = minsik(calls)
    Y = youngsik(calls)
    if M < Y:
        print("M", M)
    elif M > Y:
        print("Y", Y)
    else:
        print("Y", "M", Y)
    
def youngsik(calls) -> int:
    charge = 0
    for call in calls:
        charge += 10 + (call // 30) * 10
    return charge

def minsik(calls) -> int:
    charge = 0
    for call in calls:
        charge += 15 + (call // 60) * 15
    return charge

sol()