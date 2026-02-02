import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
import hashlib

URL = "https://scrap.tf/raffles"
OUT = "rss.xml"

r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

fg = FeedGenerator()
fg.title("scrap.tf raffles")
fg.link(href=URL)
fg.description("New raffles on scrap.tf")

for a in soup.select("a[href^='/raffles/']"):
    title = a.text.strip()
    link = "https://scrap.tf" + a["href"]
    uid = hashlib.md5(link.encode()).hexdigest()

    fe = fg.add_entry()
    fe.id(uid)
    fe.title(title)
    fe.link(href=link)

fg.rss_file(OUT)
