from selenium.webdriver.common.by import By 
from page_Signup import txt_username, txt_pass1, txt_pass2, txt_email, txt_fname, txt_lname, btn_Signup

class stepSignup:
    def __init__(self, driver):
        self.driver = driver
    def signup (self, username,fname,lname,email,pass1,pass2):
        print('[step] sign up')
        self.inputUserName(username)
        self.inputFname(fname)
        self.inputLname(lname)
        self.inputEmail(email)
        self.inputPassword1(pass1)
        self.inputPassword2(pass2)
        self.clickButtonSignup()

    def inputUserName(self, username):
        print('[+] Input username')
        self.get_txtUsername().send_keys(username)
    def get_txtUsername(self):
        return self.driver.find_element(By.XPATH, txt_username())
    
    def inputPassword1(self, password1):
        print('[+] Input password 1')
        self.get_txtPassword1().send_keys(password1)
    def get_txtPassword1(self):
        return self.driver.find_element(By.XPATH, txt_pass1())

    def inputPassword2(self, password2):
        print('[+] Input password 2')
        self.get_txtPassword2().send_keys(password2)
    def get_txtPassword2(self):
        return self.driver.find_element(By.XPATH, txt_pass2())

    def inputEmail(self, email):
        print('[+] Input email')
        self.get_txtEmail().send_keys(email)
    def get_txtEmail(self):
        return self.driver.find_element(By.XPATH, txt_email())

    def inputFname(self, fname):
        print('[+] Input fname')
        self.get_txtFname().send_keys(fname)
    def get_txtFname(self):
        return self.driver.find_element(By.XPATH, txt_fname())

    def inputLname(self, lname):
        print('[+] Input lname')
        self.get_txtLname().send_keys(lname)
    def get_txtLname(self):
        return self.driver.find_element(By.XPATH, txt_lname())

    def clickButtonSignup(self):
        print('[+] Click button signup')
        self.get_btnSignup().click()
    def get_btnSignup(self):
        return self.driver.find_element(By.XPATH, btn_Signup())


