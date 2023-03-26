import os
import pathlib
import shutil
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.error

CURRENT_PATH = os.getcwd()

def create_project_folder():
    global FOLDER_NAME
    while True:
        FOLDER_NAME = input("Please enter your project name: ")
        if not os.path.exists(FOLDER_NAME):
            print(f"Creating {FOLDER_NAME}")
            os.makedirs(FOLDER_NAME)
            print(f"{FOLDER_NAME} has been created")
            break
        if os.path.exists(FOLDER_NAME):
            print("Folder already exists. Please enter a diffrent folder name.")

def get_website_name():
    global website
    global website_file
    website_file = "website.txt"
    with open(website_file, "a") as f:
        while True:
            website = input(
                "Please type the website (note: include \"https://\"): ")
            f.write(f"{website}\n")
            print(f"{website} has been added to {website_file}")
            choice = input("Do you want to add another website? (y/n): ")
            if choice.lower() != "y":
                break
    return website

def getting_tags():
    global tag
    global tag_filter
    while True:
        try:
            url = urlopen(website)
            tag_fetch = BeautifulSoup(url.read(), "html.parser")
            tag = input("Please input what tags you wish to dump (i.e. a,p,h1 etc.): ")
            tag_filter = tag_fetch.find_all(tag)
            break
        except (ValueError, urllib.error.URLError) :
            print("Please enter a vlaid url\n")
            print(f"{website} has been removed from queue.")
            get_website_name()

    return tag_filter

def dump_tag():
    with open("dump.txt", "a" , encoding="utf-8") as f :
        f.write(f"{tag_filter}\n\n")
        f.close()

def move_files():
    folder_location = pathlib.Path(rf"{CURRENT_PATH}\{FOLDER_NAME}")
    website_file_location = pathlib.Path(rf"{CURRENT_PATH}\website.txt")
    tag_file_location = pathlib.Path(rf"{CURRENT_PATH}\dump.txt")

    shutil.move(website_file_location, folder_location)
    shutil.move(tag_file_location, folder_location)



def main():
    create_project_folder()
    get_website_name()
    getting_tags()
    dump_tag()
    move_files()
    print(f"{tag} tags have been dumped.")

main()