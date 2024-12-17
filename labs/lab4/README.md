# Лабораторна робота №4: Робота з рядками у мові Python

## Опис проекту
Програма складається з трьох різних завдань для роботи з текстом та випадковими послідовностями.

## Завдання

### Завдання 1: Генерація випадкового речення
- Створює випадкове речення з трьох списків слів
- Використовує функцію `random.choice()` для випадкового вибору
- Виводить згенероване речення

### Завдання 2: Аналіз тексту
- Читає текст з файлу `book.txt`
- Розраховує статистику тексту:
  - Кількість слів, що зустрічаються один раз
  - Кількість унікальних слів
  - Загальна кількість слів
  - Кількість символів (з пробілами та без)

### Завдання 3: Послідовності слів
- Аналізує текст з файлу `book.txt`
- Дозволяє знайти топ-10 найчастіших послідовностей слів
- Користувач задає довжину послідовності

## Вимоги
- Python 3.x
- Модуль `random`
- Модуль `collections`
- Файл `book.txt` у директорії `labs/lab4/`

## Використання
1. Запустіть файл `lab4.py` або використайте `cli.py` з командою run <номер_лабораторної>
2. Введіть номер завдання (1-3)
3. Дотримуйтесь інструкцій на екрані

## Приклад виконання
```
Введіть номер завдання (1-3): 2
Кількість слів, які зустрічаються один раз: 42
Кількість унікальних слів у тексті: 567
Кількість слів у тексті: 1024
Кількість символів з пробілами: 6543
Кількість символів без пробілів: 5621
```