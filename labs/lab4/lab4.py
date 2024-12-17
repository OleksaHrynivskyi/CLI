import random
from collections import Counter


try:
    zavd = int(input("Введіть номер завдання (1-3): ")) 

    if zavd < 1 or zavd > 3:
        print("Ви ввели некоректний номер завдання!")
    else:

        if zavd == 1:

            spys1 = ["Красивий", "Щасливий", "Злий", "Швидкий", "Терплячий"]

            spys2 = ["какаду", "собака", "тигр", "страус", "кит"]

            spys3 = ["стрибає", "плаває", "бігає", "говорить", "їсть"]

            print (random.choice(spys1), random.choice(spys2), random.choice(spys3)) 

        elif zavd == 2:
            with open('labs/lab4/book.txt', 'r', encoding='utf-8') as file:
                text = file.read()

            withspaces = len(text)
            withoutspaces = len(text.replace(" ", ""))
            words = text.split()
            allwords = len(words)
            uniquewords = len(set(words))
            wordsCount = Counter(words)
            word1time = []

            for word, count in wordsCount.items():
                if count == 1:
                    word1time.append(word)

            totalwords1 = len(word1time)

            print(f"Кількість слів, які зустрічаються один раз: {totalwords1}")
            print(f"Кількість унікальних слів у тексті: {uniquewords}")
            print(f"Кількість слів у тексті: {allwords}")
            print(f"Кількість символів з пробілами: {withspaces}\nКількість символів без пробілів: {withoutspaces}")

        elif zavd == 3:
            with open('labs/lab4/book.txt', 'r', encoding='utf-8') as file:
                text = file.read()

            words = text.split()
            N = int(input("Введіть кількіть слів у послідовності N: "))
            if N <= 0:
                print("Ви ввели не додатнє число!")
            else:
                spys = []
                words_all = len(words) - N + 1

                for i in range(words_all):
                    aboba = ""
                    for j in range(N):
                        aboba = aboba + words[i + j] + " "
                    aboba = aboba.strip()
                    spys.append(aboba)

                rah = Counter(spys)
                print(f"Топ-10 найчастіше зустрічаємих послідовностей з {N} слів {rah.most_common(10)}")
                

except ValueError:
    print("Вводьте цілі числа!")
except FileNotFoundError:
    print("Файл не знайдено!")
except Exception as e:
    print(f"Сталася помилка: {e}")