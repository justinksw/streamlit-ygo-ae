from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless=new")

DRIVER = webdriver.Chrome(options=chrome_options)

with open("releases.csv", "r") as f:
    for i, line in enumerate(f):

        if i == 0:
            continue

        line = line.strip("\n").split(",")

        # print(line)

        DRIVER.get(line[-1])

        header = DRIVER.find_element(By.ID, "broad_title")
        header_name = header.find_element(By.TAG_NAME, "h1").text

        print(line[0], line[2] == header_name)
