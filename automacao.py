import pyautogui
import pyperclip
import time
import pandas as pd
import openpyxl

pyautogui.PAUSE = 2 #tempo entre um comando e outro

#passo 1 - Entrar no sistema (entrar no link)
pyautogui.press('win') #comando para pressionar uma tecla
pyautogui.write('google') #comando para escrever um texto
pyautogui.press('enter')
pyautogui.write('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.press('enter')

time.sleep(5) #comando para 'atrasar' o programa no tempo que esta entre()

#Passo 2 - Navegar até o local do relatorio (entrar na pasta exportar)
pyautogui.click(414, 284, clicks=2)
time.sleep(2)

#Passo 3 - Fazer o download do relatório
pyautogui.click(436, 341)
pyautogui.click(1182, 180)
pyautogui.click(948, 584)
time.sleep(5)

#Passo 4 - Calcular os indicadores
#import pandas as pd
#import openpyxl

tabela = pd.read_excel(r'C:\Users\Daniel\Downloads\Vendas - Dez.xlsx')
#print(tabela)
faturamento = tabela ['Valor Final'].sum()
quantidade = tabela ['Quantidade'].sum()

#Passo 5 - Entrar no email
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(7)

#Passo 6 - Escrever e enviar o resultado via email
pyautogui.click(136, 196)
pyautogui.write('danielmrg+teste1@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy('Relatório de vendas')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('tab')

texto =f'''Prezados, bom dia

O faturamento de ontem foi de: R$ {faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

abs
Daniel'''

pyperclip.copy(texto)
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.hotkey('ctrl', 'enter')

#Para descobrir as coordenadas do mouse
"""time.sleep(5)
pyautogui.position()
print(pyautogui.position())"""