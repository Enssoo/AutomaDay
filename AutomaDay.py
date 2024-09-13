from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://graduacao.mackenzie.br/login/index.php")

#Primeiro click
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/section/div/div/div/div/div[2]/div/div[1]/a').click()

#Email
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "i0116")))
email = driver.find_element(By.ID,'i0116') 
email.send_keys("email@genérico.com.br")
driver.find_element(By.ID, 'idSIButton9').click()

#Senha
password = driver.find_element(By.ID, 'i0118')
password.send_keys('SenhaLegal123')
time.sleep(1.5)
driver.find_element(By.ID, 'idSIButton9').click()

#Manter conectado
time.sleep(0.5)
driver.find_element(By.ID, 'idSIButton9').click()

#Leitor de Horário
today = datetime.datetime.today().weekday()
time.sleep(0.5)

if (today == 0):#Segunda
    driver.get('https://graduacao.mackenzie.br/course/view.php?id=15717')
    driver.execute_script("window.open('https://graduacao.mackenzie.br/course/view.php?id=16110');")
    
elif (today == 1):#Terça
    driver.get('https://graduacao.mackenzie.br/course/view.php?id=16110')
    driver.execute_script("window.open('https://graduacao.mackenzie.br/course/view.php?id=19254');")
    
elif (today == 2):#Quarta
    driver.get('https://graduacao.mackenzie.br/course/view.php?id=15961')
    driver.execute_script("window.open('https://graduacao.mackenzie.br/course/view.php?id=15952');")
    
elif (today == 3):#Quinta
    driver.get ('https://graduacao.mackenzie.br/course/view.php?id=15961')
    driver.execute_script("window.open('https://graduacao.mackenzie.br/course/view.php?id=15952');")


elif (today == 4):#Sextou!!!
    driver.get('https://graduacao.mackenzie.br/course/view.php?id=14405')
    driver.execute_script("window.open('https://graduacao.mackenzie.br/course/view.php?id=13557');") 
