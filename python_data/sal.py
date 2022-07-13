# Importacion de librerias
import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium import webdriver

# Definimos path de ruta del server
driver = webdriver.Chrome("C:\\Users\\hp\\Downloads\\chromedriver")
s = Service("C:\\Users\\hp\\Downloads\\chromedriver")
opt = webdriver.ChromeOptions()
opt.add_argument('--start-maximized')
opt.add_argument('--disable-extensions')

# Definimos variables que vamos a utilizar
user = "salazarvegarodrigo@yahoo.com.mx"
password = "R@dr!g033"

# Vamos a la página
driver.get('https://twitter.com/')

# esperamos a que termine de cargar
sleep(5) 

# Buscamos el boton de coordenada e intentamos dar click
btn = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div")
btn.click()

# mandamos llamar la funcion con los datos
correo = driver.find_element(By.CLASS_NAME, "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu")
for i in range(2):
    try:
        correo.send_keys(user)
        correo = driver.find_element(By.CLASS_NAME, "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu")
        correo.send_keys(user)
    except:
        break

btn2 = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
btn2.click()
sleep(random.uniform(2.00, 5.00))
