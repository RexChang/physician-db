"""
This program downloads a .crv file from the Physicians Compare Medicare 
Database.

Author: Emily Wu
Date: 1/13/16
"""
from splinter import Browser
import os
from os.path import expanduser
import time

browser = Browser()
#browser.open('https://data.medicare.gov/resource/s63f-csi6.csv')
browser.visit('https://data.medicare.gov/Physician-Compare/National-Downloadable-File/s63f-csi6')
browser.find_link_by_text('Export').first.click()
browser.find_link_by_text('CSV').first.click()

#time.sleep(60)

"""
path = os.path.expanduser("~")
os.chdir(path) 
os.chdir("Downloads/")
os.system("mv National_Downloadable_File.csv ../Desktop/")
"""

browser.quit()
