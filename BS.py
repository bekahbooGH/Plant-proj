import requests
from bs4 import BeautifulSoup
import csv
import random
from urllib.parse import urljoin
import wget
import urllib

# locations = ["North Facing", "South Facing", "East Facing", "West Facing"]
# lighting = ["Bright Light", "Medium Light", "Low Light"]

url = "https://www.ecowatch.com/10-incredible-plant-facts-you-didnt-know-1881847770.html"
req = requests.get(url)

src = req.content

soup = BeautifulSoup(src, 'html.parser')

plantglob = soup.find(class='body-description')

all_text = plantglob.get_text()


csv_file2 = open('plant_facts.csv', 'w')

csv_writer = csv.writer(csv_file2)
csv_writer.writerow(['plant_fact'])

# def find_houseplants(indiv_houseplants):

#     plants_names_list = []
#     plants_descr_list = []
#     plants_pics_list = []

for listing in indiv_houseplants:
    # print(listing)
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
            # image_filename = wget.download(img_url)
            # image_filename > images
            # r = requests.get(img_url, stream=True)
            # if r.status_code == 200:
            #     r.raw.decode_content = True
            #     with open(filename, 'wb') as f:
            #         shutil.copyfileobj(r.raw,f)


           
            # image_urls.append(img_url)
            # print(pic_src1)
       
        
        print()




    csv_writer.writerow([plant_name, plant_descr, plant_lighting, plant_location, img_url])


csv_file.close()