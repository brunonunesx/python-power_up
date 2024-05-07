
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

time.sleep(5)

import pandas
pandas.read_csv('produtos.csv')
#3. Abrir/importar a base de dados de produtos para cadastrar

#4. cadastrat um produto 
#5. repetir isso tudo até acabar a lista de produtos   