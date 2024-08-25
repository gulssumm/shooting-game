import pygame
import sys
from Balloon import Balloon, balloons, SPAWN_BALLOON
from Shooter import Shooter
import Mechanism    # Assuming Mechanism contains bullet-related logic

# Initialize Pygame (this must be done before any Pygame functions are used)
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Balloon Shooting Game")

# Set the timer for balloon spawning
pygame.time.set_timer(SPAWN_BALLOON, 15000)

# Instantiate Shooter
shooter = Shooter(screen_width, screen_height)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWN_BALLOON:
            balloon = Balloon(screen_width)  # Pass screen_width to Balloon constructor
            balloons.add(balloon)
        if event.type == pygame.MOUSEBUTTONDOWN:
            Mechanism.shoot(shooter)  # Pass the shooter instance

    # Update game objects
    balloons.update()
    Mechanism.bullets.update()
    shooter.update()

    # Check for collisions
    collisions = pygame.sprite.groupcollide(balloons, Mechanism.bullets, True, True)
    if collisions:
        for balloon in collisions:
            pass  # Add logic for handling collisions here

    # Draw everything
    screen.fill((135, 206, 235))
    balloons.draw(screen)
    Mechanism.bullets.draw(screen)
    shooter.draw(screen)

    pygame.display.flip()
