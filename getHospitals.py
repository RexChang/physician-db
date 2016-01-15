
"""
Program to download Hospital-Value-Based-Purchasing-HVBP-Total-Perform 
csv from medicare website
Author:Diana Martschenko
Date: 1/15/16
"""

from time import sleep
from selenium import webdriver
import os


def main():
       # change firefox settings to allow automatic download
       profile = webdriver.FirefoxProfile()
       profile.set_preference("browser.download.folderList", 2)
       profile.set_preference("browser.download.manager.showWhenStarting", False)
       profile.set_preference("browser.download.dir", os.getcwd())
       profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
       b = webdriver.Firefox(firefox_profile = profile)

       #download the csv file
       b.get('https://data.medicare.gov/Hospital-Compare/Hospital-Value-Based-Purchasing-HVBP-Total-Perform/ypbt-wvdk')
       b.find_element_by_partial_link_text('Export').click()
       b.find_element_by_partial_link_text('CSV').click()
       
 
       
       sleep(10)
       b.quit()
main()