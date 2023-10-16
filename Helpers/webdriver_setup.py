from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

def setup_chrome_driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

def setup_chrome_driver_with_retry(url, max_retries=3):
    options = Options()
    options.add_argument("--start-maximized")
    
    driver = None
    attempts = 0

    while attempts < max_retries:
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            break
        except WebDriverException as e:
            print(f"Erro durante a configuração do driver: {e}")
            attempts += 1
            if attempts == max_retries:
                print(f"Attempts excedeu o máximo de {max_retries}. Saindo...")
                break
            else:
                print(f"Tentando novamente... Tentativa {attempts} de {max_retries}")

    return driver
