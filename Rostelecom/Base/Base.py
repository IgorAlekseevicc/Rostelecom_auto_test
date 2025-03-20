from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
def driver():
    driver =webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=AbXXJJIfn5M')
    yield driver
    driver.quit()
wait = WebDriverWait(driver, 30)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn')))