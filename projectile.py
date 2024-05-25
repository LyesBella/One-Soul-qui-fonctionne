import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 7
        self.player = player
        self.image = pygame.image.load('assets/projectile1.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 23

        # permet de faire disparaitre le projectile des qu'il sort de l'écran

    def move(self):
        self.rect.x += self.velocity

        if self.rect.x > 1280:
            self.player.all_projectiles.remove(self)

