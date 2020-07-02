import unittest
from selenium import webdriver

class DynamicElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Reinaldo\Documents\Selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://the-internet.herokuapp.com/")


    def test_name_elements(self):
        driver = self.driver
        var_disapering_elements = driver.find_element_by_link_text("Disappearing Elements")
        var_disapering_elements.click()

        options =  []
        menu = 5
        tries = 1

        while len(options)<5:
            options.clear()

            for i in range(menu):

                try:
                    options_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    options.append(options_name.text)
                    print(options)
                except:
                    print(f"Option number { i + 1 } is NOT FOUND")
                    tries = tries + 1
                    driver.refresh()

        print(f"finish in {tries} tries")            

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)        