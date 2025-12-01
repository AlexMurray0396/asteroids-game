import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # print message to inform user that game is starting
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    # initiate game
    pygame.init()

    # define playing field
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # initialise object lists
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # add object instances to appropriate object lists
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    # define initial time
    dt = 0

    # initialise instance of player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # start game loop
    while 1==1:
        # retrieve log state
        log_state()

        # enable quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # draw background
        screen.fill("black")

        # update updatable object data
        for item in updatable:
            item.update(dt)

        # draw drawable objects
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        # advance timeß
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()