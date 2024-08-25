import pygame
import random


# Define the Balloon class and sprite group here
class Balloon(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/balloon.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = 600  # Start at the bottom of the screen

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()


# Create a group to hold all balloons
balloons = pygame.sprite.Group()

# Define a custom event for balloon spawning
SPAWN_BALLOON = pygame.USEREVENT + 1
