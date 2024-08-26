import pygame
import sys
from Balloon import Balloon, balloons, SPAWN_BALLOON
from Shooter import Shooter
import Mechanism    # Assuming Mechanism contains bullet-related logic
from menu import main_menu

# Initialize Pygame (this must be done before any Pygame functions are used)
pygame.init()

# Set up the game window
screen_width = 1000
screen_height = 563
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Balloon Shooting Game")

# Display the main menu
main_menu(screen)  # Call the main menu function

# Load the background image
background = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/background.jpg").convert()

# Set the timer for balloon spawning
pygame.time.set_timer(SPAWN_BALLOON, 500)

# Instantiate Shooter
shooter = Shooter(screen_width, screen_height)

# Default score
score = 0

# Set up the font object
font = pygame.font.SysFont("comicsansms", 20)

# Game loop
while True:
    mouse_pos = pygame.mouse.get_pos()  # Get mouse position

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWN_BALLOON:
            balloon = Balloon(screen_width)  # Pass screen_width to Balloon constructor
            balloons.add(balloon)
        if event.type == pygame.MOUSEBUTTONDOWN:
            Mechanism.shoot(shooter)

    # Update game objects
    balloons.update()
    Mechanism.bullets.update()
    shooter.update()

    # Check for collisions
    collisions = pygame.sprite.groupcollide(balloons, Mechanism.bullets, True, True)
    if collisions:
        for balloon in collisions:
            score += 1

    # Draw everything
    # screen.fill((135, 206, 235))
    screen.blit(background, (0, 0))  # Draw the background image
    balloons.draw(screen)
    Mechanism.bullets.draw(screen)
    shooter.draw(screen)
    # Draw the score to the screen
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (900, 5))

    pygame.display.flip()
