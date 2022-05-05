from bs4 import BeautifulSoup
import requests
site = requests.get("https://www.youtube.com/").content
soup = BeautifulSoup(site, "html.parser")
print(soup.prettify())
