import os
import sys


if len(sys.argv) < 2:
    print("Введіть команду 'list' або 'run' з номером лабораторної!")
    sys.exit(1)

command = sys.argv[1]

if command == "list":

    papka = os.listdir("labs/")
    labs = []
    for i in papka:
        if i.startswith("lab"):
            labs.append(i)
    if labs:
        print("Доступні лабораторні роботи:")
        for lab in labs:
            lab_number = lab.split("b")[1]
            print(f"{lab_number}. {lab} - Лабораторна робота №{lab_number}")
    else:
        print("Нема доступних робіт")



elif command == "run":
        
    if len(sys.argv) < 3:
        print("Введіть номер лабораторної після команди run!")
        sys.exit(1)

    number = sys.argv[2]

    try:
        dir = os.listdir("labs/")
        lab_dirs = []

        for i in dir:
            if i.startswith("lab"):
                lab_dirs.append(i)

        number = int(number)
        lab_to_run = f"lab{number}"  

        if lab_to_run in lab_dirs:
            print(f"Запуск лабораторної роботи №{number}...")
            os.system(f"python labs/lab{number}/lab{number}.py")
            print("Результат: Лабораторна виконана успішно!")

        else: 
            print(f"Лабораторна робота №{number} недоступна.")
            
    except ValueError:
        print("Вводте тільки цифри")


else:
    print(f"Невідома команда: {command}. Використовуйте 'list' або 'run'.")

