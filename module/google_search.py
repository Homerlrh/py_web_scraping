import requests
from bs4 import BeautifulSoup


class get_news:
    def __init__(self):
        return

    def google_news(self, query):
        query = query.replace(" ", "+")
        url = f"https://google.ca/search?q={query}&num=30"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")
        link = soup.find_all("a", class_="BVG0Nb")
        return link


def get_url(str):
    return str.split("/url?q=", 1)[1].split("&sa", 1)[0]


first = get_news()
result = first.google_news("covid 19")
for title in result:
    print(get_url(title.attrs['href']))
