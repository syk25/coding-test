my_list = [input() for x in range(3)]

check = 0

for i in range(3):
    if  0<= ord(my_list[i][0]) - ord('0') <= 9:
        check = i
        break

result_number = int(my_list[check]) + 3 - check

if result_number % 3 == 0 and result_number % 5 == 0:
    print("FizzBuzz")
elif result_number % 3 == 0:
    print("Fizz")
elif result_number % 5 == 0:
    print("Buzz")
else:
    print(result_number)