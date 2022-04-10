import requests
from bs4 import BeautifulSoup
import re


def get_urls(url: list, lvl: int, arr:list):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all('a')
        for link in links:
            if link.has_attr('href') and link['href'].find('https://') != -1:
                res = re.split('/', link['href'])
                if f"https://{res[2]}" not in arr:
                    arr.append(f"https://{res[2]}")
        if lvl > 0:
            for item in arr:
                get_urls(item, lvl - 1, arr)
    except (requests.ConnectionError) as exception:
        print("No internet connection.")


if __name__ == "__main__":
    arr = []
    url = str(input("Вставьте ссылку - default(https://shatc.ru): "))
    lvl = int(input("Введите уровень: "))
    choose = str(input("Вывести в терминал(yes/no): "))
    if not url:
        url = "https://restoran.kz"
    get_urls(url, lvl, arr)
    if choose == 'yes':
        print(arr)
    else:
        with open("data.txt", "w") as file:
            for line in arr:
                file.write(line + '\n')
