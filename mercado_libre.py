import unittest
from selenium import webdriver

class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\Users\Reinaldo\Documents\Selenium\chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.mercadolibre.com/')

    def test_search_celular_xiaomi(self):
        driver = self.driver

        country = driver.find_element_by_id('BO')
        country.click()

        search_field = driver.find_element_by_xpath('/html/body/header/div/form/input')
        search_field.send_keys('Celulares Xiaomi')
        search_field.submit()

        categoria = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[1]/div[2]/div[1]/div/div/button')
        categoria.click()

        Precio_menor = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[1]/div[2]/div[1]/div/div/div/ul/li[2]')
        Precio_menor.click()

        products = {}

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text 
            price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div/div/span[1]').text 

            products[article_name] = price

        print(products)    


                                                         
     



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)          

