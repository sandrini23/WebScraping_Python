import time
import datetime
import requests
from bs4 import BeautifulSoup
import math
from selenium.webdriver.common.by import By
import re
from database_operations import DatabaseOperations
from Helpers import webdriver_setup

urlDecolar = "https://www.decolar.com/passagens-aereas/"
driver = webdriver_setup(urlDecolar)

Origem = driver.find_element (By.XPATH, '//*[@id="searchbox-sbox-box-flights"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[1]/div/input' )
Origem.click()
Origem.clear()
texto = "São Paulo"
Origem.send_keys(texto)
time.sleep(3)
OrigemClick = driver.find_element(By.XPATH, '/html/body/div[9]/div/div[1]/ul/li[1]')
OrigemClick.click()
Destino = driver.find_element (By.XPATH, '//*[@id="searchbox-sbox-box-flights"]/div/div/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/input')
Destino.click()
TextDestino = "Rio de Janeiro"
Destino.send_keys(TextDestino)
time.sleep(3)
DestinoClick = driver.find_element(By.XPATH, '/html/body/div[9]/div/div[1]/ul/li[1]')
DestinoClick.click()
Data = driver.find_element(By.XPATH, '//*[@id="searchbox-sbox-box-flights"]/div/div/div/div[3]/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div/input')
Data.click()
DataIda = driver.find_element(By.XPATH, '//*[@id="component-modals"]/div[1]/div[2]/div/div[2]/div[3]/div[1]')
DataIda.click()
time.sleep(3)
DataVolta = driver.find_element (By.XPATH, '//*[@id="component-modals"]/div[1]/div[2]/div/div[1]/div[3]/div[4]')
DataVolta.click()
Aplicar = driver.find_element(By.XPATH, '//*[@id="component-modals"]/div[1]/div[3]/div[1]/button')
Aplicar.click()
Buscar = driver.find_element(By.CSS_SELECTOR, '#searchbox-sbox-box-flights > div > div > div > div.sbox5-box-content--2pcCl.sbox5-flightType-roundTrip--fSJm8 > div.sbox5-button-container--1X4O8 > button')
Buscar.click()

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
voos = soup.find_all('div', class_=re.compile('results-content-wrapper'))

db_operations = DatabaseOperations()
for voo in voos:
    empresa = 'Decolar'
    Companhia = voo.find('span', class_='name').get_text().strip()
    PrecoTotal = voo.find('span', class_=re.compile('price')).get_text()
    TaxaEmbarque = voo.find('span', class_='price-wrapper').get_text()
    TaxaServico = voo.find('p', class_='item-fare TAXES_AND_CHARGES').find('span', class_='price-wrapper').get_text()
    TempoVoo = voo.find('span', class_='best-duration').get_text()
    DataHoraIda = voo.find('span', class_='hour').get_text()
    DataHoraVolta = voo.find('span', class_='hour').get_text()
    DataInsercao = datetime.date.today().strftime('%Y-%m-%d')
    voo_data = voo(empresa, Companhia, PrecoTotal, TaxaEmbarque, TaxaServico, TempoVoo, DataHoraIda,DataHoraVolta, DataInsercao)
    db_operations.create_voo(voo_data)

db_operations.execute_procedure_and_export_to_excel()
