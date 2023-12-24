from turtle import Screen
import time
from player import Player
from alien_manager import AlienManager
from scoreboard import Scoreboard
from player_bullet import PlayerBullet

TICK_INTERVAL = 0.05

# Setup screen
screen = Screen()
# tracer is used to prevent the screen constantly updating - instead updates are done manually once per game tick. Interval set above.
screen.tracer(0)
screen.setup(height=600, width=800)
screen.listen()
screen.bgpic("icons\\background.gif")
screen.title("Space Invaders!")

player = Player()

player_bullet = PlayerBullet()

# Setup player movement inputs
screen.onkeypress(player.left_on, "Left")
screen.onkeyrelease(player.left_off, "Left")
screen.onkeypress(player.right_on, "Right")
screen.onkeyrelease(player.right_off, "Right")

# Setup shoot input
screen.onkeypress(lambda: player_bullet.fire_bullet(player.xcor()), " ")

# Create alien manager
alien_manager = AlienManager()

# Create scoreboard
scoreboard = Scoreboard()

screen.update()

# Variable to control game loop
game_running = True

# Establish game loop
while game_running:
    time.sleep(TICK_INTERVAL)
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

    bullet_range = range(player_bullet.x_coord - 20, player_bullet.x_coord + 20)
    aliens_in_path = [
        alien for alien in alien_manager.aliens if alien.xcor() in bullet_range
    ]
    for alien in aliens_in_path:
        if player_bullet.bullet_exists:
            distance = alien.distance(player_bullet.bullet[0])
            if distance <= 15:
                alien_manager.kill_alien(alien)
                player_bullet.delete_bullet()
                scoreboard.increase_score()


screen.exitonclick()
