import time
from PIL import ImageGrab

import pyautogui


X = 420.0

quantidade = 15

def getScreen():
    screen = ImageGrab.grab()
    return screen

def detect_color(screen):
    global X
    
    aux_color = screen.getpixel((420,430))
    
    for x in range (int(X), int(X+20)):
        for y in range(400, 460):
            
            color = screen.getpixel((x,y))
            
            if color != aux_color:
                print("Pular")
                return True
            else:
                aux_color = color

def jump():
    global quantidade
    global X

    quantidade -= 1

    if quantidade <= 0:
        X += 1.4

    elif quantidade < 10:
        X += 0.9
        
    else:
        X += 0.6
        
    pyautogui.press("up")

print("3 segundos")
time.sleep(3)

while True:
    tela = getScreen()
    
    if detect_color(tela):
        jump()
        
        
