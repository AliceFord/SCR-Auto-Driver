import pyautogui
import datetime

screenshot = pyautogui.screenshot()
screenshot.save("screenshots/SCREENSHOT" + datetime.datetime.now().strftime("%H_%M_%S") + ".png")
