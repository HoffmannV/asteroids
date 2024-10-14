import pygame, constants
from shot import Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    play = True
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    the_player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    #test_asteroid = Asteroid(constants.SCREEN_WIDTH - 130, constants.SCREEN_HEIGHT - 130, 30)
    asteroid_field = AsteroidField()

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill('black')

        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for sprite in asteroids:
            for shot in shots:
                if shot.detect_collision(sprite):
                    shot.kill()
                    sprite.split()
        for sprite in asteroids:
            if the_player.detect_collision(sprite):
                print("Game Over!")
                play = False
        
        pygame.display.flip()
        
        #End of game loop the loop will wait 1/60 of a second before executing again 
        dt = game_clock.tick(120) / 1000

if __name__ == "__main__":
    main()
