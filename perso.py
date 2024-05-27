import pygame
from projectile import Projectile
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # la ligne au dessus permet de declarer le personnage comme un sprite
        self.name = "player"
        self.health = 150
        self.max_health = self.health 
        self.attack = 25
        self.velocity = 4
        self.score = 0
        self.isDead = False
        # le self velocity correspond a la vitesse de deplacement en pixel
        self.image = pygame.image.load('assets/Joueur.png')
        self.rect = self.image.get_rect()
        self.all_projectiles = pygame.sprite.Group()
    def launch_projectile(self,game):
        Projectile(self,game)

    def move(self,direction,speed):
        if direction == "right":
            self.rect.x+= speed
        elif direction == "left":
            self.rect.x-= speed
        elif direction == "up":
            self.rect.y -= speed
        elif direction == "down":
            self.rect.y += speed

    def onDeath(self):
        self.isDead = True
