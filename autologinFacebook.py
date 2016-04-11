from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys


def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)
email_field = driver.find_element_by_id("email")
email_field.send_keys("youremail@xzy.xxx")
password_field = driver.find_element_by_id("pass")
password_field.send_keys("khong nho pass")
password_field.send_keys(Keys.RETURN)
