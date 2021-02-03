import pgzrun
from random import randint
WIDTH = 800
HEIGHT = 400
score = 0
speed = 4
game_over = False
fox = Actor("fox")
fox.pos = 100, 100
coin = Actor("coin")
coin.pos = 200, 200
coin2 = Actor("coin")


def draw():
	screen.fill("blue")
	fox.draw()
	coin.draw()
	coin2.draw()

	screen.draw.text("Score: "+ str(score), color="black", topleft=(10, 10))

	if game_over:
		screen.fill("red")
		screen.draw.text("Score: "+ str(score), color="black", topleft=(10, 10), fontsize=60)


def place_coin1():
	coin.x = randint(20, (WIDTH - 20))
	coin.y = randint(20, (HEIGHT - 20))
	
def place_coin2():
	coin2.x = randint(20, (WIDTH - 20))
	coin2.y = randint(20, (HEIGHT - 20))

def time_up():
	global game_over
	game_over = True

def update():
	global score, speed

	if keyboard.up and keyboard.right:
		fox.y = fox.y - speed
		fox.x = fox.x + speed
	elif keyboard.up and keyboard.left:
		fox.y = fox.y - speed
		fox.x = fox.x - speed
	elif keyboard.down and keyboard.right:
		fox.y = fox.y + speed
		fox.x = fox.x + speed
	elif keyboard.down and keyboard.left:
		fox.y = fox.y + speed
		fox.x = fox.x - speed
	elif keyboard.left:
		fox.x = fox.x - speed
	elif keyboard.right:
		fox.x = fox.x + speed
	elif keyboard.down:
		fox.y = fox.y + speed
	elif keyboard.up:
		fox.y = fox.y - speed


	coin_collected = fox.colliderect(coin)
	coin2_collected = fox.colliderect(coin2)


	if coin_collected:
		score = score + 10
		place_coin1()
		speed = speed + 1
	if coin2_collected:
		score = score + 10
		place_coin2()
		speed = speed + 1


clock.schedule(time_up, 20.0)
place_coin1()
place_coin2()


pgzrun.go()