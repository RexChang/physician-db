"""
This program downloads a .crv file from the Physicians Compare Medicare 
Database.

Author: Emily Wu
Date: 1/13/16
"""
from splinter import Browser
import os
from selenium import webdriver
from os.path import expanduser
import time

#browser = Browser()

#do this if you want the file to save in the same folder
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", os.getcwd())
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
browser = webdriver.Firefox(firefox_profile = profile)


browser.get('https://data.medicare.gov/Physician-Compare/National-Downloadable-File/s63f-csi6')
browser.find_element_by_partial_link_text('Export').click()
browser.find_element_by_partial_link_text('CSV').click()

time.sleep(60)

#do this if you want to choose where the file is saving
"""
browser = Browser()
browser.visit('https://data.medicare.gov/Physician-Compare/National-Downloadable-File/s63f-csi6')
browser.find_link_by_text('Export').first.click()
browser.find_link_by_text('CSV').first.click()

time.sleep(60)

# This can be modified to go to wherever your computer saves downloaded files
path = os.path.expanduser("~")
os.chdir(path) 
os.chdir("Downloads/")

# This can be modified to move the csv file wherever you want to move it
os.system("mv National_Downloadable_File.csv ../Desktop/")
"""

browser.quit()
