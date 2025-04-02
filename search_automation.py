import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Стартираме Chrome браузъра
driver = webdriver.Chrome()
# Отиваме на Google
driver.get("https://www.google.com")
time.sleep(2)
try:
    # Изчакваме бутонът 'Приемане на всички' да стане кликаем
    accept_cookies_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Приемане на всички']"))
    )
    
    # Кликваме върху бутона
    accept_cookies_button.click()
    print("Бисквитките бяха приети.")
except Exception as e:
    print(f"Не беше намерен бутон за бисквитки или вече е приет. Грешка: {e}")

# Изчакваме полето за търсене да стане кликаемо
search_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "q"))
)
time.sleep(2)
# Въвеждаме текста в полето за търсене
searchword = "python"
for ch in searchword:
    search_box.send_keys(ch)
    time.sleep(1)
# Натискаме Enter
search_box.send_keys(Keys.RETURN)

# Изчакваме няколко секунди преди да затворим браузъра
driver.implicitly_wait(5)
input("Натиснете Enter, за да затворите браузъра...")
driver.quit()