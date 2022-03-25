from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\Program Files\chromedriver.exe")
driver.get("https://passport.yandex.ru/auth/add?from=mail&origin=hostroot_homer_auth_L_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1")
assert "Авторизация" in driver.title
elem = driver.find_element_by_name("login")
time.sleep(2)
elem.send_keys("snow")
time.sleep(2)
elem.send_keys(Keys.RETURN)
time.sleep(2)
assert "No result found." not in driver.page_source
driver.close()
driver.quit()