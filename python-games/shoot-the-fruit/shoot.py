import pgzrun
from random import randint
import time
apple = Actor("apple")
count = 0   

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        global count, start
        print("Good shot!")
        place_apple()
        count += 1
        if count == 1:
            start = time.time()
    else:
        print("You missed!")
        timer = time.time() - start
        timer = round(timer, 3)
        print("\nYou hit {} shots in {} seconds".format(count, timer))
        
        quit()
        
 
place_apple()

pgzrun.go()