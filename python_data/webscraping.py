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

matches = driver.find_elements(By.XPATH, '//tr[@data-ng-repeat="match in ::dtc.$scope.matches"]')
partido = []

for match in matches:
    partido.append(match.text)
driver.quit()

fecha = []
local = []
resultado = []
visitante = []

for i in range(0, len(partido)):
    temp = " "
    temp = str(partido[i]).strip(" ")
    temp = temp.split()
    fecha.append(temp[0])
    if temp[1] == 'Ath' or temp[1] == 'Real':
        local.append(temp[1] + " " + temp[2])
        resultado.append(temp[3] + temp[4] + temp[5])
        visitante.append(temp[6])
    else:
        local.append(temp[1])
        resultado.append(temp[2] + temp[3] + temp[4])
        if temp[5] == 'Ath'or temp[5] == 'Real':
            visitante.append(temp[5] + " " + temp[6])
        else:
            visitante.append(temp[5])

df = pd.DataFrame({'fecha':fecha,
'local':local,
'resultado':resultado,
'visitante':visitante})
df.to_csv('resultado.csv', index = False)