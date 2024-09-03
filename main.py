import pygame
import sys
from Balloon import balloons, Balloon, SPAWN_BALLOON
from Shooter import Shooter
import Mechanism    # Assuming Mechanism contains bullet-related logic
from menu import main_menu
from level_up_2 import level2_game

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

# Default values
score = 0
level = 1

# Set up the font object
font = pygame.font.SysFont("comicsansms", 20)
message_font = pygame.font.SysFont("comicsansms", 70)


def level_up_screen(level):
    screen.fill((95, 52, 18))  # chocolate brown

    # Display "Level Up" message
    level_up_text = font.render(f"Level {level}!", True, (255, 255, 255))
    sub_text = font.render("Press any key to continue...", True, (255, 255, 255))

    screen.blit(level_up_text, (screen.get_width() // 2 - level_up_text.get_width() // 2,
                                screen.get_height() // 2 - level_up_text.get_height() // 2 - 20))
    screen.blit(sub_text, (screen.get_width() // 2 - sub_text.get_width() // 2,
                           screen.get_height() // 2 + sub_text.get_height()))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

    # Add a short delay before showing the menu
    pygame.time.delay(1000)  # 1000 milliseconds (0.5 seconds) delay


def reset_game(level):
    global score, balloons
    score = 0
    balloons.empty()  # Remove all balloons
    Mechanism.bullets.empty()  # Remove all bullets

    level_up_screen(level)
    main_menu(screen)  # Call the main menu function
    if level == 2:
        level2_game(score, level, font, reset_game)


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
    if score == 2:
        level += 1
        reset_game(level)

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
    screen.blit(level_text, (900, 25))

    pygame.display.flip()
