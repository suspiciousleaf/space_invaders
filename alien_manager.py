from turtle import Turtle, register_shape

# Hard coded values for easy access
MOVE_DISTANCE = 3
DROP_DISTANCE = 20
BORDER_MARGIN = 50

# Below are all of the icons to be imported
octopus_closed = "icons\\closed-octopus.gif"
octopus_open = "icons\\open-octopus.gif"

crab_closed = "icons\\closed-crab.gif"
crab_open = "icons\\open-crab.gif"

squid_closed = "icons\\closed-squid.gif"
squid_open = "icons\\open-squid.gif"

# See comment for "aliens" list below
register_shape(squid_open)

pop = "icons\\pop.gif"
register_shape(pop)

# List of all alien types to spawn at the start of the level. Only squid_closed is spawned for the squids, whereas both types of the other two aliens are used for a total of five rows. The list below is iterated through to register the icons as turtle shapes; since squid_open is missing from the list, that shape is registered separately above.
aliens = [squid_closed, crab_open, crab_closed, octopus_closed, octopus_open]

for alien in aliens:
    register_shape(alien)

# Dictionary to hold the alternating forms for each alien
shapes = {
    octopus_closed: octopus_open,
    octopus_open: octopus_closed,
    squid_closed: squid_open,
    squid_open: squid_closed,
    crab_closed: crab_open,
    crab_open: crab_closed,
}


class AlienManager:
    # Initialise the alien manager
    def __init__(self):
        self.aliens = []
        self.dead_aliens = []
        self.dead_timer = 0
        self.create_aliens()
        self.direction = 1
        self.steps_taken = 0
        self.drops = 0
        self.descend = False
        self.border_margin = 400 - BORDER_MARGIN

    # Creates all the aliens at the start of the level
    def create_aliens(self):
        y_cor = 200
        for alien in aliens:
            x_cor = -250
            for _ in range(11):
                new_alien = Turtle()
                new_alien.penup()
                new_alien.speed("fastest")
                new_alien.shape(alien)
                new_alien.setpos(x_cor, y_cor)
                self.aliens.append(new_alien)
                x_cor += 50
            y_cor -= 30

    def move(self):
        self.process_dead()

        # Count the number of steps taken, and alternate the alien icon every 5 steps
        self.steps_taken += 1
        if self.steps_taken >= 5:
            self.open_close()

        # Calculate the max and min values for x coordinate and change direction when an alien reaches the edge of the screen
        x_coordinates = [alien.xcor() for alien in self.aliens]
        x_max = max(x_coordinates)
        x_min = min(x_coordinates)

        if x_max >= self.border_margin or x_min <= -self.border_margin:
            self.direction *= -1
            self.drops += 1
            self.descend = True

        # If aliens have reached a border, all descend
        if self.descend:
            self.drop()
            self.border_margin = 380
            return
        else:
            # Set new position for each alien on x axis
            for alien in self.aliens:
                alien.setpos(
                    alien.xcor() + (self.direction * MOVE_DISTANCE), alien.ycor()
                )
            self.border_margin = 350

    # Alternates alien icons between the two versions for each alien
    def open_close(self):
        for alien in self.aliens:
            alien.shape(shapes[alien.shape()])
        self.steps_taken = 0

    # Causes all aliens to descend
    def drop(self):
        for alien in self.aliens:
            alien.setpos(alien.xcor(), alien.ycor() - DROP_DISTANCE)
        self.descend = False

    # Check to see if any aliens have reached the bottom of the screen
    def check_lose(self):
        y_min = min([alien.ycor() for alien in self.aliens])
        return y_min <= -240

    def kill_alien(self, alien):
        alien.shape(pop)
        self.aliens.remove(alien)
        self.dead_aliens.append(alien)

    def process_dead(self):
        if len(self.dead_aliens):
            self.dead_timer += 1
            if self.dead_timer >= 5:
                for dead_alien in self.dead_aliens:
                    dead_alien.hideturtle()
                    self.dead_aliens.remove(dead_alien)
                self.dead_timer = 0
