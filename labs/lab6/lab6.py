import requests
from bs4 import BeautifulSoup
from collections import Counter


url = input("Введіть покликання: ")

try:
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")

    text = soup.get_text().lower()

    words = Counter(text.split())

    all_tags = soup.find_all(True)

    tag_name = []

    for tag in all_tags:
        tag_name.append(tag.name)

    tag_kilkist = Counter(tag_name)

    links = len(soup.find_all('a'))
    images = len(soup.find_all('img'))

    print("Частота слів (найбільш популярні):")
    for word, count in words.most_common(10):
        print(f"  {word}: {count}")
    print("\nЧастота HTML-тегів:")
    for tag, count in tag_kilkist.items():
        print(f"  {tag}: {count}")
    print(f"Кількість посилань: {links}")
    print(f"Кількість зображень: {images}")

except requests.exceptions.RequestException as e:
    print(f"Помилка при отриманні сторінки: {e}")