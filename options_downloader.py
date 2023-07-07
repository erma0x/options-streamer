import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pyautogui

def main():
    EXPIRATION_DATE = '2022-08-19'
    EXAMPLE_BARCHART_EMAIL = 'jasper5@glaptopsw.com'
    EXAMPLE_BARCHART_PASSWORD = '7BXZmkOmRX7LxsxB0jmV875RXC8JaL'
    
    LINK = f"https://www.barchart.com/stocks/quotes/$SPX/options?expiration={EXPIRATION_DATE}-m&moneyness=allRows"

    binary = FirefoxBinary("/usr/bin/firefox")
    browser = webdriver.Firefox(firefox_binary=binary)
    time.sleep(2)

    browser.maximize_window()
    time.sleep(2)

    browser.get(LINK)
    time.sleep(15)

    pyautogui.leftClick(1260, 373)
    time.sleep(4)

    pyautogui.leftClick(1447, 199)
    time.sleep(2)

    pyautogui.leftClick(793, 334)
    pyautogui.write(EXAMPLE_BARCHART_EMAIL)
    time.sleep(2)

    pyautogui.leftClick(788, 361)
    pyautogui.write(EXAMPLE_BARCHART_PASSWORD)
    time.sleep(5)

    pyautogui.leftClick(938, 455)
    time.sleep(5)

    pyautogui.leftClick(1580, 638)

if __name__ == '__main__':
    main()
