from time import sleep
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless=new")

DRIVER = webdriver.Chrome(options=chrome_options)


URL = "https://www.db.yugioh-card.com/yugiohdb/card_search.action?ope=2&cid="

with open("AETable.csv", "r") as f:

    csvreader = csv.reader(f)

    for i, line in enumerate(csvreader):

        if i == 0:
            continue

        cid = str(line[8])

        DRIVER.get(URL + cid)

        print(line[0], line[1], line[8])

        img = DRIVER.find_element(By.ID, "card_image_1")

        b = img.screenshot_as_png

        with open(f"./img/{line[8]}.jpg", mode="wb") as p:
            p.write(b)


DRIVER.quit()
