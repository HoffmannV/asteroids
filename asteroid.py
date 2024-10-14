import circleshape, constants, pygame, random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()

        if self.radius < constants.ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.randint(30, 50)
            new_asteroid = Asteroid(self.position[0], self.position[1], self.radius - constants.ASTEROID_MIN_RADIUS)        
            new_asteroid.velocity = self.velocity.rotate(angle) * 1.2
            new_asteroid = Asteroid(self.position[0], self.position[1], self.radius - constants.ASTEROID_MIN_RADIUS)
            new_asteroid.velocity = self.velocity.rotate(-angle) * 1.2
