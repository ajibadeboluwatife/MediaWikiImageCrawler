import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

url_base = "YOUR URL"

url = url_base + "YOUR URL"

print(url)

html = requests.get(url)

data = html.text

soup = BeautifulSoup(data)

image_info_links = list()

for link in soup.find_all('a'):
    href = link.get('href', "")
    if ".png" in href or '.jpg' in href:
        if not href in image_info_links:
            image_info_links.append(href)


image_list = list()
for image_info_link in image_info_links:
    image_info_html = requests.get(url_base + image_info_link)
    image_info_text = image_info_html.text
    image_info_soup = BeautifulSoup(image_info_text)
    for img in image_info_soup.find_all('img'):
        img_link = img.get('src', 'thumb')
        if not "thumb" in img_link:
            image_list.append(img_link)

for image in image_list:
    r = requests.get(url_base + image)
    i = Image.open(BytesIO(r.content))
    i.save(image.split('/')[-1])
