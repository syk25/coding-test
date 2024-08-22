def factorial(n:int)-> int:
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

my_num_str = str(factorial(int(input())))

count = 0

for i in my_num_str[::-1]:
    if i == '0':
        count += 1
    else:
        break

print(count)


