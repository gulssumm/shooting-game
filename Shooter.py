import pygame


class Shooter:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("C:/Users/21180/PycharmProjects/balloon_game/images/shooter.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
