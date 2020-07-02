import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r'C:\Users\Reinaldo\Documents\Selenium\chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(20)

    def test_hello_world(self):
        driver=self.driver
        driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')

    def test_visit(self):
        driver=self.driver
        driver.get('https://www.techmeme.com/')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2 ,testRunner = HTMLTestRunner(output ='reportes',report_name='hello-world-report'))       

