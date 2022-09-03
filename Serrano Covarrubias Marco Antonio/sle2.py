import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 

from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_argument('--start-maximized')
opt.add_argument('--disable-extensions')

s = Service('E:/Python/chromedriver_win32/chromedriver.exe')

driver= webdriver.Chrome('E:/Python/chromedriver_win32/chromedriver.exe')

driver.get('https://www.olx.com.ec/autos_c378')

boton = driver.find_element(By.XPATH,'//button[@data-aut-id="btnLoadMore"]')

for i in range(3):
    try:
        boton.click()
        
        sleep(random.uniform(8.0,10.0))
        boton = driver.find_elements(By.XPATH,'//button[@data-aut-id="btnLoadMore"]')
    except:
        break
    
autos = driver.find_elements(By.XPATH,'//li[@data-aut-id="itemBox"]')

for auto in autos:
    precio =auto.find_element(By.XPATH,'.//span[@data-aut-id="itemPrice"]').text
    print(precio)
    descripcion =auto.find_element(By.XPATH,'.//span[@data-aut-id="itemTitle"]').text
    print(descripcion) 
