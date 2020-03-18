import requests
from bs4 import BeautifulSoup as soup
import lxml
import pandas as pd
from urllib.parse import urlencode

BASE_URL = "https://www.imdb.com/find?"
HEADERS = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}


def crawl(query_type, query):
    f = {'s': query_type, 'q': query}
    search_url = (BASE_URL + urlencode(f))
    response = requests.get(search_url, headers=HEADERS)

    if "No results found for" in response.text:
        return None
    else:
        df = pd.read_html(search_url)
        return df[0][1]
