import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome

import time
from time import sleep
import warnings
import urllib3

class WebDriverSetup(unittest.TestCase):

    def setUp(self):
        # Configuração inicial antes da execução de cada teste
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)  # Opção para manter o Chrome aberto após o término do teste
        servico = Service(ChromeDriverManager().install())  # Configuração do serviço do ChromeDriver usando o WebDriver Manager
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # Desabilita os avisos de solicitação insegura
        self.driver = webdriver.Chrome(service=servico, options=opts)  # Inicializa o WebDriver do Chrome
        self.driver.implicitly_wait(10)  # Define um tempo de espera implícito de 10 segundos para localizar elementos na página

    def tearDown(self):
        # Limpeza após a execução de cada teste
        if self.driver is not None:
            print("Limpeza do ambiente de teste")
            self.driver.close()  # Fecha a janela do navegador
            self.driver.quit()   # Encerra a instância do WebDriver
