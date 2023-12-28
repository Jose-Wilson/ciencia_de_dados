#                       Desafio
#   Queremos automatizar o backup de arquivos no sistema.

import pyautogui as ptg
from time import sleep

# mensagem de alerta
ptg.alert('O código vai começar! Não mexar enquanto o código está rodando.')
ptg.PAUSE = 0.5

#   abrir o google drive no computador
ptg.press('winleft')
ptg.write('chrome')
ptg.press('enter')
sleep(1)
ptg.write('https://drive.google.com/drive/u/0/home')
ptg.press('enter')

#   entrar na área de trabalho
ptg.hotkey('winleft', 'd')

#   cliclar no arquivo que eu quero fazer backup e arrastar ele
ptg.moveTo(x=31, y=276)
ptg.mouseDown()
ptg.moveTo(x=1339, y=713)

#   enquanto arrasto vou mudar par o google drive
ptg.hotkey('alt', 'tab')
sleep(1)

#   largar o arquivo no google drive
ptg.mouseUp()

#   esperar alguns segundos
sleep(5)
ptg.alert('O código acabou de rodar. Pode usar o computador novamente.')
