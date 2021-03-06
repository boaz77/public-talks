
import datetime
from time import sleep
from selenium import webdriver

# kick off a firefox
driver = webdriver.Firefox()

# now as before
url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'
driver.get(url)
dateField = driver.find_element_by_id('UpdatedTextCDR')
print(dateField.text)

# or, cause it's python....
dt = datetime.datetime.strptime("-".join( [[str(i) for i in driver.find_element_by_id('UpdatedTextCDR').text.split(' ')[2].split('/')][j] for j in [2,0,1]] ),"%Y-%m-%d")

sleep(15)
driver.quit()