import Score.score
from perso import Player
import time,random,monstre,Score


class Game:
    monsters = []
    deltaTime = 0
    startTime = time.time()
    gameDuration = startTime - time.time()
    def __init__(self):
        self.time = time.time()
        self.player =Player()
        self.pressed={}

    def reset(self):
        print("La partie va recommencer")
        Score.score.ajouterScore(self.player.name, self.player.score, self.gameDuration)
        self.monsters.clear()
        self.player = Player()
        self.startTime = time.time()
        self.gameDuration = 0
        print("La partie a recommencée")

    def spawnMonster(self,fenetre):
        cote = random.choice(["gauche","droite","bas","haut"])
        if cote == "gauche":
            monstre.Monstre((0,random.randint(0,700)),fenetre,self)
        if cote == "droite":
            monstre.Monstre((1280,random.randint(0,700)),fenetre,self)
        if cote == "haut":
            monstre.Monstre((random.randint(0,1280),0),fenetre,self)
        if cote == "bas":
            monstre.Monstre((random.randint(0,1280),700),fenetre,self)
