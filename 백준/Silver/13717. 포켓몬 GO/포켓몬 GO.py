import sys

input = sys.stdin.readline


def sol():

    N, pokemon = inputs()
    lv_sum, max_pokemon = logic(N, pokemon)

    print(lv_sum)
    print(max_pokemon)


def inputs() -> tuple:
    N = int(input())
    pokemon = [None] * N

    for i in range(N):
        name = input().strip()
        candy, current = map(int, input().split())
        pokemon[i] = [name, candy, current]

    return (N, pokemon)


def logic(N: int, pokemon: list) -> tuple:
    lv_sum, lv_max = 0, 0
    max_pokemon = ""
    for i in range(N):
        name, candy, current = pokemon[i]
        lv = 0
        while current // candy > 0:
            current -= candy - 2
            lv += 1
        lv_sum += lv
        if lv_max < lv:
            lv_max = lv
            max_pokemon = name
    return (lv_sum, max_pokemon)


sol()
