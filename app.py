#pip utilizado: pip install selenium openpyxl
#XPATH => tag[@atributo='valor]

from selenium import webdriver #abrir o nevegador
from selenium.webdriver.common.by import By #ira permitir interagir com o site
from time import sleep
import openpyxl #altomação de planilias
import os

driver = webdriver.Chrome()
#1 - Navegar até o site https://contabilidade-devaprender.netlify.app/
driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(5)

#2 - Digitar e-mail
email = driver.find_element(By.XPATH,"//input[@id= 'email']")
sleep(2)
email.send_keys('admin@contabilidade.com')
#3 - Digitar senha
senha = driver.find_element(By.XPATH,"//input[@id= 'senha']")
sleep(2)
senha.send_keys('contabilidade123456')
#4 - Clicar em entrar
btnEntrar = driver.find_element(By.XPATH,"//button[@id= 'Entrar']")
btnEntrar.click()
#5 - extrair as informações da planilia
caminho_absoluto = os.path.abspath("empresas.xlsx")
empresas = openpyxl.load_workbook(caminho_absoluto)
pagina_empresas = empresas['dados empresas']#pegar o nome da página

#6 - clicar no inputs preenchendo com as informações da planilha
for linha in pagina_empresas.iter_rows(min_row= 2):
    nome_empresa, email, telefone, endereco, cnpj, area_atuacao, quantidade_de_funcionarios, data_de_fundacao = linha

    driver.find_element(By.ID,'nomeEmpresa').send_keys(nome_empresa)
    sleep(1)
    driver.find_element(By.ID,'emailEmpresa').send_keys(email)
    sleep(1)
    driver.find_element(By.ID,'telefoneEmpresa').send_keys(telefone)
    sleep(1)
    driver.find_element(By.ID,'enderecoEmpresa').send_keys(endereco)
    sleep(1)
    driver.find_element(By.ID,'cnpj').send_keys(cnpj)
    sleep(1)
    driver.find_element(By.ID,'areaAtuacao').send_keys(area_atuacao)
    sleep(1)
    driver.find_element(By.ID,'numeroFuncionarios').send_keys(quantidade_de_funcionarios)
    sleep(1)
    driver.find_element(By.ID,'dataFundacao').send_keys(data_de_fundacao)
    sleep(1)

    #7 - Clicar em Cadastrar
    driver.find_element(By.ID,'Cadastrar').click()
    sleep(3)



#8 - Repitir os passos 5 e 6