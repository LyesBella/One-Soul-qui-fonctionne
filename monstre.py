class Monstre():
    def __init__(self,coordonnees: tuple) -> None:
        self.coordonnees = coordonnees
        self.health = 250
        self.max_health = self.health
        self.attack = 25
        self.all_projectiles = pygame.sprite.Group()
        self.velocity = 2
        # le self velocity correspond a la vitesse de deplacement en pixel
        self.image = pygame.image.load('assets/monstre.png')
        self.rect = self.image.get_rect()
        pass