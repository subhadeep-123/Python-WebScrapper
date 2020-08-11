import requests
from bs4 import BeautifulSoup
import csv

res = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(res.text, 'html.parser')
articles = soup.find_all('article')

with open("csvFile.csv", "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Title", "Links", "Date"])
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])
