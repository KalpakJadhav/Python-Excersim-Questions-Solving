"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate."""

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        """Initialize an Alien."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

        Alien.total_aliens_created += 1

    def hit(self):
        """Decrement Alien health by one point."""
        self.health -= 1

    def is_alive(self):
        """Return True if the Alien is alive."""
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move Alien to new coordinates."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        """Detect collision with another Alien."""
        pass


def new_aliens_collection(coordinates):
    """Create a list of Alien objects from coordinates."""
    return [Alien(x, y) for x, y in coordinates]