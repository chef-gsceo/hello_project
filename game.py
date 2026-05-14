import random

target = random.randint(1, 50)

print("Да начнется игра!")
name = input("Введи имя: ")
more = "ты ЕБЛАН! Слишком много!"
less = "ты ЕБЛАН! Слишком мало!"
win = "Угадал, ЕБЛАН!"

while True:
    guess = int(input("Угадай число: "))
    if guess > target:
        print(f"{name.title()}, {more}")
    elif guess < target:
        print(f"{name.title()}, {less}")
    elif guess == target:
        break

print(win)