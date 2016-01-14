"""
This program downloads the procedure .xlsx files from the CMS website and 
converts them to .csv files.

Author: Diana Martschenko, Emily Wu
Date: 1/13/2016
"""
from splinter import Browser
import os
from os.path import expanduser
import time
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
import zipfile

masterlst = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd'], ['EFG', 'efg'], ['HIJ', 'hij'], ['KL', 'kl'], ['MN', 'mn'], ['OPQ', 'opq'], ['R', 'r'], ['S', 's'], ['TUVWX', 'tuvwx'], ['YZ and Numeric', 'yz']]
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.dir", os.getcwd())
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv/zip")
browser = webdriver.Firefox(firefox_profile = profile)

link = 'Medicare Physician and Other Supplier PUF, CY2013, Microsoft Excel (.xlsx) Provider Last Name (%s)' % (masterlst[0][0])
browser.get('https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Physician-and-Other-Supplier2013.html')
browser.find_element_by_link_text(link).click()
time.sleep(5) #accounts for webpage load time
browser.find_element_by_xpath("//form[input/@name = 'agree']").click()

Alert(browser).accept()

time.sleep(45)

filename = 'Medicare_Provider_Util_Payment_PUF_%s_CY2013.zip' % (masterlst[0][1])
path = os.path.expanduser("~")
#os.chdir(path)
#os.chdir("Downloads/") #modify to wherever the file downloads on your computer
zip = zipfile.ZipFile(filename)
zip.extractall(path+"/Desktop/NuFitMedia/Procedures") #modify to wherever you want the file to end up
zip.close()
os.chdir(path+"/Desktop/NuFitMedia/Procedures")
#license = "CMS_AMA_CPT_license_agreement.pdf"
os.system("rm CMS_AMA_CPT_license_agreement.pdf")
#os.chdir(path+"Desktop/NuFitMedia/physician-db")
#os.system("rm Medicare_Provider_Util_Payment_PUF_%s_CY2013.zip" % masterlst[0][1])

browser.quit()

