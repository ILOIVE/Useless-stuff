import os
import time
import pathlib
import shutil
from bs4 import BeautifulSoup
from urllib.request import urlopen

SYS_PATH = os.getcwd()

def create_project_directory():
    global directory
    i = 0
    while i <= 0 :
        directory = input("Please enter your project name: ")
        directory_maker = os.path.join(SYS_PATH, f'{directory}')
        if not os.path.exists(directory):
            print("Creating said directory as " + directory)
            os.makedirs(directory_maker)
            time.sleep(1)
            print("Directory created")
            i += 1
            break
        if os.path.exists(directory):
            print("Folder name already exists! Please enter a different name")


def create_queue_and_visited_text_files():
    global queue
    queue = input("Please type the website (note: include \"https://\"): ")
    if not os.path.isfile(queue):
        make_text_file(queue)

def make_text_file(queue):
    maker = open("queue.txt", "x")
    maker = open("queue.txt", "w")
    maker.write(f"{queue}")
    maker.close()


    created_text_file_path = pathlib.Path(rf"{SYS_PATH}\queue.txt")
    move_to_this_file_path = pathlib.Path(fr"{SYS_PATH}\{directory}")

    shutil.move(created_text_file_path, move_to_this_file_path)

def get_website_html_content():
    content = urlopen(queue)
    beautiful_soup_content_fetcher = BeautifulSoup(content.read(), "html.parser")


def get_website_a_tags():
    tags = urlopen(queue)
    beautiful_soup_tag_fetcher = BeautifulSoup(tags.read(),"html.parser")
    beautiful_soup_tag_filter = beautiful_soup_tag_fetcher.findAll('a')
    make_html_a_tag_text_file(beautiful_soup_tag_filter)

def make_html_a_tag_text_file(beautiful_soup_tag_filter):
    make = open("a_tags.txt", "x", encoding="utf-8")
    make = open("a_tags.txt", "w", encoding="utf-8")
    make.write(f"{beautiful_soup_tag_filter}")
    make.close()
    os.makedirs("a_tags")

    a_tags_folder_location = pathlib.Path(fr"{SYS_PATH}\a_tags")
    a_tags_target_location = pathlib.Path(fr"{SYS_PATH}\{directory}")
    a_tags_file_location = pathlib.Path(fr"{SYS_PATH}\a_tags.txt")
    a_tags_file_target_location = pathlib.Path(fr"{SYS_PATH}\{directory}\a_tags")

    shutil.move(a_tags_folder_location, a_tags_target_location)
    shutil.move(a_tags_file_location, a_tags_file_target_location)



def main():
    create_project_directory()
    create_queue_and_visited_text_files()
    get_website_a_tags()

if __name__ == "__main__":
    main()


