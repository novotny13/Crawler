from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

# Nastavení ChromeDriveru
chrome_path = "C:/Users/ADMIN/Pictures/chromedriver-win64/chromedriver.exe"
service = Service(chrome_path)
options = Options()
options.add_argument("--headless")  # Bez GUI, pokud chceš vidět, odstraň
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=service, options=options)

# Start URL Carvago
base_url = "https://carvago.com/cs/auta?page={}&sort=recommended&direction=desc"
index = 1
# Počet stránek, které chceme projet (můžeš změnit)
max_pages = 70

# Výsledek
cars_data = []

# Procházení stránek
for page in range(1, max_pages + 1):
    url = base_url.format(page+2000)
    print(f"Načítám stránku: {url}")
    driver.get(url)

    # Najdi všechny auta na stránce
    car_elements = driver.find_elements(By.CSS_SELECTOR, 'a[data-testid="feature.car.card_serp"]')

    car_links = []
    for elem in car_elements:
        href = elem.get_attribute("href")
        if href:
            car_links.append(href)

    print(f"Nalezeno {len(car_links)} odkazů na auta")

    # Pro každé auto
    for car_url in car_links:
        print(f"Zpracovávám {index}: {car_url}")
        driver.get(car_url)
        index = index + 1

        car_info = {}

        # Značka
        try:
            brand = driver.find_element(By.CSS_SELECTOR, 'div.css-7c1h2u a').text.strip()
            car_info['Značka'] = brand
        except NoSuchElementException:
            car_info['Značka'] = None

        # Model (nově přidané)
        try:
            model = driver.find_element(By.XPATH, '//p[text()="Model"]/ancestor::div[contains(@class, "css-7c1h2u")]//a').text.strip()
            car_info['Model'] = model
        except NoSuchElementException:
            car_info['Model'] = None

        # První registrace
        try:
            reg_date = driver.find_element(By.XPATH, '//span[contains(text(), "První registrace")]/following-sibling::p').text.strip()
            car_info['První registrace'] = reg_date
        except NoSuchElementException:
            car_info['První registrace'] = None

        # Cena
        try:
            price = driver.find_element(By.XPATH, '//dt[contains(text(), "Cena celkem")]/following-sibling::dd').text.strip()
            car_info['Cena'] = price
        except NoSuchElementException:
            car_info['Cena'] = None

        # Najeto
        try:
            mileage = driver.find_element(By.XPATH, '//span[contains(text(), "Najeto")]/following-sibling::p').text.strip()
            car_info['Najeto'] = mileage
        except NoSuchElementException:
            car_info['Najeto'] = None

        # Výkon
        try:
            power = driver.find_element(By.XPATH, '//span[contains(text(), "Výkon")]/following-sibling::p').text.strip()
            car_info['Výkon'] = power
        except NoSuchElementException:
            car_info['Výkon'] = None

        # Palivo
        try:
            fuel = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="desc-fuel-type"] p').text.strip()
            car_info['Palivo'] = fuel
        except NoSuchElementException:
            car_info['Palivo'] = None

        # Spotřeba
        try:
            consumption = driver.find_element(By.XPATH, '//span[contains(text(), "Spotřeba")]/following-sibling::p').text.strip()
            car_info['Spotřeba'] = consumption
        except NoSuchElementException:
            car_info['Spotřeba'] = None

        # Převodovka
        try:
            transmission = driver.find_element(By.XPATH, '//span[contains(text(), "Převodovka")]/following-sibling::p').text.strip()
            car_info['Převodovka'] = transmission
        except NoSuchElementException:
            car_info['Převodovka'] = None

        cars_data.append(car_info)

# Zavřít prohlížeč
driver.quit()

# Uložit do CSV
df = pd.DataFrame(cars_data)
df.to_csv("carvago_autaMID2.csv", index=False, encoding='utf-8-sig')

print("Hotovo! Data uložena do 'carvago_autaMujTest.csv'")