from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://wiki.yandex.ru/homepage/sctipt-1/")
wait = WebDriverWait(driver, 600)
user_menu = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/nav/div[1]/a')))  # Укажите XPath для элемента, который появляется после логина
driver.get("https://wiki.yandex.ru/homepage/sctipt-1/")
edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/div/div[2]/div[4]/div/div/div/button/span')))
edit_button.click()
editor_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/main/div/div/div[2]/div/div[1]/div/div/div/div[2]/div')))
editor_field.clear()
editor_field.send_keys("Майкросов эдж говно бля.")
save_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div/main/div/div/div[2]/div/div[2]/div[2]/button[2]')
save_button.click()

input()