import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pyautogui

"""
download SnP options open contract from  barchart with expiration date that you can set 

"""

def main(): 

    EXPIRATION_DATE = '2022-08-19'
    EXAMPLE_BARCHART_EMAIL = 'jasper5@glaptopsw.com'
    EXAMPLE_BARCHART_PASSWORD = '7BXZmkOmRX7LxsxB0jmV875RXC8JaL'
    
    LINK = f"https://www.barchart.com/stocks/quotes/$SPX/options?expiration={EXPIRATION_DATE}-m&moneyness=allRows"


    # set the browser path 
    binary = FirefoxBinary("/usr/bin/firefox")
    browser = webdriver.Firefox(firefox_binary=binary)
    time.sleep(2)

    # browser maximize the window screen size
    browser.maximize_window()
    time.sleep(2)

    # Firefox go to barchart.com
    browser.get(LINK)
    time.sleep(15)

    # accept the conditions
    pyautogui.leftClick(1260 , 373)
    time.sleep(4)

    # click on LOGIN
    pyautogui.leftClick(1447,199)
    time.sleep(2)

    # click on USERNAME
    pyautogui.leftClick(793,334)
    # write email address
    pyautogui.write(EXAMPLE_BARCHART_EMAIL)  

    time.sleep(2)

    # click on PASSWORD
    pyautogui.leftClick(788,361)
    # scrivi PASSWORD
    pyautogui.write(EXAMPLE_BARCHART_PASSWORD)  
    time.sleep(5)

    # click on LOGIN
    pyautogui.leftClick(938,455)
    time.sleep(5)

    # click on DOWNLOAD
    pyautogui.leftClick(1580 , 638)

if __name__ == '__main__':
    main()
