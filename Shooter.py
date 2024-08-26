import pygame


class Shooter:
    def __init__(self, screen_width, screen_height):
        # Load the shooter image and convert it for Pygame
        self.image = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/shooter.png").convert_alpha()

        # Get the rectangle that encloses the shooter image
        self.rect = self.image.get_rect()

        # Position the shooter at the bottom center of the screen
        self.rect.center = (screen_width // 2, screen_height - 50)

    def update(self):
        # Update the shooter's horizontal position based on the mouse's x position
        self.rect.centerx = pygame.mouse.get_pos()[0]

    def draw(self, screen):
        # Draw the shooter on the screen at its current position
        screen.blit(self.image, self.rect)
