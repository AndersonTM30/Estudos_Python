from selenium import webdriver
from selenium.webdriver.common.by import By

# 1 - Criar um navegador webdriver
driver = webdriver.Chrome(executable_path='chromedriver.exe')

# 2 - Navegar até um site
driver.get('https://bpms.sistemafiea.com.br/orquestra')

# 3 Encontrar elementos
user = driver.find_element(By.ID, 'TxtLogin')
# 4 - Interagir com eles digitando ou clicando
user.click()
user.send_keys('t.mesha16')

password = driver.find_element(By.ID, 'TxtPassword')

password.click()
password.send_keys('01castlevania03@')

entrar = driver.find_element(By.ID, 'BtnLogin')
entrar.click()

driver.implicitly_wait(15)