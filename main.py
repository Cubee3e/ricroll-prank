import os
import random
import shutil
import webbrowser

def play_game():
    # Генерируем случайное число от 1 до 10
    correct_number = random.randint(1, 10)
    
    # Запрашиваем у пользователя ввод
    try:
        user_input = int(input("Угадай число от 1 до 10: "))
    except ValueError:
        print("Ошибка: введите число.")
        return

def play_game():
    # Пусть это будет какое-то правильное число
    correct_number = 5

    # Ввод пользователя
    user_input = int(input("Угадай число: "))

    # Проверяем, угадал ли пользователь
    if user_input == correct_number:
        print("Поздравляем, ты победил!")
    else:
        # Открыть ссылку в браузере по умолчанию
        url = "https://youtu.be/oPLObjVAvIU?si=sjl4ixkhEWwtelFh"
        webbrowser.open(url)

play_game()