# Лабораторна робота №3: Робота з файлами у мові Python

## Опис проекту
Додаток для керування списками студентів з можливістю виконання основних операцій над даними.

## Функціональність
Програма пропонує наступні можливості:
1. Додавання нового студента
2. Перегляд списку студентів
3. Пошук студента за прізвищем
4. Сортування студентів за середнім балом
5. Видалення студента з групи
6. Робота з файлами різних навчальних груп

## Структура проекту
- `lab3.py`: Головний файл з меню та логікою роботи
- `function.py`: Допоміжні функції для роботи з файлами
- `*.txt`: Файли для збереження даних про студентів груп

## Вимоги
- Python 3.x

## Використання
1. Запустіть файл `lab3.py` або використайте `cli.py` з командою run <номер_лабораторної>
2. Оберіть групу для роботи
3. Виберіть бажану операцію з меню (1-6)

## Особливості
- Дані зберігаються у текстових файлах
- Підтримка створення нових файлів груп
- Проста навігація через консольне меню

## Приклад
```
Меню:
1. Додати студента
2. Відобразити студентів
3. Знайти студента
4. Сортувати студентів за середнім балом
5. Видалити студента
6. Вийти

Виберіть опцію (1-6): 1
Введіть групу (Англійською, example 11-KI) 11-KI
Введіть прізвище студента Петров
Введіть середній бал 95
```
