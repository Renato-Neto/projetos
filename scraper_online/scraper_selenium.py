import random
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
]

def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")

    # Ajuste os caminhos para o Firefox e o geckodriver no seu ambiente
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    service = Service(r"C:\Users\renat\geckodriver.exe")

    driver = webdriver.Firefox(service=service, options=options)
    return driver

def fetch_products_from_url(url):
    driver = setup_driver()
    try:
        driver.get(url)
        products_data = []
        
        # Espera até que os elementos de produtos estejam presentes
        products = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'product__details'))
        )
        
        for product in products:
            try:
                title = product.find_element(By.CLASS_NAME, 'product__title').text
                price = product.find_element(By.CLASS_NAME, 'product__price').text
                products_data.append({"title": title, "price": price})
            except NoSuchElementException:
                products_data.append({"error": "Informações de produto incompletas"})
        
        return products_data
    except TimeoutException:
        return {"error": "Timeout ao carregar a página"}
    finally:
        driver.quit()
