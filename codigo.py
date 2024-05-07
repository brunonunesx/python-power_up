
#Passo a passo do projeto

#1. Abrir o sistemada empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login

#para istalalar: pip install pyautogui
import pyautogui

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




#2. fazer login 
#3. Abrir/importar a base de dados de produtos para cadastrar
#4. cadastrat um produto 
#5. repetir isso tudo até acabar a lista de produtos   