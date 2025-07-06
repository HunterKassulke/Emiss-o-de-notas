Projeto criado para emissão e baixa de notas no GOV.BR = https://www.nfse.gov.br/EmissorNacional/Login

# Emissor de Notas - Automação

Este projeto realiza a **emissão de notas fiscais** com base nos parâmetros fornecidos em um arquivo de texto (`dados.txt`). A data de emissão é sempre considerada como a **data atual**.

## ⚙️ Funcionamento

- Cada execução do executável `Emitirnota.exe` realiza a **emissão de uma nota fiscal**.
- Os parâmetros da nota devem ser informados previamente no arquivo `dados.txt`.
- A **data de emissão** será a **data atual do sistema**.
- A **baixa das notas** também será feita considerando a **data atual**.  
  Portanto, **execute a baixa somente após emitir a nota**.

## 📁 Estrutura esperada

- `Emitirnota.exe`: Executável responsável pela emissão da nota.
- `dados.txt`: Arquivo de entrada com os parâmetros necessários para a emissão.

## ⚠️ Atenção

- **NÃO execute `Emitirnota.exe` mais de uma vez** sem antes atualizar o conteúdo do `dados.txt`, para evitar a emissão duplicada de notas.
- Certifique-se de que os dados estejam corretos antes de cada execução.

## ✅ Exemplo de uso

1. Preencha o arquivo `dados.txt` com os dados da nota.
2. Execute `Emitirnota.exe` (duplo clique ou via terminal).
3. Aguarde a finalização da emissão.
4. Prossiga com o processo de **baixa** no mesmo dia.

---



