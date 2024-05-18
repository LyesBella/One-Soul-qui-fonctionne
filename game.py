import pygame
from perso import Player

class Game:
    monsters = []
    def __init__(self):
        self.player =Player()
        self.pressed={}