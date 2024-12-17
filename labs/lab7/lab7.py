import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

try:
    zavd = int(input("Введіть номер завдання (1-3): ")) 

    if zavd < 1 or zavd > 3:
        print("Ви ввели некоректний номер завдання!")
    else:

        if zavd == 1:

            x = np.linspace(0.01, 5, 1000)
            y = 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)
            plt.plot(x, y, color = "pink", label=r'$F(x) = \frac{5 \cos(10x) \sin(3x)}{\sqrt{x}}$')

            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Графік функції F(x) = 5 * cos(10x) * sin(3x) / sqrt(x)')
            plt.legend()

            plt.savefig('labs/lab7/function.png', dpi=500)

            plt.show()

        elif zavd == 2:
            
            text = str(input("Введіть текст для аналізу "))
            text = text.lower()
            text = text.replace(" ", "")
            count = Counter(text)
            bykvu = list(count.keys())
            chastota = list(count.values())

            plt.bar(bykvu, chastota, color='pink')

            plt.xlabel('Літери')
            plt.ylabel('Частота')
            plt.title('Частота літер у тексті')

            plt.savefig('labs/lab7/histograma.png', dpi=500)

            plt.show()

        elif zavd == 3:

            text = (input("Введіть текст для аналізу "))
            text = text.replace('...', ' <<TripleDot>> ')

            prosti = []
            potal = []
            oklich = []
            trykrap = []

            words = text.split()
            for word in words:  
            
                if "<<TripleDot>>" in word:
                    trykrap.append(word)
                elif word.endswith("!"):
                    oklich.append(word)
                elif word.endswith("?"):
                    potal.append(word)
                elif word.endswith("."):
                    prosti.append(word)

            types = ['Прості', 'Питальні', 'Окличні', 'Три крапки']

            chastota = [len(prosti), len(potal), len(oklich), len(trykrap)]

            plt.bar(types, chastota, color=['blue', 'green', 'red', 'orange'])
            plt.xlabel('Типи речень')
            plt.ylabel('Частота')
            plt.title('Частота появи різних типів речень у тексті')

            plt.savefig('labs/lab7/histograma_2.png', dpi=500)

            plt.show()

except ValueError:
    print("Вводьте цілі числа!")
except Exception as e:
    print(f"Сталася помилка: {e}")