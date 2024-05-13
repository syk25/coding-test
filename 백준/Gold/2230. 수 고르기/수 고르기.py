# 2024.05.13(월)
# 백준 2230: 수 고르기(https://www.acmicpc.net/problem/2230)
# 주제: 투포인터

import sys

input = sys.stdin.readline


def sol():
    N, M = map(int, input().split())
    sorted_numbers = inputs(N)
    answer = logic(N, M, sorted_numbers)
    print(answer)


# 입력함수: 입력받은 후 리스트 정렬
def inputs(N: int) -> list:
    numbers = [int(input()) for x in range(N)]
    numbers.sort()
    return numbers


# 로직함수: 정렬된 리스트에서 차이가 M 이상 중 최소값
def logic(N, M, sorted_numbers) -> int:
    left, right = 0, 0  # 포인터 2개 설정
    result = int(2e9)  # 최소값 추적 변수 설장

    while left <= right and right < N:
        # 두 수의 차이가 M 미만인 경우
        if sorted_numbers[right] - sorted_numbers[left] < M:
            right += 1  # 오른쪽 인덱스 1 추가

        # 두 수의 차이가 M 이상인 경우
        else:
            result = min(result, sorted_numbers[right] - sorted_numbers[left])
            left += 1

    return result


sol()
