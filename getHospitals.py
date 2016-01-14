from splinter import Browser
from time import sleep
from selenium import webdriver
import os


def main():
    #with Browser() as b:
       
       profile = webdriver.FirefoxProfile()
       profile.set_preference("browser.download.folderList", 2)
       profile.set_preference("browser.download.manager.showWhenStarting", False)
       profile.set_preference("browser.download.dir", os.getcwd())
       profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
       b = webdriver.Firefox(firefox_profile = profile)
       b.get('https://data.medicare.gov/Hospital-Compare/Hospital-Value-Based-Purchasing-HVBP-Total-Perform/ypbt-wvdk')
       b.find_element_by_partial_link_text('Export').click()
       b.find_element_by_partial_link_text('CSV').click()
       
       #b.find_link_by_text('ok').first.click()
       #print link

       
       
       sleep(10)
       b.quit()
main()