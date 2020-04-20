import requests
from bs4 import BeautifulSoup
from newsmodule import Connect


class google(Connect):
    def __init__(self):
        self.source = "Google"
        self.url = "https://google.ca/search?q=%s&num=30"

    def connect(self):
        s = super().connect()
        return (s % self.source)

    # get the top stories
    def get_top_stories(self, query):
        query = query.replace(" ", "+")
        response = requests.get(self.url % query)
        soup = BeautifulSoup(response.text, "html.parser")
        span = soup.find_all("span", class_="rQMQod Xb5VRe")
        link = soup.find_all("a", class_="BVG0Nb")
        return {"head": span, "url": link}

    def get_link_only(self, query):
        query = query.replace(" ", "+")
        response = requests.get(self.url % query)
        soup = BeautifulSoup(response.text, "html.parser")
        link = soup.find_all("a", class_="BVG0Nb")
        return link

    def get_search_title(self):
        # query = query.replace(" ", "+")
        response = requests.get(self.url % "ice")
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")
        link = soup.find_all("div", class_="r")
        return link


if __name__ == '__main__':
    first = google()
    for k in first.get_search_title():
        print(k)
