import pygame
import Score
import Score.score
from projectile import Projectile
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # la ligne au dessus permet de declarer le personnage comme un sprite
        self.health = 250
        self.max_health = 250
        self.attack = 25
        self.all_projectiles = pygame.sprite.Group()
        self.velocity = 2
        # le self velocity correspond a la vitesse de deplacement en pixel
        self.image = pygame.image.load('assets/soldat.png')
        self.rect = self.image.get_rect()
        self.score = 0
        self.name = "player"


    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        self.rect.x+= self.velocity

    def move_left(self):
        self.rect.x-= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
    def kill():
        Score.score.ajouterScore(self.name, self.score)
