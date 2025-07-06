from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os
import time

dados = {}
with open("dados.txt", "r", encoding="utf-8") as f:
    for linha in f:
        if ":" in linha:
            chave, valor = linha.strip().split(":", 1)
            dados[chave.strip().lower()] = valor.strip()

# 🔑 Variáveis extraídas
login = dados["login"]
senha = dados["senha"]

options = Options()
drive = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

drive.get('https://www.nfse.gov.br/EmissorNacional/Login')

drive.find_element(By.ID, 'Inscricao').send_keys(login)
drive.find_element(By.ID, 'Senha').send_keys(senha)
acessar = drive.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
acessar.click()

drive.get('https://www.nfse.gov.br/EmissorNacional/Notas/Emitidas')
time.sleep(3)

hoje = datetime.now().strftime("%d/%m/%Y")

linhas = drive.find_element(By.XPATH, "/html/body/div[1]/table/tbody")
linhas = linhas.find_elements(By.TAG_NAME,'TR')

for linha in linhas:
    try:
        data_emissao = linha.find_element(By.CSS_SELECTOR, "td").text.strip()
        

        if data_emissao == hoje:
            print(f"Nota com data de hoje encontrada: {data_emissao}")
            botao_opcoes = linha.find_element(By.CSS_SELECTOR, "td .glyphicon-option-vertical")
            botao_opcoes.click()
            time.sleep(1)

            linkPDF = linha.find_elements(By.TAG_NAME,"a")[5]
            linkPDF.click()
            time.sleep(2)


    except Exception as erro:
        print("Erro ao processar linha:", erro)

drive.quit()

        

