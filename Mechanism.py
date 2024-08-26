import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Load the bullet image and convert it for Pygame
        self.image = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/bullet.png").convert_alpha()

        # Get the rectangle that encloses the bullet image
        self.rect = self.image.get_rect()

        # Position the bullet based on the provided x and y coordinates
        self.rect.centerx = x
        self.rect.top = y

    def update(self):
        # Move the bullet upward by reducing its y coordinate
        self.rect.y -= 2

        # Remove the bullet if it goes off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


# Create a group to hold all bullets
bullets = pygame.sprite.Group()


def shoot(shooter):
    # Create a bullet at the shooter's position and add it to the bullets group
    bullet = Bullet(shooter.rect.centerx, shooter.rect.top)
    bullets.add(bullet)
