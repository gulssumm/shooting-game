import pygame
import sys


def main_menu(screen):
    # Set up the font for the buttons
    font = pygame.font.SysFont("comicsansms", 50)

    # Define the button texts
    start_button_text = font.render('Start Game', True, (100, 0, 0))
    quit_button_text = font.render('Quit Game', True, (100, 0, 0))

    # Define the button rectangles
    start_button_rect = start_button_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    quit_button_rect = quit_button_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

    # Menu loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return  # Exit the menu and start the game
                if quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Draw the menu
        # screen.fill((255, 255, 255))  # Fill the screen with black
        # Load the background image
        paper_background = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/paper_background.jpg").convert()
        screen.blit(paper_background, (0, 0))  # Draw the background image
        screen.blit(start_button_text, start_button_rect)
        screen.blit(quit_button_text, quit_button_rect)

        pygame.display.flip()
