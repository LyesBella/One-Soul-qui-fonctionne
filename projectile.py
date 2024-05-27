import pygame,math

class Projectile(pygame.sprite.Sprite):
    def __init__(self,player,game):
        super().__init__()
        self.velocity = 8
        self.image= pygame.image.load('assets/projectile.png')
        self.image= pygame.transform.scale(self.image,(25,50))
        self.rect=self.image.get_rect()
        self.rect.x= player.rect.x
        self.rect.y= player.rect.y
        direction = pygame.mouse.get_pos()
        
        self.objectif_x = direction[0]  - self.rect.x
        self.objectif_y = direction[1]  - self.rect.y
        # Calcul de la distance
        distance = math.sqrt(self.objectif_x ** 2 + self.objectif_y ** 2)
        # Mettre le vecteur en fonction de la vitesse proportionnellement
        self.objectif_x = (self.objectif_x / distance) * self.velocity
        self.objectif_y = (self.objectif_y / distance) * self.velocity

        game.projectiles.append(self)
    
    def onDeath(self,game):
        game.projectiles.remove(self)
    
    def move(self):
        self.rect.move_ip(self.objectif_x, self.objectif_y)

