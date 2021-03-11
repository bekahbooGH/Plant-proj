import requests
from bs4 import BeautifulSoup
import csv
import random
from urllib.parse import urljoin
import wget
import urllib

locations = ["North Facing", "South Facing", "East Facing", "West Facing"]
lighting = ["Bright Light", "Medium Light", "Low Light"]

url = "https://www.houseofplants.co.uk/indexofplants.php"
req = requests.get(url)
src = req.content
soup = BeautifulSoup(src, 'html.parser')
houseplants = soup.find(id='plant-index')
indiv_houseplants = houseplants.find_all(class_= "product-inner-box")
csv_file = open('plant_data_pics.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['plant_name', ' plant_descr', 'plant_lighting', 'plant_location',' pic_src'])

for listing in indiv_houseplants:
    plant_name = listing.find(class_="commonName").get_text()
    print(plant_name)
    plant_descr = listing.find(class_="description").get_text()
    print(plant_descr)
    plant_lighting = random.choice(lighting)
    print(plant_lighting)
    plant_location = random.choice(locations)
    print(plant_location)
    plant_pic_img = listing.findAll('img')
    for plant_pic in plant_pic_img:
        pic_src = plant_pic['src']
        if pic_src.endswith("jpg"):
            pic_src1 = pic_src
            filename = pic_src1
            # image_urls = []
            img_url = urljoin(url, pic_src1)
            print(img_url)
        print()

    csv_writer.writerow([plant_name, plant_descr, plant_lighting, plant_location, img_url])
csv_file.close()


# if __name =="__main__":
#     url = "https://www.houseofplants.co.uk/indexofplants.php"
#     scrape_data(url)







    