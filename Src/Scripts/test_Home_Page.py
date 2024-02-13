import sys
sys.path.append(sys.path[0] + "/...")

from Src.Base.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.HomePage import Home
import unittest
from selenium import webdriver

class Google_HomePage(WebDriverSetup):

    def test_Home_Page(self):
        driver = self.driver
        web_page_title = "Google"

        try:
            # Verifica se o título da página é igual ao esperado ("Google")
            if driver.title == web_page_title:
                print("Página carregada com sucesso.")
                self.assertEqual(driver.title, web_page_title)  # Garante que o título da página é o esperado
        except Exception as error:
            print(error + " - Ocorreu um erro. Algo de errado não está certo.")

        # Cria uma instância da classe HomePage para utilizar os métodos definidos nela
        home_page = Home(driver)

if __name__ == '__main__':
    unittest.main()
