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

#Storing the tags and id of the different types of tickets
return_ticket = "//label[@id='flight-type-roundtrip-label-hp-flight']"
one_way_ticket = "//label[@id='flight-type-one-way-label-hp-flight']"
multi_ticket = "//label[@id='flight-type-multi-dest-label-hp-flight']"

def ticket_chooser(ticket):
    try:
        ticket_type = browser.find_element_by_xpath(ticket)
        ticket_type.click()
    except Exception as e:
        pass

#Choosing the departure and arrival countries
def dep_country_chooser(dep_country):
    fly_from = browser.find_element_by_xpath("//input[@id='flight-origin-hp-flight']")
    time.sleep(1)
    fly_from.clear()
    time.sleep(1.5)
    fly_from.send_keys('  ' + dep_country)
    time.sleep(1.5)
    first_item = browser.find_element_by_xpath("//a[@id='aria-option-0']")
    time.sleep(1.5)
    first_item.click()

browser.get('https://www.expedia.com/')
time.sleep(10)
ticket_chooser(return_ticket)
dep_country_chooser("France")