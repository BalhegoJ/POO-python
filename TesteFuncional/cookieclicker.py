from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Utilização do ChromeWebdriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Acessa o site do cookie clicker
driver.get("https://orteil.dashnet.org/cookieclicker/")

# ID do cookie clicável
cookie_id = "bigCookie"
# ID da quantidade total de cookies que foram clicados
cookies_id = "cookies"
# ID do preço do upgrade
product_price_prefix = "productPrice"
# ID do nome do upgrade
product_prefix = "product"

# Aguarda pelo menu seletor de idioma, para selecionar English
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

# Procura pelo primeiro elemento na pagina contendo English no XPATH e clica nele
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Aguarda pelo elemento cookie ser carregado na tela
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

# Aguarda mais 5 segundos e procura pelo primeiro elemento na pagina contendo o bigCookie como ID e clica nele
time.sleep(5)
cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()
    # Pega somente o número da string da quantidade de cookies
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    # Converte essa string para int, removendo a virgula
    cookies_count = int(cookies_count.replace(",", ""))

    # Verifica os 4 upgrades e compra o primeiro que aparecer disponível para a compra
    for i in range(4):
        # Busca pelo elemento de upgrade e remove as virgulas das strings
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        # Verifica se o elemento do preço do produto é uma string
        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        # Se a minha quantidade de cookies for >= ao preço do produto
        # Encontra o elemento do upgrade e compra ele
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break


