import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from crawler import CrawledArticle


class ArticleFetcher:
    def __init__(self, base_url):
        self.url = base_url

    def fetch(self, limit_pages=0, limit_entries=0):
        url = self.url
        page_count = 0
        entry_count = 0

        while url is not None:
            if 0 < limit_pages <= page_count:
                break
            time.sleep(1)
            print("read data from " + url)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")
            nav = doc.select_one("div.navigation a")
            url = urljoin(url, nav.attrs["href"]) if nav is not None else None
            for card in doc.select(".card"):
                if 0 < limit_entries <= entry_count:
                    url = None
                    break
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin(url, card.select_one("img").attrs["src"])
                yield CrawledArticle(title, emoji, content, image)
                entry_count += 1

            page_count += 1
