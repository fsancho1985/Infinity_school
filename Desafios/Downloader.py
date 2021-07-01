import webbrowser
import pyautogui
import time
import pyperclip

link = input("Insira o link do Youtube: ")
url = link
pyperclip.copy(url)
url = url[:12] + 'ss' + url[12:]
webbrowser.open(url)
time.sleep(5)
pyautogui.click(x=617, y=308)
time.sleep(5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
pyautogui.click(x=941, y=305)
time.sleep(5)
pyautogui.click(x=659, y=550)
time.sleep(5)
pyautogui.hotkey('enter')