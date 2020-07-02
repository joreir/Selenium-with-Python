import unittest
from selenium import webdriver 

class Typos(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Reinaldo\Documents\Selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element_by_link_text("Typos").click()


    def test_find_typo(self):
        driver = self.driver

        paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
            text_to_check = paragraph_to_check.text
            driver.refresh()

        while not found:
            if text_to_check == correct_text:
                tries+=1
                driver.refresh()
                found = True

        self.assertEqual(found,True)            
        
        print(f"It took to selenium to found the correct paragrah {tries} tries")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2) 