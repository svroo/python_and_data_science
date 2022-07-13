# Importacion de librerias
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd

# Definimos variables que vamos a usar despues
partido = []
fecha = []
local = []
resultado = []
visitante = []

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

# Seleccionamos el boton de la region donde queremos los resultados en este caso Spain ya que el sitio esta en ingles
dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text('Spain')
sleep(5)

# Buscamos las columnas pertenecientes a la tabla de los partidos y la almacenamos en una variable
matches = driver.find_elements(By.XPATH, '//tr[@data-ng-repeat="match in ::dtc.$scope.matches"]')

# Cada renglon que haya en la variabla que asignamos previamente lo vamos a convertir a texto y lo vamos a agregar a una lista 
for match in matches:
    partido.append(match.text)
driver.quit()

# Empezamos a separar y almacenar los datos en columnas diferentes
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


# Se crea un data frame con el nombre de cada columna
df = pd.DataFrame({'fecha':fecha,
'local':local,
'resultado':resultado,
'visitante':visitante})

# Se guarda el dataframe
df.to_csv('resultado.csv', index = False)