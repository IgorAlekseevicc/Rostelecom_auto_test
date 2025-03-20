import time

import pytest
from pytest_selenium import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
#Введите в переменные свои данные
number = '89133674749' #Номер телефона
password = '19862604Qq.' #Пароль
username = 'igoralekseevicc@gmail.com' #Почта
login = 'rtkid_1741101158974' #Логин, появится после регистрации в ЛК
personal_account = '670010831359 ' #Лицевой счет, появится после регистрации в ЛК

@pytest.fixture(autouse=True)
def driver():
    driver =webdriver.Chrome()
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=fc343b3b-9ff7-4786-bb30-e60caa7821cd&client_id=lk_b2c&tab_id=AbXXJJIfn5M')
    yield driver
    driver.quit()

def test_registered(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#kc-register'))).click()
    #Заполните своими данными
    time.sleep(120)
    driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > button').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app-header > div > div > div.app-header_navigation > a.app-header_navigation_link.active')))
    assert driver.find_element(By.CSS_SELECTOR, '#app-header > div > div > div.app-header_navigation > a.app-header_navigation_link.active')

def test_number_phone(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()

    driver.find_element(By.CSS_SELECTOR, '#username').send_keys(number)

    driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > div.rt-input-container > div > div.rt-input__action > svg').click()
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app-header > div > div > div.app-header_navigation > a.app-header_navigation_link.active')))
    assert driver.find_element(By.CSS_SELECTOR, '#app-header > div > div > div.app-header_navigation > a.app-header_navigation_link.active')

def test_Email(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn')))

    driver.find_element(By.CSS_SELECTOR, '#standard_auth_btn').click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-mail')))
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').click()

    driver.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app-header > div > div > div.app-header_navigation > a.app-header_navigation_link.active')))
    assert driver.find_element(By.CSS_SELECTOR, '#app-header > div > div > div.app-header_navigation > a.app-header_navigation_link.active')

def test_login(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-login'))).click()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys(login)

    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app-header > div > div > div.app-header_navigation > a.app-header_navigation_link.active')))
    assert driver.find_element(By.CSS_SELECTOR, '#app-header > div > div > div.app-header_navigation > a.app-header_navigation_link.active')

def test_personal_account(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-ls'))).click()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys(personal_account)

    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app-header > div > div > div.app-header_navigation > a.app-header_navigation_link.active')))
    assert driver.find_element(By.CSS_SELECTOR,'#app-header > div > div > div.app-header_navigation > a.app-header_navigation_link.active')

def test_time_code(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#address'))).send_keys(number)
    driver.find_element(By.CSS_SELECTOR, '#otp_get_code').click()
    time.sleep(20)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app-header > div > div > div.app-header_navigation > a.app-header_navigation_link.active')))
    assert driver.find_element(By.CSS_SELECTOR,'#app-header > div > div > div.app-header_navigation > a.app-header_navigation_link.active')

def test_negativ_number_phone(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()

    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('89999999999')

    driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > div.rt-input-container > div > div.rt-input__action > svg').click()
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_number_password(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()

    driver.find_element(By.CSS_SELECTOR, '#username').send_keys(number)

    driver.find_element(By.CSS_SELECTOR, '#page-right > div > div.card-container__wrapper > div > form > div.rt-input-container > div > div.rt-input__action > svg').click()
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('1111111111')

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_number_password(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-phone'))).click()

    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('89999999999')

    driver.find_element(By.CSS_SELECTOR,
                        '#page-right > div > div.card-container__wrapper > div > form > div.rt-input-container > div > div.rt-input__action > svg').click()
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('1111111111')

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_email(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn')))

    driver.find_element(By.CSS_SELECTOR, '#standard_auth_btn').click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-mail')))
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').click()

    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('111@gmail.com')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR,'#form-error-message')

def test_negativ_error_email(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn')))

    driver.find_element(By.CSS_SELECTOR, '#standard_auth_btn').click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-mail')))
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').click()

    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('111@gmailcom')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_email_password(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn')))

    driver.find_element(By.CSS_SELECTOR, '#standard_auth_btn').click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-mail')))
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').click()

    driver.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('1111111111')

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_email_and_password(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn')))

    driver.find_element(By.CSS_SELECTOR, '#standard_auth_btn').click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-mail')))
    driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').click()

    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('111@gmail.com')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('1111111111')

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_login(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-login'))).click()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('11111111')

    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_login_password(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-login'))).click()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys(login)

    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('11111111')
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_login_and_password(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-login'))).click()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('11111111')

    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('1111111111')
    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_personal_account(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-ls'))).click()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('111111111111')

    driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_persosnal_password(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-ls'))).click()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys(login)

    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('111111111')

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_personal_accaunt_and_password(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#standard_auth_btn'))).click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#t-btn-tab-ls'))).click()
    driver.find_element(By.CSS_SELECTOR, '#username').send_keys('111111111111')

    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('111111111')

    driver.find_element(By.CSS_SELECTOR, '#kc-login').click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_time_code_number(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#address'))).send_keys('89999999999')
    driver.find_element(By.CSS_SELECTOR, '#otp_get_code').click()
    time.sleep(20)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')

def test_negativ_time_email(driver):
    wait = WebDriverWait(driver, 60)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#address'))).send_keys('1111@gmail.com')
    driver.find_element(By.CSS_SELECTOR, '#otp_get_code').click()
    time.sleep(20)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#form-error-message')))
    assert driver.find_element(By.CSS_SELECTOR, '#form-error-message')