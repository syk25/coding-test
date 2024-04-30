# 백준 22460

def divide(x, y, n):
    if n == 1: # 한변의 길이가 2인 경우
        return graph[x][y]
    else: # 한변의 길이가 2보다 많은 경우
        List = [ 
            divide(x, y, n // 2), # top_left
            divide(x, y + (n // 2), n // 2), # top_right
            divide(x + (n // 2), y, n // 2), # borrom_left
            divide(x + (n // 2), y + (n // 2), n // 2), # bottom_right
        ]
        List.sort()
        return List[1]

N = int(input())

graph = [list(map(int, input().split())) for i in range(N)] # 함수 외부에 선언된 객체로서 함수 내부에서 참조함

print(divide(0, 0, N))


