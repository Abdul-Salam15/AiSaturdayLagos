import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    for quote, author in zip(quotes, authors):
        writer.writerow([quote.text, author.text])
print("Scraping complete! Data saved to quotes.csv")
