import pygame

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, screen):
        super().__init__()
        self.uncharged = pygame.image.load(path)
        self.charged = pygame.image.load('./assets/spaceship_charged.png')

        self.image = self.uncharged
        self.rect = self.image.get_rect(center = (x_pos, y_pos))
        self.shield_surface = pygame.image.load('./assets/shield.png')
        self.health = 3
        self.screen = screen

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constrain()
        self.display_health()

    def screen_constrain(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 720:
            self.rect.bottom = 720

    def display_health(self):
        for index, shield in enumerate(range(self.health)):
            self.screen.blit(self.shield_surface, (10 + index*50 , 10))

    def charge(self):
        self.image = self.charged

    def discharge(self):
        self.image = self.uncharged