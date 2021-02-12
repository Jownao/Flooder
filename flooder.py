import pyautogui, time


time.sleep(2)

f = open("beemovie.txt", 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

