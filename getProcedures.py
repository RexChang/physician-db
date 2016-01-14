"""
This program downloads the procedure .xlsx files from the CMS website and 
converts them to .csv files.

Author: Diana Martschenko, Emily Wu
Date: 1/13/2016
"""
#from splinter import Browser
import os
#from os.path import expanduser
import time
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
import zipfile
import csv
import xlrd


"""
def excel_to_csv():
	wrkbk = xlrd.open_workbook('')
    sheet = wrkbk.shee_by_name('Sheet1')
    csv_file = open('Medicare(A)','wb')
    wr = cs.writer(Medicare(A), quoting = csv.QUOTE_ALL)

    for row in xrange(sheet.nrows):
    	wrkbk.writerow(sheet.row_values(row))
    Medicare(A).close()
    """

def unzipFile(filename):
	"""
	This function unzips the newly downloaded file.
	"""
	path = os.path.expanduser("~")
	#os.chdir(path)
	#os.chdir("Downloads/") #modify to wherever the file downloads on your computer
	zip = zipfile.ZipFile(filename)
	zip.extractall(path+"/Desktop/NuFitMedia") #modify to wherever you want the file to end up
	zip.close()
	os.chdir(path+"/Desktop/NuFitMedia/Procedures")
	os.system("rm CMS_AMA_CPT_license_agreement.pdf")
	os.chdir(path+"/Desktop/NuFitMedia/physician-db") #return to correct directory

def main():

	masterlst = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd'], ['EFG', 'efg'], ['HIJ', 'hij'], ['KL', 'kl'], ['MN', 'mn'], ['OPQ', 'opq'], ['R', 'r'], ['S', 's'], ['TUVWX', 'tuvwx'], ['YZ and Numeric', 'yzandnumeric']]

	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.download.folderList", 2)
	profile.set_preference("browser.download.dir", os.getcwd())
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv/zip")
	browser = webdriver.Firefox(firefox_profile = profile)

	link = 'Medicare Physician and Other Supplier PUF, CY2013, Microsoft Excel (.xlsx) Provider Last Name (%s)' % (masterlst[0][0])
	browser.get('https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Physician-and-Other-Supplier2013.html')
	browser.find_element_by_link_text(link).click()

	time.sleep(5)
	browser.find_element_by_xpath("//form[input/@name = 'agree']").click()

	Alert(browser).accept()

	time.sleep(45)

	filename = 'Medicare_Provider_Util_Payment_PUF_%s_CY2013.zip' % (masterlst[0][1])

	unzipFile(filename)
	#excel_to_csv():

	browser.quit()


main()

