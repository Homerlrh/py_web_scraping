import requests
from bs4 import BeautifulSoup


class get_news:
    def __init__(self):
        return

    def google_news(self, query):
        query = query.replace(" ", "+")
        url = f"https://google.ca/search?q={query}&num=30"
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")
        link = soup.find_all("a")
        return title


first = get_news()
result = first.google_news("covid 19")
print(result.__len__())

for title in result:
    print(title)
