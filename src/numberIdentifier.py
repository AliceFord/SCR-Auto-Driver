import pyautogui
import os
import PIL
import pytesseract
import time


def getCurrentNumberTesseract(image):
	image = image.crop((678, 1050, 714, 1069))
	return pytesseract.image_to_string(image)


def getCurrentNumber(image):
	if image[695, 1055] == (188, 188, 188):
		return 2
	elif image[695, 1054] >= (215, 215, 215):
		return 7


def getPoint(x, y):
	files = [f for f in os.listdir('screenshots') if os.path.isfile(f) and f[:3] == 'SCR']
	for file in files:
		print(file, PIL.Image.open(file).load()[x, y])


	# HIGH >= (215, 215, 215)
	# 695 1055 = (188,188,188) -> 2
	# 695 1054 = HIGH -> 7


t1 = time.perf_counter()
getCurrentNumberTesseract(PIL.Image.open(r"C:\Users\olive\Desktop\Coding\After Da USB\SCRAutoDriver\src\screenshots\SCREENSHOT07_36_40.png"))
print(time.perf_counter()-t1)
