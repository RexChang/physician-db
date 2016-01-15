"""
This program downloads the procedure .xlsx files from the CMS website and 
converts them to .csv files.

Author: Diana Martschenko, Emily Wu
Date: 1/13/2016
"""
import os
import time
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
import zipfile
import csv
import xlrd

    
def main():
	"""
	Notes: masterlst, sheetlst, and linknames are subject to change
	"""
	masterlst = [['A', 'a'], ['B', 'b'], ['C', 'c'], ['D', 'd'], ['EFG', 'efg'], ['HIJ', 'hij'], ['KL', 'kl'], ['MN', 'mn'], ['OPQ', 'opq'], ['R', 'r'], ['S', 's'], ['TUVWX', 'tuvwx'], ['YZ and Numeric', 'yz']]
	sheetlst = ['A', 'B', 'C', 'D', 'EFG', 'HIJ', 'KL', 'MN', 'OPQ', 'R', 'S', 'TUVWX', 'YZ']
	
	#forces webpage to automatically download the file into the same folder as the program
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.download.folderList", 2)
	profile.set_preference("browser.download.dir", os.getcwd())
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv, application/zip")
	browser = webdriver.Firefox(firefox_profile = profile)

	#downloads each file from the CMS webpage.
	for i in range(len(masterlst)):
		link = 'Medicare Physician and Other Supplier PUF, CY2013, Microsoft Excel (.xlsx) Provider Last Name (%s)' % (masterlst[i][0])
		browser.get('https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Physician-and-Other-Supplier2013.html')
		browser.find_element_by_link_text(link).click()

		time.sleep(5)
		browser.find_element_by_xpath("//form[input/@name = 'agree']").click()

		Alert(browser).accept()

		time.sleep(120)

		#unzip file
		filename = 'Medicare_Provider_Util_Payment_PUF_%s_CY2013.zip' % (masterlst[i][1])
		path = os.path.expanduser("~")
		zip = zipfile.ZipFile(filename)
		zip.extractall(path+"/Desktop/Procedures") #modify to wherever you want the file to end up
		zip.close()
		letter = masterlst[i][1]

		path = os.path.expanduser("~")
		os.chdir(path+"/Desktop/NuFitMedia/Procedures") #modify to move to whatever directory the program is in
		filename2 = 'Medicare_Provider_Util_Payment_PUF_%s_CY2013.xlsx' % (masterlst[i][1])

		#convert xlsx to csv
		wrkbk = xlrd.open_workbook(filename2)
		sheetname = 'PUPD_PUF_%s' % (sheetlst[i])
		sheet = wrkbk.sheet_by_name(sheetname)
		newfile = 'Medicare(%s).csv' % (masterlst[i][0])
		newfile = open(newfile,'wb')
		wr = csv.writer(newfile, quoting = csv.QUOTE_ALL)
		for row in xrange(sheet.nrows):
			wr.writerow(sheet.row_values(row))
		newfile.close()

		#renames the file to correspond with makeTable.py
		os.system("mv Medicare(%s).csv 2013_Procedures_%s.csv" % (letter, letter))

		#deletes the zip file
		os.chdir(path+"/Desktop/NuFitMedia/physician-db") #modify to move to wherever the .zip file ended up
		os.system("rm Medicare_Provider_Util_Payment_PUF_%s_CY2013.zip" % letter)


	browser.quit()


main()

