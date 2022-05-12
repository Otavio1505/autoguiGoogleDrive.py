#Abrir o navegador, abrir o google drive e armazenar o arquivo de minha escolha
import time
import pyautogui as p


p.hotkey('win','d')
time.sleep(0.5)
p.press('win')
time.sleep(2)
p.write('Microsoft Edge')
p.press('enter')
p.hotkey('win','up')

time.sleep(1.5)
p.write('drive.google.com/drive/my-drive')
p.press('enter')
time.sleep(6)
p.hotkey('win','left')
p.press(['esc'])
p.moveTo(x=1314, y=25)
p.drag(xOffset=-770,yOffset=480,duration=1)
time.sleep(1)
p.mouseUp()

time.sleep(8)









