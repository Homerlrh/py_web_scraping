from .google_search import google
from .help_module.helper import Helper
import sys


class program_run:
    def __init__(self):
        self.options = {
            "0": self.new_user,
            "1": self.google_search,
            "2": self.yahooh_search,
            "3": self.quit
        }
        self.search1 = google()
        self.help = Helper()

    def run(self):
        print("""
        Web scraping tool (for news):
        0 . Create new user
        1 . Use google
        2 . Use yahooh
        3 . quit program""")
        option = input("\tChoose one to excute: ")
        if self.options.get(option):
            self.options.get(option)()
        else:
            print('Invalid option, try again')

    def new_user(self):
        pass

    def google_search(self):
        print(self.search1.connect())
        query = str(input("What you want to know about? : "))
        result = self.search1.get_top_stories(query)
        try:
            for k, v in zip(result['head'], result['url']):
                print(f"""Top stories: {k.string}\nRead more here: {self.help.url_extration(v.attrs['href'])}
                """)
        except:
            print("it seems like there is no top story for them, try a new topic")

    def yahooh_search(self):
        pass

    def quit(self):
        sys.exit(0)
