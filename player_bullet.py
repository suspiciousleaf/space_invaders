from turtle import Turtle, register_shape

MOVE_DISTANCE = 25

bullets = [
    "icons\\invbullet.gif",
    "icons\\invbullet2.gif",
    "icons\\invbulletopen.gif",
]

for icon in bullets:
    register_shape(icon)


class PlayerBullet:
    def __init__(self):
        self.x_coord = 0
        self.bullet = []
        self.bullet_exists = False
        self.bullet_icon = 0
        self.bullet_icon_generator = self.cycle_bullet_icon()

    def cycle_bullet_icon(self):
        while True:
            for num in [0, 1, 2, 1]:
                yield num

    def fire_bullet(self, x_coord):
        if not self.bullet_exists:
            self.x_coord = x_coord
            self.bullet_exists = True
            new_bullet = Turtle()
            new_bullet.penup()
            new_bullet.speed("fastest")
            new_bullet.shape(bullets[0])
            new_bullet.setpos(x_coord, -245)
            self.bullet.append(new_bullet)

    def move(self):
        for bul in self.bullet:
            bul.setpos(self.x_coord, bul.ycor() + MOVE_DISTANCE)
            next_icon = next(self.bullet_icon_generator)
            bul.shape(bullets[next_icon])

    def delete_bullet(self):
        for bul in self.bullet:
            bul.hideturtle()
            self.bullet.remove(bul)
        self.bullet_exists = False
