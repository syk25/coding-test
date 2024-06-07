from sys import stdin

input = stdin.readline


def sol():
    N, M = map(int, input().split())
    press_e = sorted([x for x in map(int, input().split())])
    press_o = sorted([x for x in map(int, input().split())])
    cnt_e = logic(press_e, 100)
    cnt_o = logic(press_o, 360)
    print(f"{cnt_e} {cnt_o}")


def logic(press, duration):
    cnt = 1
    start = press[0]
    cur = start

    if len(press) == 1:
        return cnt

    for i in range(1, len(press)):
        if press[i] - cur >= duration:
            cur = press[i]
            cnt += 1
    return cnt


sol()
