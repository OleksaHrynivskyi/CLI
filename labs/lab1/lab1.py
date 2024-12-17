from math import *
import random

try:
    zavd = int(input("Введіть номер завдання (1-3): ")) 

    if zavd < 1 or zavd > 3:
        print("Ви ввели некоректний номер завдання!")
    else:

        if zavd == 1:

            m = float(input("Введіть додатнє число m "))

            if m < 0:
                print("Ви ввели не додатнє число!")
            else:
                z = 1/(sqrt(m)+sqrt(2))
                print(z)

        elif zavd == 2:

            def proste(n):

                if n <= 1:
                    return False
                
                if n == 2:
                    return True
                
                if n % 2 == 0:
                    return False
                
                for i in range(3, int(sqrt(n)) + 1, 2):
                    if n % i == 0:
                        return False
                
                return True

            number = int(input("Введіть число: "))
            if proste(number):
                print(f"Число {number} є простим.")
            else:
                print(f"Число {number} не є простим.")

        elif zavd == 3:

            try:

                n = int(input("Введіть кількість елементів списку: "))

                spysok_random = [random.randint(-10, 10) for _ in range(n)]
                print("Згенерований список:",spysok_random)

                min_spys = []

                for i in spysok_random:
                    if i > 0:
                        min_spys.append(i)
                
                min = min(min_spys)

                print(f"Мінімальний додатній елемент: {min}")


                sum_spys = []

                for i in spysok_random:
                    if i % 2 == 0:
                        sum_spys.append(i)
                
                sum = sum(sum_spys)

                print(f"Сума парних елементів: {sum}")

                zvorot = spysok_random[::-1]
                print(f"Зворотній список: {zvorot}")

            except ValueError:
                print("Ви ввели не ціле додатнє число!")
                
except ValueError:
    print("Вводьте числа!")