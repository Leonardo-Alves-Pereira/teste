import sys
sys.path.append(sys.path[0] + "/...")
# import os
# Descomente se o exemplo acima gerar um erro de caminho relativo
# sys.path.append(os.getcwd())

import unittest
from time import sleep
from Src.Base.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.HomePage import Home

class Google_Search(WebDriverSetup):
    def test_GoogleSearch(self):
 
        driver = self.driver

        # Crie uma instância da classe para que possamos usar os métodos
        # na classe
        home = Home(driver)
        home.search_text.send_keys("Python é bom?")
        home.submit.submit()
        
        # Aguarde por 30 segundos para visualização manual
        # sleep(30)
 
if __name__ == '__main__':
    unittest.main()
