from selenium import webdriver

from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = ChromeOptions()
#esta opcao serve para nao fechar o navegador apos a execucao do script
opts.add_experimental_option("detach", True)
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)

driver.get("https://www.infomoney.com.br/")
 
sleep(2)

#find_element_by_id
dados1 = driver.find_element(By.ID,"high").text
 
print(dados1)

sleep(2)

driver.get("https://statusinvest.com.br/fundos-imobiliarios/hglg11")


#NOME DA PRIMEIRA ABA
original_window = driver.current_window_handle

#NOME DO FUNDO
#find_element_by_tag_name
dados2 = driver.find_element(By.TAG_NAME,"h1").text
 
print(dados2)

#VALOR ATUAL
#find_element_by_class_name
dados3 = driver.find_element(By.CLASS_NAME,"value").text
 
print(dados3)

#MIN 52 SEMANAS
#find_elements_by_class_name
dados4 = driver.find_elements(By.CLASS_NAME,"value")[1].text
 
print(dados4)

#P/VP
#find_elements_by_css_selector
dados5 = driver.find_element(By.CSS_SELECTOR,"#main-2 > div.container.pb-7 > div:nth-child(5) > div > div:nth-child(2) > div > div:nth-child(1) > strong").text

#NUMERO DE COTISTAS
print(dados5)

#find_element_by_xpath
dados6 = driver.find_element(By.XPATH,'//*[@id="main-2"]/div[2]/div[5]/div/div[6]/div/div[1]/strong').text
 
print(dados6)

clickable = driver.find_element(By.XPATH, '//*[@id="main-nav-nav"]/div/div/div/ul/li[2]/a')
ActionChains(driver)\
        .click(clickable)\
        .perform()


text_input = driver.find_element(By.XPATH, '//*[@id="main-search"]/div[1]/span[1]/input[2]')
ActionChains(driver)\
    .send_keys_to_element(text_input, '"abc"')\
    .perform()

driver.switch_to.new_window('tab')
sleep(2)


#NOME DA SEGUNDA ABA
second_window = driver.current_window_handle
driver.switch_to.window(original_window)



