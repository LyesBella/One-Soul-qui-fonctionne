import Score.score
from perso import Player
import time,random,monstre,Score,pygame,math


class Game:
    monsters = []
    projectiles = []
    deltaTime = 0
    startTime = time.time()
    gameDuration = startTime - time.time()
    def __init__(self):
        self.time = time.time()
        self.player =Player()
        self.pressed = {}
        self.lastSpawn:int = 0
        self.spawned:bool = False

    def reset(self):
        print("Score : ",self.player.score)
        Score.score.ajouterScore(self.player.name, self.player.score, self.gameDuration)
        self.monsters.clear()
        self.projectiles.clear()
        self.player = Player()
        self.startTime = time.time()
        self.gameDuration = 0
        self.spawned = False    
    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

    def spawnMonster(self,fenetre):
        delai = 100 / (math.pow(self.player.score,0.2)+1)
        if ( (self.time - self.lastSpawn) > delai and not self.spawned and self.gameDuration > 10):
            for i in range(random.randint(1,6)):
                cote = random.choice(["gauche","droite","bas","haut"])
                if cote == "gauche":
                    monstre.Monstre((0,random.randint(0,700)),fenetre,self)
                if cote == "droite":
                    monstre.Monstre((1280,random.randint(0,700)),fenetre,self)
                if cote == "haut":
                    monstre.Monstre((random.randint(0,1280),0),fenetre,self)
                if cote == "bas":
                    monstre.Monstre((random.randint(0,1280),700),fenetre,self)
                self.lastSpawn = self.time
                self.spawned = True
            print(delai)
        elif ((self.time - self.lastSpawn) > delai):
            self.spawned = False

