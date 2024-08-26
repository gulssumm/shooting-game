import pygame
import random


# Define the Balloon class and sprite group here
class Balloon(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the balloon image and convert it for Pygame
        self.image = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/balloon.png").convert_alpha()

        # Get the rectangle that encloses the balloon image
        self.rect = self.image.get_rect()

        # Randomly position the balloon horizontally on the screen
        self.rect.x = random.randint(0, screen_width - self.rect.width)

        # Start the balloon near the bottom of the screen
        self.rect.y = 600

    def update(self):
        # Move the balloon upward by reducing its y coordinate
        self.rect.y -= 1

        # Remove the balloon if it goes off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


# Create a group to hold all balloons
balloons = pygame.sprite.Group()

# Define a custom event for balloon spawning
SPAWN_BALLOON = pygame.USEREVENT + 1
