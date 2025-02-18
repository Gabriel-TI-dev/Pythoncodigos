#Automação para rodar antivirus

import pyautogui
import time

#pyautogui.click-> clicar com o mouse
#pyautogui.press-> pressionar uma tecla
#pyautogui.write-> escrever

#o programa faz uma pausa á cada codigo executado
pyautogui.PAUSE = 5

#Passo 1-> Abrir as configurações
pyautogui.press("win")
pyautogui.write("config")
pyautogui.press("enter")

#tempo para pagina carregar por completo
time.sleep(10)

#Passo 2-> Localizar o antivirus e clicar para começar a execução
pyautogui.click(x=706, y=555)
pyautogui.click(x=21, y=316)
pyautogui.click(x=517, y=283)
pyautogui.click(x=406, y=346)

#comentario:
#Codigo de automação bem simples, para usar o antivirus do proprio windows, vcs podem ajustar no pc de vcs e se tiverem,
#ideias de melhorar podem dizer, continuar evoluindo é o meu objetivo!