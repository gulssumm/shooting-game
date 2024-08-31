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

# Load the background image
background = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/background.jpg").convert()

# Set the timer for balloon spawning
pygame.time.set_timer(SPAWN_BALLOON, 500)

# Instantiate Shooter
shooter = Shooter(screen_width, screen_height)

# Default values
level = 0
score = 0

# Set up the font object
font = pygame.font.SysFont("comicsansms", 20)
message_font = pygame.font.SysFont("comicsansms", 70)

# Display the main menu
main_menu(screen)  # Call the main menu function


def reset_game():
    global score, balloons
    score = 0
    balloons.empty()  # Remove all balloons
    Mechanism.bullets.empty()  # Remove all bullets
    # Draw the level-up message
    message = message_font.render("Level is up !!!", True, (255, 255, 255))
    screen.blit(message, (300, 250))  # Center the message on the screen
    pygame.display.flip()  # Update the display to show the message
    pygame.time.delay(3000)
    main_menu(screen)  # Call the main menu function


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

    # Check if score has reached 10
    if score == 10:
        level += 1
        reset_game()

    # Draw everything
    # screen.fill((135, 206, 235))
    screen.blit(background, (0, 0))  # Draw the background image
    balloons.draw(screen)
    Mechanism.bullets.draw(screen)
    shooter.draw(screen)

    # Draw the score to the screen
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (900, 5))

    # Draw the level to the screen
    level_text = font.render(f'Level: {level}', True, (255, 255, 255))
    screen.blit(level_text, (900, 30))

    pygame.display.flip()
