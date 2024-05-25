import pygame
from perso import Player
import time

class Game:
    monsters = []
    deltaTime = 0
    def __init__(self):
        self.time = time.time()
        self.player =Player()
        self.pressed={}