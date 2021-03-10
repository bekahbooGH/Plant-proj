import requests
from bs4 import BeautifulSoup
import csv
import random
from urllib.parse import urljoin
import wget
import urllib

url = "https://www.ecowatch.com/10-incredible-plant-facts-you-didnt-know-1881847770.html"
req = requests.get(url)
src = req.content
soup = BeautifulSoup(src, 'html.parser')
plantglob = soup.find(class='body-description')
all_text = plantglob.get_text()
csv_file2 = open('plant_facts.csv', 'w')
csv_writer = csv.writer(csv_file2)
csv_writer.writerow(['plant_fact'])
csv_file.close()