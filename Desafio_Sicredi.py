                   #IMPORTAÇÕES

#importação do selenium e webdriver, para que seja possível abrir o navegador,
#selecionar elementos na página e etc.   

#importação do time, para evitar que o código bug e também para visualizar melhor
#a digitação das informações no formulário

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

import time

                     #COMEÇO DA AUTOMAÇÃO


#abaixo crio uma variável navegador, que recebe o driver do Google Chrome e logo #em se faço com que esta variável leia o link do formulário que será preenchido #desta forma, quando o programa for inicializado o navegador abrirá de forma #automatizada                      

navegador = webdriver.Chrome()
navegador.get("https://www.rpachallenge.com/")

#time.sleep(3) - é uma função vinda da Biblioteca time, isso faz com que
#a automação espere X segundos, neste caso são 3 segundos, usar o time
#é uma boa prática de programação pois evita que o código bugue tentando 
#automatizar todos os processos ao mesmo tempo

time.sleep(3)

#IMPORTAÇÃO da Biblioteca PANDAS para que eu consiga carregar os dados da minha base de dados que está em Excel
import pandas as pd

tabela = pd.read_excel("challenge.xlsx")
#atribuindo a "leitura" da base da dados a variável tabela 

tabela.columns = tabela.columns.str.strip()
#comando utilizando para retirar possíveis espaços que ficam entre as palavras
#pois esses espaços podem causar erros

#abaixo tem-se um for, que vai ir interando na tabela, selecionando os atributos
#que estão na mesma linha

for i, firstname in enumerate(tabela["First Name"]):
       lastname = tabela.loc[i, "Last Name"]
       companyname = tabela.loc[i, "Company Name"]
       roleincompany = tabela.loc[i, "Role in Company"]
       address = tabela.loc[i, "Address"]
       email = tabela.loc[i, "Email"]
       phonenumber = tabela.loc[i, "Phone Number"]

#abrindo o navegador
       navegador.get("https://www.rpachallenge.com/")

#no trecho abaixo o navegador já estara "aberto", atráves do By.CSS_SELECTOR é possível navegar pela página em busca de um campo contendo essa informa: "ng-flect-name="labelFirstName"" ", quando encontrada, o send_keys que é a função usada para escrever, irá digitar o valor presente na variável "firstname", que é a variável que contém o nome presente na base de dados  
 
       navegador.find_element(By.CSS_SELECTOR,'[ng-reflect-name="labelFirstName"]').send_keys(firstname)                   
       time.sleep(1)
        
       navegador.find_element(By.CSS_SELECTOR,'[ng-reflect-name="labelLastName"]').send_keys(lastname)
       time.sleep(1)
        
       navegador.find_element(By.CSS_SELECTOR,'[ng-reflect-name="labelCompanyName"]').send_keys(companyname)
                            
       time.sleep(1)
        
       navegador.find_element(By.CSS_SELECTOR,'[ng-reflect-name="labelRole"]').send_keys(roleincompany)
                              
       time.sleep(1)
        
       navegador.find_element(By.CSS_SELECTOR,'[ng-reflect-name="labelAddress"]').send_keys(address)
        
       time.sleep(1)
        
       navegador.find_element(By.CSS_SELECTOR,'[ng-reflect-name="labelEmail"]').send_keys(email)
        
       time.sleep(1)
       
       navegador.find_element(By.CSS_SELECTOR,'[ng-reflect-name="labelPhone"]').send_keys(str(phonenumber))
        
       time.sleep(1)
        
#neste trecho, o código navega pela página, e clica no campo de enviar

       navegador.find_element("xpath",'/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()