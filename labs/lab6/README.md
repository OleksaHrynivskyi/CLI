# Лабораторна робота №6: Збір даних з веб-документів за допомогою мови Python

## Опис проекту
Інструмент для аналізу вмісту веб-сторінки з використанням бібліотек `requests` та `BeautifulSoup`.

## Функціональність
- Збирання статистики слів на сторінці
- Підрахунок частоти HTML-тегів
- Підрахунок кількості посилань та зображень

## Вимоги
- Python 3.x
- Бібліотеки:
  - `requests`
  - `beautifulsoup4`

## Встановлення залежностей
```bash
pip install requests beautifulsoup4
```

## Використання
1. Запустіть файл `lab6.py` або використайте `cli.py` з командою run <номер_лабораторної>
2. Введіть повне посилання на веб-сторінку
3. Отримайте детальну статистику

## Приклад виведення
```
Введіть покликання: https://example.com
Частота слів (найбільш популярні):
  the: 42
  a: 23
  in: 18

Частота HTML-тегів:
  div: 15
  p: 10
  span: 7

Кількість посилань: 12
Кількість зображень: 5
```

