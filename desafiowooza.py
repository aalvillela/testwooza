import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class WoozaTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_title(self):
        """Validate title string"""
        driver = self.driver
        driver.get("http://www.celulardireto.com.br/")
        sleep(2)
        assert "Celular Direto" in driver.title

    def test_search(self):
        """Validate search box"""
        driver = self.driver
        driver.get("http://www.celulardireto.com.br/")
        elem = driver.find_element_by_name("phrase")
        elem.send_keys("notebook")
        elem.send_keys(Keys.RETURN)
        sleep(2)
        assert "Não foram encontrados resultados" in driver.page_source

    def test_check_plan(self):
        """Validate plans page"""
        driver = self.driver
        driver.get("http://www.celulardireto.com.br/")
        elem = driver.find_element_by_xpath('//*[@id="bgcolor-top-home"]/div[1]/div[2]/div[1]/div[2]/div[5]/a')
        elem.click()
        sleep(2)
        assert "Internet Banda Larga" in driver.title

    def test_compare_plan(self):
        """Validate compare page"""
        driver = self.driver
        driver.get("http://www.celulardireto.com.br/")
        elem = driver.find_element_by_xpath('//*[@id="bgcolor-top-home"]/div[1]/div[2]/div[2]/div[2]/div[5]/a')
        elem.click()
        sleep(2)
        assert "Compare os melhores planos" in driver.title

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
