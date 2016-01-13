"""
This program downloads the procedure .xlsx files from the CMS website and 
converts them to .csv files.

Author: Emily Wu
Date: 1/13/2016
"""
from splinter import Browser
import os
from os.path import expanduser
import time
from selenium.webdriver.common.alert import Alert

browser = Browser()
browser.visit('https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Physician-and-Other-Supplier2013.html')
browser.find_link_by_text('Medicare Physician and Other Supplier PUF, CY2013, Microsoft Excel (.xlsx) Provider Last Name (A)').first.click()
browser.find_by_value("Accept").first.click()
alert = browser.get_alert()
alert().accept()
#browser.find_by_value("Accept").first.click()
#alert = browser.switch_to_alert()
#alert().accept()

time.sleep(60)

browser.quit()

