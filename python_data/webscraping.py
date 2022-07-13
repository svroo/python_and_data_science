# Importacion de librerias
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd

# Definimos path de ruta del server
driver = webdriver.Chrome("C:\\Users\\hp\\Downloads\\chromedriver")
s = Service("C:\\Users\\hp\\Downloads\\chromedriver")

# Definimos la web
web = "https://www.adamchoi.co.uk/teamgoals/detailed"
driver.get(web)
sleep(5)

# Buscamos el boton de todos los partidos
allmatches = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
allmatches.click()
sleep(2)

dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text('Spain')
sleep(5)

matches = driver.find_elements(By.TAG_NAME, "tr")
partidos = []

for match in matches:
    partidos.append(match.text)
driver.quit()

df = pd.DataFrame({'partidos': partidos})
print(df)
df.to_csv('partidos.csv', index=False)