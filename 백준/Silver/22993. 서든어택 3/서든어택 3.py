N = int(input())
attack = list(map(int, input().strip().split()))

def findOut(N, attack):
    junwon = attack[0]
    other_attack = sorted(attack[1:len(attack)])
    for i in range(0, len(other_attack)):
        if junwon > other_attack[i]:
            junwon += other_attack[i]
        elif junwon <= other_attack[i]:
            print("No")
            return
    
    print("Yes")

findOut(N, attack)