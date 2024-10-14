import pygame, math, constants

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def detect_collision(self, other):
        # selfwritten method to detect collisions
        # return math.sqrt(pow(self.position[0] -other.position[0],2) + pow(self.position[1] - other.position[1],2)) < constants.PLAYER_RADIUS + other.radius
        return self.position.distance_to(other.position) < constants.PLAYER_RADIUS + other.radius
