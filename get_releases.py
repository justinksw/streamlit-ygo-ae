from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


import pandas as pd


chrome_options = Options()
chrome_options.add_argument("--headless=new")

DRIVER = webdriver.Chrome(options=chrome_options)

URL = "https://www.db.yugioh-card.com/yugiohdb/card_list.action?request_locale=ae"


data = {
    "Date": [],
    "Name": [],
}


DRIVER.get(URL)

table_rows = DRIVER.find_elements(
    By.XPATH,
    "//div[@id='card_list_3']/div[@id='update_list']/div[@class='t_body']/div[@class='t_row']",
)

for i, row in enumerate(table_rows):

    data["Date"].append(row.find_element(By.CLASS_NAME, "time").text)
    data["Name"].append(row.find_element(By.TAG_NAME, "p").text)

df = pd.DataFrame(data)

df.to_csv("releases.csv")

DRIVER.quit()
