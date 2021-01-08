import pyautogui
import PIL

# test = pyautogui.screenshot()
# test.save(r"screenshots\test.png")

X = 1310
Y1 = 996
Y2 = 1016
Y3 = 1036
Y4 = 1056


def getAllLights(image):
	return [image[X, Y1], image[X, Y2], image[X, Y3], image[X, Y4]]


def main():
	image = PIL.Image.open("screenshots/YellowLight1.jpg").load()

	if image[X, Y2][1] > 250 and image[X, Y2][0] < 170:
		print("Light is green")
	elif 170 < image[X, Y1][1] < 200 and image[X, Y1][0] > 250:
		print("Light is yellow 1")
	elif image[X, Y2][1] > 250 and 170 < image[X, Y2][0] < 200:
		print("Light is yellow 2")
	elif image[X, Y4][0] > 250:
		print("Light is red")
	else:
		print("No clue what colour the light is! Colours: ", end="")
		[print(item, end=", ") for item in getAllLights(image)]
		print()


if __name__ == "__main__":
	main()
