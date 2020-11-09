import requests
from bs4 import BeautifulSoup
import csv
import random

locations = ["North Facing", "South Facing", "East Facing", "West Facing"]
lighting = ["Bright Light", "Medium Light", "Low Light"]

url = "https://www.houseofplants.co.uk/indexofplants.php"
req = requests.get(url)

src = req.content

soup = BeautifulSoup(src, 'html.parser')

houseplants = soup.find(id='plant-index')

indiv_houseplants = houseplants.find_all(class_= "product-inner-box")

csv_file = open('plant_data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['plant_name', ' plant_descr', 'plant_lighting', 'plant_location',' pic_src'])

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
            print(pic_src1)


       
        
        print()




    csv_writer.writerow([plant_name, plant_descr, plant_lighting, plant_location, pic_src1])


csv_file.close()


# if __name =="__main__":
#     url = "https://www.houseofplants.co.uk/indexofplants.php"
#     scrape_data(url)







    