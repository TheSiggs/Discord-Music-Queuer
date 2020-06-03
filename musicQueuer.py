import pyautogui as gui
import time
# go to the discord chat box 
# (set at a certian location on screen)
def find_location():
    while True:
        time.sleep(1)
        x, y = gui.position()
        print("X:", x, "Y:", y, "RGB:", gui.screenshot().getpixel(gui.position()))
        if x == 0 and y == 0:
            break

def typeIn(text):
    gui.typewrite(text + " ")


def enter():
    gui.press('enter')

# X: 584 Y: 987
def exceuteCommand(Input):
    gui.click(584, 987)
    typeIn(Input)
    enter()


# type the the command ;;p songname


# Read a text file of song titles or song links
with open('songs.txt') as f:
	for line in f:
		# l = 
		exceuteCommand(";;p "+ line.split('\n')[0]);