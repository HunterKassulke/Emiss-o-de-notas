import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select    


dados = {}
with open("dados.txt", "r", encoding="utf-8") as f:
    for linha in f:
        if ":" in linha:
            chave, valor = linha.strip().split(":", 1)
            dados[chave.strip().lower()] = valor.strip()

# 🔑 Variáveis extraídas
login = dados["login"]
senha = dados["senha"]
codatv = dados["codatv"]
servico = dados["servico"]
tomador = dados["tomador"]
municipio = dados["municipio"]
valor = dados["valor"]

drive = webdriver.Chrome()
drive.get('https://www.nfse.gov.br/EmissorNacional/Login')
drive.title

drive.find_element(By.ID, 'Inscricao').send_keys(login)
drive.find_element(By.ID, 'Senha').send_keys(senha)
acessar = drive.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
acessar.click()

drive.get('https://www.nfse.gov.br/EmissorNacional/DPS/Pessoas')
data = drive.find_element(By.ID, 'DataCompetencia')
brasil = drive.find_element(By.ID, 'Tomador_LocalDomicilio')
campotomador = drive.find_element(By.ID, 'Tomador_Inscricao')
data_hoje = datetime.today().strftime('%d/%m/%Y')
data.send_keys(data_hoje)
data.send_keys(Keys.TAB)
time.sleep(2)
label = drive.find_element(By.XPATH, "//label[contains(text(), 'Brasil')]")
label.click()
time.sleep(2)
campotomador.click
campotomador.send_keys(tomador)

data.send_keys(Keys.TAB)
avanc = drive.find_element(By.ID, 'btnAvancar')
time.sleep(2)
avanc.click()
# ENCONTRA O CAMPO NA PÁGINA E CLICA NO CAMPO MUNICÍPIO
select2_container = drive.find_element(By.CSS_SELECTOR, ".select2-selection")
select2_container.click()

time.sleep(1)

# AO CLICAR NO CAMPO ENCONTRA A BARRA DE PESQUISA QUE ABRE EMBAIXO E PESQUISA POR "BLU"
search_box = drive.find_element(By.CSS_SELECTOR, ".select2-search__field")
search_box.send_keys(municipio)

time.sleep(1)

# APÓS A PESQUISA CARREGAR OS ITENS DA LISTA SELECIONA A PRIMEIRA OPÇÃO
search_box.send_keys(Keys.ENTER)
combo = drive.find_element(By.CSS_SELECTOR, '[aria-labelledby="select2-ServicoPrestado_CodigoTributacaoNacional-container"]')
combo.click()

time.sleep(1)  # Aguarda abrir o dropdown

# Digita no campo de busca do Select2
coda = drive.find_element(By.CSS_SELECTOR, '[aria-controls="select2-ServicoPrestado_CodigoTributacaoNacional-results"]')
coda.send_keys(codatv)
time.sleep(1)
coda.send_keys(Keys.TAB)
label2 = drive.find_element(By.CSS_SELECTOR, '[class="cr-icon"]')
label2.click()
time.sleep(2)
descservico = drive.find_element(By.ID, 'ServicoPrestado_Descricao')
descservico.send_keys(servico)
avanc2 = drive.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary direita has-spin"]')
avanc2.click()
valores = drive.find_element(By.ID, 'Valores_ValorServico')
valores.send_keys(valor)
valores.send_keys(Keys.TAB)
avanc3 = drive.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary direita has-spin"]')
avanc3.click()
emitirnota = drive.find_element(By.ID, 'btnProsseguir')
emitirnota.click()
drive.close()