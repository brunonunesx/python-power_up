
#Passo a passo do projeto

#1. Abrir o sistemada empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login

#para istalalar: pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 1.5

#pyautogui.click -> clicar como o mouse 
#pyautogui.write -> escrever um texto
#pyautogui.press -> pressionar uma tecla do teclado 
#pyautogui.hotKey -> apertar um conjunto de teclas ( ctrl C, ctrl V, Alt tab)

# abrir o navegador (chrome)
time.sleep(2)
pyautogui.press("win")
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
# entrar no site do sistema
pyautogui.write('https://discord.com/channels/1228404913705451612/1238509258996453438')
pyautogui.press('enter')
#aqui pode ser que ele demora alguns segundos para carregar o site
time.sleep(2)
while True:
    pyautogui.click(x=482, y=806)
    pyautogui.write('Dei um like no meu projeto de previsoes https://discord.com/channels/1228404913705451612/1228406162618060913/1238686305756385331 https://github.com/brunonunesx/projeto_imers-o_IAobg ')
    pyautogui.press('enter')
    
    time.sleep(120)
    pyautogui.click(x=482, y=806)
    pyautogui.write('ta feito, boa sorte a todos 🚀🚀 https://discord.com/channels/1228404913705451612/1228406162618060913/1238686305756385331')
    pyautogui.press('enter')

    time.sleep(180)
    pyautogui.click(x=482, y=806)
    pyautogui.write('vota la, obghttps://discord.com/channels/1228404913705451612/1228406162618060913/1238686305756385331')
    pyautogui.press('enter')

    time.sleep(300)
    pyautogui.click(x=482, y=806)
    pyautogui.write('vota la, retribuo o voto, vlw https://discord.com/channels/1228404913705451612/1228406162618060913/1238686305756385331 https://github.com/brunonunesx/projeto_imers-o_IA')
    pyautogui.press('enter')

    time.sleep(420)
'''
time.sleep(3)
#3. Abrir/importar a base de dados de produtos para cadastrar
import pandas as pd ta uma fora la, obg desejo boa sorte a
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
#5. repetir isso tudo até acabar a lista de produtos'''