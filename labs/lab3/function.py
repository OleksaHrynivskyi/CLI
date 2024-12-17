

def read_file(file_name):
    try: 
        with open("labs/lab3/" + file_name, 'r', encoding = "utf-8") as file_local:
            datas = file_local.readlines()
            return datas
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")
        create_file = input("Бажаєте створити файл? (так/ні): ").strip().lower()
        if create_file == "так":
            write_file(file_name, [])
            print(f"Файл {file_name} створено.")
            return []
        else:
            print("Операція скасована.")
            return []

def write_file(file_name, data):
        with open("labs/lab3/" + file_name, 'w', encoding = "utf-8") as file_local:
            file_local.writelines(data)
