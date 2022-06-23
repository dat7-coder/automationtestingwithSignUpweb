import unittest
from parameterized import parameterized
from Step_Signup import stepSignup
from dataSignupTest import readDatatest
from Verify_Signup import verifySignup
from customChromeDriver import customChrome

dataTests = readDatatest().dataTestSignUp()

class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('---Begin Test---')
        self.brower = customChrome()
        self.brower.get('http://127.0.0.1:8000/signup')

    def tearDown(self):
        self.brower.quit()
        print('---End Test---\n')

    @parameterized.expand(dataTests)
    def test_Signup(self, no, username, fname, lname, email, pass1, pass2,desiredResult, Message):
        stepSignup(self.brower).signup(username, fname, lname, email, pass1, pass2)
        self.assertIn(Message, verifySignup(self.brower).signup())

if __name__=='__main__':
    unittest.main()

