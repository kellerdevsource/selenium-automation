import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://chastite.com/bg/")

time.sleep(1)
manufacturer_elements = driver.find_element(By.ID, "homepage-manufacturer-select")
select_manufacturer = Select(manufacturer_elements)
series_elements = driver.find_element(By.ID, "homepage-model-series-select")
select_series = Select(series_elements)
models_elements = driver.find_element(By.ID, "homepage-models-select")
select_models = Select(models_elements)
engines_elements = driver.find_element(By.ID, "homepage-engines-select")
select_engines = Select(engines_elements)

def findoption(value,searchfield):
    for option in searchfield.options:
        if value.lower() in option.text.lower():
            searchfield.select_by_visible_text(option.text) 
            print(searchfield)
            break
    time.sleep(1)

manufacturer = "Merc"
series = "SLK"
model = "r170"
engine = "136"

findoption(manufacturer,select_manufacturer)
findoption(series,select_series)
findoption(model,select_models)
findoption(engine,select_engines)

select =  driver.find_element(By.ID,"homepage-select-button")
time.sleep(1)
select.send_keys(Keys.RETURN)

input("Натиснете Enter, за да затворите браузъра...")
driver.quit()