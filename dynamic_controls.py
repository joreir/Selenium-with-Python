import unittest
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Reinaldo\Documents\Selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_xpath('//*[@id="content"]/ul/li[13]/a').click()


    def test_dynamic_controls(self):
        driver = self.driver
        
        check_button = driver.find_element_by_xpath('//*[@id="checkbox"]/input')
        check_button.click()

        remove_add_button = driver.find_element_by_xpath('//*[@id="checkbox-example"]/button')
        remove_add_button.click()

        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="checkbox-example"]/button')))
        remove_add_button.click()

        enable_disable_button = driver.find_element_by_xpath('//*[@id="input-example"]/button')
        enable_disable_button.click()

        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="input-example"]/button')))
        
        enable_to_write = driver.find_element_by_xpath('//*[@id="input-example"]/input')
        enable_to_write.send_keys('I Can Write in this moment')

        enable_disable_button.click()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2) 