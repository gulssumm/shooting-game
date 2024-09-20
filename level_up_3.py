import pygame
import sys
from Balloon import balloons, Balloon, SPAWN_BALLOON
from Drop import SPAWN_DROP, drops, DropClass
import Mechanism
from Shooter import Shooter


def level3_game(score, level, font, reset_game):
    # Set up the game window
    screen_width = 1000
    screen_height = 563
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Balloon Shooting Game Level 3")

    # Instantiate Shooter
    shooter = Shooter(screen_width, screen_height)

    # Load new background image for Level 3
    background = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/level3_background.jpg").convert()

    # Set timers for balloon and drop spawning
    pygame.time.set_timer(SPAWN_BALLOON, 500)
    pygame.time.set_timer(SPAWN_DROP, 700)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == SPAWN_BALLOON:
                balloon = Balloon(screen_width)
                balloons.add(balloon)

            if event.type == SPAWN_DROP:
                drop = DropClass(screen_width)
                drops.add(drop)

            if event.type == pygame.MOUSEBUTTONDOWN:
                Mechanism.shoot(shooter)

        # Update and draw objects for level 3
        Mechanism.bullets.update()
        balloons.update()
        drops.update()
        Mechanism.bullets.update()
        shooter.update()

        screen.blit(background, (0, 0))

        # Draw balloons and drops
        Mechanism.bullets.draw(screen)
        balloons.draw(screen)
        drops.draw(screen)
        shooter.draw(screen)

        # Check for collisions between bullets and balloons or drops
        balloon_collisions = pygame.sprite.groupcollide(balloons, Mechanism.bullets, True, True)
        drop_collisions = pygame.sprite.groupcollide(drops, Mechanism.bullets, True, True)

        # Update score based on collisions
        if balloon_collisions or drop_collisions:
            for _ in balloon_collisions:
                score += 1
            for _ in drop_collisions:
                score += 1

        # Check if score has reached the required level-up score (for example, 10)
        if score == 10:
            level += 1
            reset_game(level)

        # Draw the score and level to the screen
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (900, 5))

        level_text = font.render(f'Level: {level}', True, (255, 255, 255))
        screen.blit(level_text, (900, 25))

        pygame.display.flip()
