from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


import pandas as pd


chrome_options = Options()
chrome_options.add_argument("--headless=new")

DRIVER = webdriver.Chrome(options=chrome_options)


TABLE = {
    "Name": [],
    "Card Type": [],
    "Attribute": [],
    "Type of Spell and Trap": [],
    "Type": [],
    "Level/Rank/Link": [],
    "Abilities/Other": [],
    "Cid": [],
    "Release Name": [],
    "Release Date": [],
    "Release Link": [],
}


FILTER = {
    "Card Type": [
        "Normal",
        "Effect",
        "Fusion",
        "Ritual",
        "Synchro",
        "Xyz",
        "Pendulum",
        "Link",
        "Spell",
        "Trap",
    ],
    "Attribute": [
        "LIGHT",
        "DARK",
        "WATER",
        "FIRE",
        "EARTH",
        "WIND",
        "DIVINE",
    ],
    "Type of Spell and Trap": [
        "Normal Spell",
        "Field Spell",
        "Equip Spell",
        "Continuous Spell",
        "Quick-play Spell",
        "Ritual Spell",
        "Normal Trap",
        "Continuous Trap",
        "Counter Trap",
    ],
    "Type": [
        "Spellcaster",
        "Dragon",
        "Zombie",
        "Warrior",
        "Beast-Warrior",
        "Beast",
        "Winged Beast",
        "Machine",
        "Fiend",
        "Fairy",
        "Insect",
        "Dinosaur",
        "Reptile",
        "Fish",
        "Sea Serphent",
        "Aqua",
        "Pyro",
        "Thunder",
        "Rock",
        "Plant",
        "Psychic",
        "Wyrm",
        "Cyberse",
        "Divine-Beast",
        "Illusion",
    ],
    "Level/Rank/Link": [str(i) for i in list(range(14))],  # 0 - 13
    "Abilities/Other": [
        "Toon",
        "Gemini",
        "Union",
        "Spirit",
        "Tuner",
        "Flip",
        "Special Summon",
    ],
    "Limit": [
        "Forbidden",
        "Limited",
        "Semi-Limited",
        "Unlimited",
    ],
}


def parse_table_by_row(row, url, release_name, release_date):

    name = row.find_element(By.CLASS_NAME, "box_card_name").text

    cid = row.find_element(By.CLASS_NAME, "link_value").get_attribute("value")
    cid_value = cid.split("&")[-1][4:]

    attribute = row.find_element(By.CLASS_NAME, "box_card_attribute").text

    TABLE["Name"].append(name)
    TABLE["Cid"].append(cid_value)

    TABLE["Release Name"].append(release_name)
    TABLE["Release Date"].append(release_date)
    TABLE["Release Link"].append(url)

    # === MONSTERS === #

    if attribute in FILTER["Attribute"]:

        TABLE["Attribute"].append(attribute)

        try:
            level = row.find_element(By.CLASS_NAME, "box_card_level_rank").text
        except:
            level = row.find_element(By.CLASS_NAME, "box_card_linkmarker").text
        level_value = level.split(" ")[-1]
        TABLE["Level/Rank/Link"].append(level_value)

        types = row.find_element(By.CLASS_NAME, "card_info_species_and_other_item").text

        types = types.strip("[").strip("]").strip(" ").split(" / ")

        TABLE["Card Type"].append(types[1])
        TABLE["Type"].append(types[0])

        if len(types) == 4:
            TABLE["Abilities/Other"].append(types[-2])
        else:
            TABLE["Abilities/Other"].append(None)

        TABLE["Type of Spell and Trap"].append(None)

    # === NOT MONSTERS === #
    else:
        if attribute == "SPELL":

            TABLE["Card Type"].append("Spell")

            try:
                types = row.find_element(By.CLASS_NAME, "box_card_effect").text

                if types == "Quick-Play":
                    types = "Quick-play Spell"

                elif types == "Continuous":
                    types = "Continuous Spell"

                elif types == "Field":
                    types = "Field Spell"

                elif types == "Equip":
                    types = "Equip Spell"

                elif types == "Ritual":
                    types = "Ritual Spell"

            except:
                types = "Normal Spell"

            TABLE["Type of Spell and Trap"].append(types)

        else:  # attribute == 'TRAP'

            TABLE["Card Type"].append("Trap")

            try:
                types = row.find_element(By.CLASS_NAME, "box_card_effect").text

                if types == "Continuous":
                    types = "Continuous Trap"

                elif types == "Counter":
                    types = "Counter Trap"

            except:
                types = "Normal Trap"

            TABLE["Type of Spell and Trap"].append(types)

        TABLE["Attribute"].append(None)
        TABLE["Type"].append(None)
        TABLE["Level/Rank/Link"].append(None)
        TABLE["Abilities/Other"].append(None)


with open("releases.csv", "r") as f:
    for i, line in enumerate(f):

        if i == 0:
            continue

        line = line.strip("\n").split(",")

        DRIVER.get(line[-1])

        table = DRIVER.find_element(By.ID, "card_list")
        rows = table.find_elements(By.CLASS_NAME, "t_row")

        print(line[0], line[2], len(rows))

        for each in rows:
            parse_table_by_row(each, line[-1], line[2], line[1])

DF = pd.DataFrame(TABLE)
DF.to_csv("AETable.csv")


DRIVER.quit()
