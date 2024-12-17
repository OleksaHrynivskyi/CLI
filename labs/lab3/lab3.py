from function import write_file, read_file



while True:

    print("Меню:\n")
    print("1. Додати студента\n")
    print("2. Відобразити студентів\n")
    print("3. Знайти студента\n")
    print("4. Сортувати студентів за середнім балом\n")
    print("5. Видалити студента\n")
    print("6. Вийти\n")

    try:
        choice = int(input("Виберіть опцію (1-6): "))
        if choice < 1 or choice > 6:
                print("Будь ласка, введіть число від 1 до 6.\n")
                continue
        
        if choice == 6 :
            print("Вихід!")    
            break

        group = input("Введіть групу (Англійською, example 11-KI) ")
        group = group.__add__(".txt")


        if choice == 1 :
            data = read_file(group)
            surname = input("Введіть прізвище студента ")
            try:
                avg_bal = int(input("Введіть середній бал "))
            except ValueError:
                print("Середній бал повинен бути цілим числом\n")
                break
            data.append(surname + " " + str(avg_bal) + "\n")
            write_file(group, data)
            print("Дані успішно додані.\n")
            continue
        

        elif choice == 2 :
            data = read_file(group)
            if not data:
                print("Список порожній")
                continue
            for i, bezN in enumerate(data):
                bezN = bezN.strip('\n')
                print(i+1, bezN)
            print("Список виведений\n")
            continue


        elif choice == 3 :
            data = read_file(group)
            shyk_student = input("Введіть шуканого студента ")
            Find = False
            for i in data: 
                if i.startswith(shyk_student):
                    Find = True
                    surname, avg_bal = i.strip().split(" ")
                    break 
            if Find == True:
                print(f"Студент {surname} знайдений у списку з середнім балом - {avg_bal}\n")
            else:
                print("Студента нема в списку\n")
            continue
               
        
        elif choice == 4 :
            data = read_file(group)
            sorted_data = sorted(data, key=lambda x: float(x.split(" ")[1]), reverse=True)
            if not sorted_data:
                print("Список порожній")
                continue
            sorted_list = "\n".join([entry.strip() for entry in sorted_data])
            print(sorted_list)
            print("Список студентів відсортований за середнім балом\n")
            continue
        

        elif choice == 5 :
            data = read_file(group)
            delete = int(input("Введіть номер студента для видалення "))
            if delete < 1 or delete > len(data):
                    print('Невірний номер студента\n')
                    continue
            index = delete - 1
            stud_delete = data[index].strip('\n')
            data.pop(index)
            print(f"Студента {stud_delete} успішно видалено\n")
            write_file(group, data)
            continue

    except ValueError:
        print("Вводьте правильні числа")


