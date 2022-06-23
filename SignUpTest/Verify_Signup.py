from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from page_Signup import msg_result

class verifySignup:
    def __init__(self,driver):
        self.driver = driver
    
    def signup(self):
        self.waitSignupfinish()
        contentMessage = self.waitSignupfinish()
        print(contentMessage)

        return contentMessage
    
    def waitSignupfinish(self):
        print('[+] wait sign up finish')
        #return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, msg_result())))
        return self.driver.find_element(by=By.XPATH, value="//*[@id='flash-message']").text