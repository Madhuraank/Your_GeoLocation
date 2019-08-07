#!/usr/bin

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

def getLocation():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")#  avoids the need to grant camera/microphone permissions.
    timeout = 20
    driver = webdriver.Chrome(executable_path =r'/usr/bin/chromedriver')# create a new instance of google chrome. This will help our program open an url in google chrome.

    driver.get("https://mycurrentlocation.net/")#access google chrome and open our website. By the way, chrome knows that you are accessing it through an automated software!
	
    wait = WebDriverWait(driver, timeout)#waits fr time specified at timeout
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')#XPath is the language used for locating nodes in an XML document. As HTML can be an implementation of XML (XHTML), Selenium users can leverage this powerful language to target elements in their web applications
# add the XPath of the element you want to grab and returning the elements.    
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    locationname = driver.find_elements_by_xpath('//*[@id="locationname"]')
    locationname = [x.text for x in locationname]
    locationname = str(locationname[0])
    driver.quit()
    return (latitude,longitude,locationname)
print(getLocation())
