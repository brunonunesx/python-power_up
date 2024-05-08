
#Passo a passo do projeto

#1. Abrir o sistemada empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login

#para istalalar: pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5

#pyautogui.click -> clicar como o mouse 
#pyautogui.write -> escrever um texto
#pyautogui.press -> pressionar uma tecla do teclado 
#pyautogui.hotKey -> apertar um conjunto de teclas ( ctrl C, ctrl V, Alt tab)

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no site do sistema
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#aqui pode ser que ele demora alguns segundos para carregar o site
time.sleep(3)

#2. fazer login
pyautogui.click(x=3668, y=611)
pyautogui.write('adjaljla')
pyautogui.press('tab') #passou para o botão de login
pyautogui.write('ldfkdal')

pyautogui.press("tab")
pyautogui.press('enter')

time.sleep(3)
#3. Abrir/importar a base de dados de produtos para cadastrar
import pandas as pd
tabela = pd.read_csv('produtos.csv')
#4. cadastra um produto 
for linha in tabela.index:
    pyautogui.click(x=3572, y=446)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = (str(tabela.loc[linha, 'obs']))
    if (obs != "nan"):
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)
#5. repetir isso tudo até acabar a lista de produtos   