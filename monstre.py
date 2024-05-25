import pygame
import math
import game
class Monstre():
    def __init__(self,coordonnees: tuple,fenetre: pygame.Surface) -> None:
        self.coordonnees = coordonnees
        self.health = 250
        self.max_health = self.health
        self.attack = 25
        self.all_projectiles = pygame.sprite.Group()
        # Vitesse doit etre supérieur à 1 pour éviter les bugs
        self.velocity = 2
        # le self velocity correspond a la vitesse de deplacement en pixel
        self.image = pygame.image.load('assets/Goblin_Epee.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.coordonnees[0],self.coordonnees[1])
        # On ajoute le monstre à la liste des monstres
        game.Game.monsters.append(self)
    def gotoPlayer(self,game:game.Game):
        player = game.player
        # Position du joueur
        objectif = (player.rect.x, player.rect.y)
        # Calculer le vecteur de direction
        direction_x = objectif[0] - self.rect.x
        direction_y = objectif[1] - self.rect.y
        # Calculer la distance
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
        # Si la distance est plus petite que la vitesse, se rendre directement à l'objectif
        if distance != 0:
            # Normaliser le vecteur de direction et le multiplier par la vitesse
            direction_x = (direction_x / distance) * self.velocity
            direction_y = (direction_y / distance) * self.velocity
        # Mise à jour de la position du rectangle avec les valeurs entières
        self.rect.move_ip(direction_x, direction_y)