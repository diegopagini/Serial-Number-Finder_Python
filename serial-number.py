import re
import os
import time
import datetime
from pathlib import Path
import math

init = time.time()
url = 'C:\\Users\\my_user\\desktop\\directory'
my_pattern = r'N\D{3}-\d{5}'
today = datetime.date.today()
found_numbers = []
found_files = []


def search_number(file, pattern):
    this_file = open(file, 'r')
    text = this_file.read()
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''


def create_list():
    for folder, sub_folder, file in os.walk(url):
        for f in file:
            result = search_number(Path(folder, f), my_pattern)
            if result != '':
                found_numbers.append(result.group())
                found_files.append(f.title())


def show_all():
    index = 0
    print("-" * 50)
    print(f"Search date: {today.day}/{today.month}/{today.year}")
    print("\n")
    print("File\t\t\tSerial number:")
    print("-------\t\t\t-------")
    for f in found_files:
        print(f"{f}\t{found_numbers[index]}")
        index += 1
    print("\n")
    print(f"Founded numbers: {len(found_numbers)}")
    end = time.time()
    duration = end - init
    print(f"Duration of the search: {math.ceil(duration)}")


create_list()
show_all()

