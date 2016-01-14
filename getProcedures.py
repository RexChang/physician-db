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
from selenium import webdriver


profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", os.getcwd())
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
browser = webdriver.Firefox(firefox_profile = profile)

browser.get('https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Physician-and-Other-Supplier2013.html')
browser.find_element_by_link_text('Medicare Physician and Other Supplier PUF, CY2013, Microsoft Excel (.xlsx) Provider Last Name (A)').click()
browser.find_element_by_name("next").click()

#browser.find_by_text("Continue").first.click(

alert = browser.get_alert()
#alert.text
#alert.accept()
alert.dismiss()

#browser.find_by_value("Accept").first.click()
#alert = browser.switch_to_alert()
#alert().accept()

time.sleep(6)

browser.quit()

