my_grade = {'A': 4, 'B':3, 'C': 2, 'D':1, 'F': 0}
my_point = {'+': 0.3, '0':0, '-': -0.3}

grade = input()

if len(grade) < 2:
    print('0.0')
else:
    print(float( my_grade[grade[0]] + my_point[grade[1]]))