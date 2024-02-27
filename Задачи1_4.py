import random

while True:
    user_choice = input("Введите ваш выбор (камень, ножницы или бумага): ")
    computer_choice = random.choice(["камень", "ножницы", "бумага"])

    print(f"Ход компьютера: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "камень" and computer_choice == "ножницы") or (user_choice == "ножницы" and computer_choice == "бумага") or (user_choice == "бумага" and computer_choice == "камень"):
        print("Вы победили!")
    else:
        print("Компьютер победил!")

    play_again = input("Хотите сыграть еще раз? (да/нет): ")
    if play_again.lower() != "да":
        break