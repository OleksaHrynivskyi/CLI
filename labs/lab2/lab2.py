import random
from function import find_element

try:
    n = int(input("Введіть кількість елементів списку: "))
    if n < 0:
        print("Ви ввели не додатнє число!")
    else:
        
        spysok_random = [random.randint(-10, 10) for i in range(n)]
        print("Згенерований список:", spysok_random)

        shchyslo = int(input("Введіть число, яке треба знайти: "))

        res = find_element(spysok_random, shchyslo)

        if res != -200:
            print(f"Елемент {shchyslo} знайдено на індексі - {res}")
        else:
            print("Елементів не знайдено")

except ValueError:
    print("Ви ввели не ціле число!")





