from sys import stdin
input = stdin.readline

n = int(input())
my_words = [input().strip() for x in range(n)]

# 사전순으로 정렬하기
my_words.sort() # 문자열인 경우 사전순으로 정렬하는 듯 하다.

# 길이순으로 정렬하기
my_words.sort(key = lambda x:len(x)) # key 값을 활용하여 정렬기준을 설정할 수 있다.

# 중복 제거하기
my_words = list(dict.fromkeys(my_words))

# 모든 원소 출력
for word in my_words:
    print(word)