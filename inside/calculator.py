print('Calculator')
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
result = input('Выберите действие (+ - / x): ')
if result == "+":
    print(a + b) 
elif result == "-":
    print(a - b)
elif result == "/":
    print(a / b)
elif result == "x":
    print(a * b)
else:
    print('Вы ввели не правельные данные!')
    

