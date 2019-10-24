# Selenium (for accessing websites and automation testing)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Pandas (we will mainly just used Pandas for structuring our data):
import pandas as pd

# Time and date-time (for using delays and returning current time we will see why later)
import time
import datetime

# connecting to our email and sending our message
import smtplib
from email.mime.multipart import MIMEMultipart

browser = webdriver.Chrome(executable_path=r"C:\Users\joel.bushiri\PycharmProjects\webScrap\chromedriver.exe")

def dep_country_chooser(dep_country):
    fly_from = browser.find_element_by_xpath("//div[@id='flight-origin-hp-flight']")
    time.sleep(1)
    fly_from.clear()
    time.sleep(1.5)
    fly_from.send_keys('  ' + dep_country)
    time.sleep(1.5)
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    time.sleep(1.5)
    first_item.click()