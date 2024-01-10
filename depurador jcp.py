import pyautogui
import pyperclip
import time
import datetime

# instalar pip install pyautogui, pyperclip, time, datetime, timedelta, comando (python -m pip install --upgrade)

pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
link = "https://admin-atibaia.guichepass.com.br/"
pyperclip.copy(link)
pyautogui.hotkey('ctrl','t')
pyautogui.write('https://admin-atibaia.guichepass.com.br/') #abrir sitema do Gpass
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x = 766, y = 572 )
time.sleep(3)
pyautogui.click(x = 1054, y = 197)
time.sleep(3)
pyautogui.click(x = 643, y = 471)
time.sleep(3)
pyautogui.click(x = 817, y = 354)
time.sleep(3)
pyautogui.click(x = 1204, y = 198)
time.sleep(3)
pyautogui.click(x = 1079, y = 287)
time.sleep(3)
pyautogui.click(x = 422, y = 205)
time.sleep(3)

#pegar data do dia anterior e copiar para colar no
date_now = datetime.datetime.now()
one_days_ago = date_now - datetime.timedelta(days=1)
tree_days_ago = date_now - datetime.timedelta(days=3)
seven_days_ago = date_now - datetime.timedelta(days=7)
print('now:', date_now.strftime("%d/%m/%y"))
print( one_days_ago.strftime("%d/%m/%y")) 
print( tree_days_ago.strftime("%d/%m/%y")) 
print( seven_days_ago.strftime("%d/%m/%y"))

dt = datetime.datetime(year=2021, month=8, day=16)
str_dt = dt.strftime("%A")
print(str_dt)
weekday_name = ["SEG","TER","QUAR","QUI","SEX","SAB","DOM"]
wkday = dt.weekday()
print(weekday_name[wkday])

if weekday_name[wkday] == "SEG":
    pyautogui.write( tree_days_ago.strftime("%d/%m/%y"))
else:
    pyautogui.write( one_days_ago.strftime("%d/%m/%y"))

pyautogui.click(x = 690, y = 206)
time.sleep(3)

pyautogui.write( one_days_ago.strftime("%d/%m/%y"))

pyautogui.click(x = 1009, y = 202)
time.sleep(3)
pyautogui.click(x = 1069, y = 249)
time.sleep(3)
pyautogui.click(x = 1069, y = 249)
time.sleep(3)

pyautogui.click(x = 898, y = 256)
time.sleep(3)
pyautogui.click(x = 1190, y = 124)
time.sleep(3)

pyautogui.click(x = 284, y = 366)
time.sleep(3)
pyautogui.click(x = 354, y = 451)
time.sleep(3)

pyautogui.click(x = 1209, y = 199)
time.sleep(3)
pyautogui.click(x = 1150, y = 241)
time.sleep(3)

pyautogui.click(x = 425, y = 207)
time.sleep(3)
pyautogui.write( seven_days_ago.strftime("%d/%m/%y"))
pyautogui.click(x = 689, y = 203)
time.sleep(3)
pyautogui.write( one_days_ago.strftime("%d/%m/%y"))
pyautogui.click(x = 1114, y = 257)
time.sleep(3)

# fim do Gpass