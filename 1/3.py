#!/usr/bin/env python3

import re
import requests
from bs4 import BeautifulSoup


class EmailRetrievier:
    def __init__(self, url: str):
        if not isinstance(url, str):
            raise TypeError("data_string must be a str type")

        content = requests.get(url).text
        self.html = BeautifulSoup(content, "html.parser").get_text()

    def retrieve(self):
        compiled = re.compile(r"[a-z0-9]+[\._]?[a-z0-9]+[@][\w+\.]+", re.UNICODE)
        return compiled.findall(self.html)


if __name__ == "__main__":
    url = "http://biologia.amu.edu.pl/page.php?id=wydzial-bos"
    parser = EmailRetrievier(url)
    res = parser.retrieve()
    print(res)
