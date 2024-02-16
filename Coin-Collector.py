from random import randint
from pgzrun import *
import pgzrun
while True:
    WIDTH = 400
    HEIGHT = 400
    score = 0
    game_over = False
    #code start_____________________________________________________________________

    hedgehog = Actor("hedgehog")
    hedgehog.pos = 100, 100

    coin = Actor("coin")
    coin.pos = 200, 200

    def draw():
        screen.fill("green")
        hedgehog.draw()
        coin.draw()
        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

        if game_over:
            screen.fill("pink")
            screen.draw.text("Final Score: " + str(score), color="black", topleft=(10, 10), fontsize=60)
            screen.draw.text()        

    def place_coin():
        coin.x = randint(20, (WIDTH - 20))
        coin.y = randint(20, (HEIGHT - 20)) 
    
    def time_up():
        global game_over
        game_over = True

    clock.schedule(time_up, 7.0)


    def update():
        global score
    
        if keyboard.left:
            hedgehog.x = hedgehog.x - 10

        elif keyboard.right:
            hedgehog.x = hedgehog.x + 10

        elif keyboard.up:
            hedgehog.y = hedgehog.y - 10

        elif keyboard.down:
            hedgehog.y = hedgehog.y + 10

        coin_collected = hedgehog.colliderect(coin)

        if coin_collected:
            score = score + 10
            place_coin()
    place_coin()


    pgzrun.go()



