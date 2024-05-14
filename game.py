import pygame
from perso import Player

class Game:
    def __init__(self):
        self.player =Player()
        self.monsters = []
        self.pressed={}