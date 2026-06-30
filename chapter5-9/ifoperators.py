# 5.3. Цвета пришельцев 1. Представьте, что в вашей компьютерной игре только что был подбит корабль пришельцев. Создайте переменную alien_color и присвойте ей значение 'green',
# 'yellow' или 'red'
# • Напишите оператор if для проверки того, что переменная содержит значение
# 'green'. Если условие истинно, то выведите сообщение о том, что игрок только что заработал 5 очков.Напишите одну версию программы, в которои условие it выполняется, и дру-гую, в которой оно не выполняется. (Во второй версии никакое сообщение
# выводиться не должно.)
print('\n5.3')

alien_color = 'green'

if alien_color == 'green':
    print('You earned 5 points!')

alien_color = 'red'

if alien_color == 'green':
    print('You earned 5 points!')


# 5.4. Цвета пришельцев 2. Выберите цвет, как это было сделано в упражне-
# нии 5.3, и напишите цепочку if-else.
# • Напишите оператор if для проверки того, что переменная содержит значение
# 'green'. Если условие истинно, то выведите сообщение о том, что игрок только
# что заработал 5 очков.
# • Если переменная содержит любое другое значение, то выведите сообщение о том, что игрок только что заработал 10 очков.
# • Напишите одну версию программы, в которой выполняется блок if, и другую,
# в которой выполняется блок else.
print('\n5.4')

alien_color = 'red'

if alien_color == 'green':
    print('You earned 5 points!')
else:
    print('You earned 10 points!')

alien_color = 'green'

if alien_color == 'green':
    print('You earned 5 points!')
else:
    print('You earned 10 points!')

# 5.5. Цвета пришельцев 3. Преобразуйте цепочку if-else из упражнения 5.4 в цепочку if-elif-else.
# • Если переменная содержит значение 'green' , выведите сообщение о том, что
# игрок только что заработал 5 очков.
# • Если переменная содержит значение 'yellow', выведите сообщение о том, что игрок только что заработал 10 очков.
# • Если переменная содержит значение 'red', выведите сообщение о том, что игрок только что заработал 15 очков.
# • Напишите три версии программы и проследите за тем, чтобы для каждого цвета пришельца выводилось соответствующее сообщение.
print('\n5.5')

alien_color = 'green'

if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
elif alien_color == 'red':
    print('You earned 15 points!')

alien_color = 'yellow'

if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
elif alien_color == 'red':
    print('You earned 15 points!')

alien_color = 'red'

if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
elif alien_color == 'red':
    print('You earned 15 points!')

