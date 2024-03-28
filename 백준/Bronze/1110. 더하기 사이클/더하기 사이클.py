N = input()

a1 = N
counter  = 0


while True:
    a2 = 0

    if len(a1) >= 2:
        for x in a1:
            a2 += int(x)
        a2 = str(a2)
    else:
        a2 = a1 + a1
    
    counter += 1
    
    a1 = a1[-1] + a2[-1]
    if int(a1) == int(N):
        break

print(counter)
