import main
class Monstre():
    def __init__(self,coordonnees: tuple) -> None:
        self.coordonnees = coordonnees
        self.health = 250
        self.max_health = self.health
        self.attack = 25
        self.all_projectiles = pygame.sprite.Group()
        self.velocity = 0.2
        # le self velocity correspond a la vitesse de deplacement en pixel
        self.image = pygame.image.load('assets/monstre.png')
        self.rect = self.image.get_rect()
        # On ajoute le monstre à la liste des monstres
        main.game.monsters.append(self)
    def gotoPlayer():
        player = main.game.player
        # position du joueur
        objectif = (player.rect.x,player.rect.y)
        
        direction = np.array([objectif[0] - self.rect.x,objectif[1] - self.rect.y])
        distance = np.linalg.norm(direction)

        if distance < speed:
            return objectif

        # Normaliser le vecteur de direction et le multiplier par la vitesse
        direction = (direction / distance) * speed

        # Mettre à jour la position du rectangle
        self.rect.x += direction[0]
        self.rect.y += direction[1]