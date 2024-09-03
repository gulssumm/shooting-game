import pygame
import sys
from Drop import SPAWN_DROP, drops, DropClass
import Mechanism
from Shooter import Shooter  # Import Shooter class


def level2_game(score, level, font,reset_game):
    # Set up the game window
    screen_width = 1000
    screen_height = 563
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Balloon Shooting Game Level 2")

    # Instantiate Shooter
    shooter = Shooter(screen_width, screen_height)

    # Load new background image for Level 2
    background = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/level2_background.png").convert()
    pygame.time.set_timer(SPAWN_DROP, 500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SPAWN_DROP:
                drop = DropClass(screen_width)  # Create new Drop
                drops.add(drop)
                print("drop spawned")
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mechanism.shoot(shooter)   # Use Mechanism to shoot

        # Update and draw objects for level 2
        drops.update()
        Mechanism.bullets.update()
        shooter.update()

        screen.blit(background, (0, 0))
        drops.draw(screen)
        shooter.draw(screen)

        # Check for collisions
        collisions = pygame.sprite.groupcollide(drops, Mechanism.bullets, True, True)
        if collisions:
            for drop in collisions:
                score += 1

        # Check if score has reached 10
        if score == 2:
            level += 1
            reset_game(level)

        # screen.fill((135, 206, 235))
        screen.blit(background, (0, 0))  # Draw the background image

        # Draw the score to the screen
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (900, 5))

        # Draw the level to the screen
        level_text = font.render(f'Level: {level}', True, (255, 255, 255))
        screen.blit(level_text, (900, 25))

        pygame.display.flip()
