import pygame
import random


# Define the Drop class and sprite group here
class DropClass(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the balloon image and convert it for Pygame
        self.image = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/water.png").convert_alpha()

        # Get the rectangle that encloses water drop image
        self.rect = self.image.get_rect()

        # Randomly position water drop horizontally on the screen
        self.rect.x = random.randint(0, screen_width - self.rect.width)

        # Start water drop near the top of the screen
        self.rect.y = -self.rect.height

    def update(self):
        # Move water drop downward
        self.rect.y += 1  # Adjust speed

        # Remove water drop if it goes off the bottom of the screen
        if self.rect.top > 600:  # Assuming screen height is 563
            self.kill()


# Create a group to hold all water drops
drops = pygame.sprite.Group()

# Define a custom event for balloon spawning
SPAWN_DROP = pygame.USEREVENT + 1
