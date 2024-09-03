import pygame
import sys


def draw_button(screen, text, font, color, rect, is_hovered):
    if is_hovered:
        color = (color[0] + 40, color[1] + 40, color[2] + 40)  # Make the button brighter when hovered
    pygame.draw.rect(screen, color, rect)
    screen.blit(text, text.get_rect(center=rect.center))


def main_menu(screen):
    # Set up the font for the buttons
    font = pygame.font.SysFont("comicsansms", 20)

    # Button colors
    button_color = (100, 0, 0)

    # Define the button texts
    start_button_text = font.render('Start Game', True, (255, 255, 255))
    quit_button_text = font.render('Quit Game', True, (255, 255, 255))

    # Define the button rectangles
    start_button_rect = pygame.Rect(0, 0, 120, 60)
    start_button_rect.center = (screen.get_width() // 2, screen.get_height() // 2 - 50)

    quit_button_rect = pygame.Rect(0, 0, 120, 60)
    quit_button_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 50)

    # Menu loop
    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(mouse_pos):
                    return  # Exit the menu and start the game
                if quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        # Draw the menu
        menu_background = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/bg.png").convert()
        screen.blit(menu_background, (0, 0))  # Draw the background image

        # Draw buttons with hover effect
        draw_button(screen, start_button_text, font, button_color, start_button_rect,
                    start_button_rect.collidepoint(mouse_pos))
        draw_button(screen, quit_button_text, font, button_color, quit_button_rect,
                    quit_button_rect.collidepoint(mouse_pos))

        pygame.display.flip()
