from lib2to3.pgen2 import driver
from selenium.webdriver.chrome.options import Options 
from selenium import webdriver

def customChrome():
    option = Options()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(chrome_options=option, executable_path=r'D:\Temp\chromedriver_win32\chromedriver.exe')
    driver.implicitly_wait(3)
    driver.maximize_window()

    print('[Open browser]')
    return driver
