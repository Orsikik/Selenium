# $x("//button[@id='ptm']") >>>> Xpath request
# $x("//b[text()='Product 1']/../../p")[0].inner.HTML >>>> complicated Xpath request

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located
from selenium.webdriver.common.keys import Keys
import time

#Set-up
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

browser = webdriver.Chrome(chrome_options=option,
                          executable_path=r'/home/ors/Dev/Selenium/drivers/chromedriver.exe')

alert = Alert(browser)


# LOGIN
browser.get("https://my.ausweis.io/ru/accounts/login/")
email_field = browser.find_element_by_id("id_login")
password_field = browser.find_element_by_id("id_password")
enter_button = browser.find_element_by_css_selector("button[type='submit']")

email_field.send_keys('i.orsyk@ausweis.io')
password_field.send_keys('PepsiCola1')
enter_button.click()


#Main >> profile
profile_options = browser.find_element_by_xpath("//a[@class='collapsed']")
edit_profile = browser.find_element_by_xpath("//a[text()='Edit Profile']")

profile_options.click()
wait = WebDriverWait(browser, 10)
wait.until(visibility_of_all_elements_located((By.LINK_TEXT, 'Edit Profile')))
edit_profile.click()


#Profile (change name)

name_field = browser.find_element_by_id('id_name')

# submit_button = browser.find_element_by_class_name("btn btn-fill btn-info")

name_field.clear()
name_field.send_keys('Igor Ausweis')
name_field.send_keys(Keys.ENTER)

phone_field = browser.find_element_by_id('id_phone')
phone_field.clear()
phone_field.send_keys(+380950000000)
enter_button = browser.find_element_by_css_selector("button[type='submit']")
enter_button.click()
#phone_field = browser.find_element_by_id('id_phone')
# name_field.send_keys(Keys.ENTER)

#TODO: Change profile photo