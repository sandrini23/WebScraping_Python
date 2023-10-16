import time
import requests
from bs4 import BeautifulSoup
import json
from selenium.webdriver.common.by import By
import math
import re
from database_operations import DatabaseOperations
from Helpers import webdriver_setup
import datetime

urlCVC = "https://www.cvc.com.br/passagens-aereas"
driver = webdriver_setup(urlCVC)

Origem  = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[1]')
Origem.click()
texto = "São Paulo"
Origem.send_keys(texto)
time.sleep(3)
SP = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/div/ul/div[1]/div[2]')
SP.click()
Destino = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[1]')
Destino.click()
DestinoClick = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div/div/ul/li/div[1]/input')
DestinoClick.click()
textoDestino = "Rio de Janeiro"
DestinoClick.send_keys(textoDestino)
time.sleep(3)
RioDeJaneiro = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div/div/ul/div[1]/div[2]/span')
RioDeJaneiro.click()
Data = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]')
Data.click()
Ida = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/table/tbody/tr[1]/td[4]')
Ida.click()
time.sleep(3)
Volta = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div/table/tbody/tr[1]/td[7]')
Volta.click()
Selecionar = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div[3]/div[2]/button')
Selecionar.click()
Buscar = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/button/span[1]')
Buscar.click()
time.sleep(3)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
voos = soup.find_all('div', class_=('cards-list'))

db_operations = DatabaseOperations()
for voo in voos:
    empresa = 'CVC'
    Companhia = voo.find('div', attrs={'data-test': 'flights-cluster'}).get_text().strip()
    PrecoTotal = voo.find('h5',attrs={'data-test="flights-cluster-pricebox-total-price"'}).get_text().strip()
    TaxaEmbarque = voo.find('span', class_=re.compile('MuiTypography-root')).get_text()
    TaxaServico = voo.find('p', class_='item-fare TAXES_AND_CHARGES').find('span', class_='price-wrapper').get_text() 
    TempoVoo = voo.find('span', class_='best-duration').get_text() 
    DataHoraIda = voo.find('span', class_='hour').get_text()
    DataHoraVolta = voo.find('span', class_='hour').get_text()
    DataInsercao= datetime.date.today().strftime('%Y-%m-%d') 
    voo_data = voo(empresa, Companhia, PrecoTotal, TaxaEmbarque, TaxaServico, TempoVoo, DataHoraIda, DataHoraVolta, DataInsercao
                   )
    db_operations.create_voo(voo_data)

db_operations.execute_procedure_and_export_to_excel()
    