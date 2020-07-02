import unittest
from selenium import webdriver

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Reinaldo\Documents\Selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')

    def test_add_remove(self):
        driver = self.driver

        var_addRemove = driver.find_element_by_xpath('//*[@id="content"]/ul/li[2]/a')
        var_addRemove.click()

        elements_added = int(input("How many elements add : "))
        elements_removed = int(input("How many elements remove : "))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')


        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                remove_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                remove_button.click()
            except:
                print("Sorry but the script dont cant remove more than added")
                break

        if total_elements > 0:
            print(f'There are {total_elements} elements on the scren') 

        else:
            print('There are 0 elements on the scren')       





    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)          





