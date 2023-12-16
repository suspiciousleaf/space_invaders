from turtle import Screen
import time
import random
from player import Player
from alien_manager import AlienManager
from scoreboard import Scoreboard
from player_bullet import PlayerBullet

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=800)
screen.listen()
screen.bgpic("icons\\background.gif")
screen.title("Space Invaders!")

player = Player()

player_bullet = PlayerBullet()

screen.onkeypress(player.left_on, "Left")
screen.onkeyrelease(player.left_off, "Left")
screen.onkeypress(player.right_on, "Right")
screen.onkeyrelease(player.right_off, "Right")


screen.onkeypress(lambda: player_bullet.fire_bullet(player.xcor()), " ")

alien_manager = AlienManager()

scoreboard = Scoreboard()

screen.update()


game_running = True

while game_running:
    time.sleep(0.05)
    screen.update()
    alien_manager.move()
    if player.right_move:
        player.right()
    if player.left_move:
        player.left()

    if player_bullet.bullet_exists:
        player_bullet.move()

    if alien_manager.check_lose():
        game_running = False
        scoreboard.game_over()

    for bul in player_bullet.bullet:
        if bul.ycor() > 290:
            player_bullet.delete_bullet()

    for alien in alien_manager.aliens:
        if random.randint(0, 99) == 0:
            alien_manager.kill_alien(alien)


screen.exitonclick()
