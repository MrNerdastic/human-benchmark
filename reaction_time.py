import pyautogui as pag
import keyboard
import time

time.sleep(5)
x, y = pag.position()
while True:
	color = pag.pixel(x, y)
	if color == (75, 219, 106):
		pag.click()
	if keyboard.is_pressed("q"):
		break