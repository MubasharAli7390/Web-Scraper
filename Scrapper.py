from bs4 import BeautifulSoup as soup
import urllib.request
import requests
import os


path = "/home/mubashar/Desktop"
website = "https://replit.com/"




def scrap_links(document):
    i = 0
    for links in document.find_all('a'):
        href = links.get('href')
        link_file.write(href + "\n")
        print("Link Saved", i)
        i = i + 1
    return print("All " + str(i) + " Links Saved")



def scrap_images(document): 
    i = 0
    for image in document.find_all('img'):
        source = image.get('src')
        urllib.request.urlretrieve(source, path+"/Imgs/img{}".format(i))
        i = i+1
        print("Image saved", i)
    return print("All " + str(i) + "Images Saved")



def scrap_text(document):
        local_document = document
        for script_element in local_document(["script", "style"]):
            script_element.extract()
        text = local_document.get_text()
        text_file.write(text)
        print("All Text Saved")



def scrap_metadata(document):
    i = 0
    meta = document.head
    for elements in meta:
        meta_file.write(str(elements) + "\n")
        print("meta data saved", i)
        i = i + 1
    print("All " + str(i) + " meta data elements saved")

def make_image_dir():
    img_dir_exist = os.path.exists(path + "/Imgs")
    print(img_dir_exist)
    if img_dir_exist == False:
        os.mkdir(path + "/Imgs")
    return None


link_file = open(path + "/Links.txt", "a")
text_file = open(path + "/Text.txt","a")
meta_file = open(path + "/meta.txt","a")


web_data = requests.get(website)
if web_data.status_code != 200:
    print("The Website didn't respond")
else:
    parsed_data = soup(web_data.content, "html.parser")
    make_image_dir()
    scrap_links(parsed_data)
    scrap_images(parsed_data)
    scrap_text(parsed_data)
    scrap_metadata(parsed_data)
    print("Scrapping Completed")
    


          


