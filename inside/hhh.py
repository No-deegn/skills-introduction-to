import random

while True:
    random_number = random.randint(1, 5)
    user_number = input('Угадайте число (от 1 до 5): ')
    if int(user_number) == 0:
        break
    if int(user_number) == random_number:
        print('Вы угадали! :)')
    elif int(user_number) > 5 or user_number == str:
        print("Введите число от 1 до 5")
    else:
        print(f"Вы не угадали! :(")
        print(F"Было загадано число: {random_number}")

    