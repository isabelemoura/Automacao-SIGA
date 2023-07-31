# Passo a passo do projeto
# Passo 1: Entrar no sistema no SIGA
# Link para o sistema no SIGA: https://siga.cps.sp.gov.br/aluno/login.aspx
import pandas as pd
import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.5

pyautogui.press("win")

# Entrar no Edge
pyautogui.write("Edge")
pyautogui.press("enter")

# Abrir página anomina 
pyautogui.hotkey("ctrl", "shift", "n")
time.sleep(0.5)

# Entrar no SIGA
pyautogui.write("https://siga.cps.sp.gov.br/aluno/login.aspx")
pyautogui.press("enter")

# Escrever no Usuario
time.sleep(0.5) 
pyautogui.write("50456337830")
pyautogui.press("tab")
# Escrever a senha
pyautogui.write("Beluca@ads2021")
# Dar um TAB e pressionar o "CONFIRMAR" e entrar
pyautogui.press("tab")
pyautogui.press("enter")

# Entrar em Histórico (Grade)
time.sleep(0.5)
pyautogui.moveTo(x=144, y=680, duration=0.5)
pyautogui.click()
# Rolagem da tela 
time.sleep(10)
pyautogui.scroll(-5000)
time.sleep(10)
pyautogui.scroll(5000)

# Entrar em Horário
pyautogui.moveTo(x=102, y=726)
pyautogui.click()
time.sleep(5)
# Imprimir o horário de aulas
pyautogui.moveTo(x=1182, y=776)
pyautogui.click()
pyautogui.moveTo(x=133, y=930)
pyautogui.click()
# Vai abrir onde você quer salvar o arquivo...
time.sleep(5)
pyautogui.moveTo(x=190, y=437)
pyautogui.write("Horario de Aulas - Fatec SCS 2023.2")
pyautogui.moveTo(x=780, y=504)
pyautogui.click()

# Entrar em Notas parciais
pyautogui.moveTo(x=123, y=745)
pyautogui.click()
time.sleep(10)


# Entrar em Faltas parciais
pyautogui.moveTo(x=127, y=768)
pyautogui.click()
time.sleep(10)

# Entrar em Agenda >> Calendário de 
pyautogui.moveTo(x=111, y=810)
pyautogui.click()
time.sleep(10)