import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y

    def update(self):
        self.rect.y -= 5
        if self.rect.bottom < 0:
            self.kill()


# Create a group to hold all bullets
bullets = pygame.sprite.Group()


def shoot(shooter):
    bullet = Bullet(shooter.rect.centerx, shooter.rect.top)
    bullets.add(bullet)
