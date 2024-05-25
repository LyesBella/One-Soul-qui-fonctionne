import pygame
import Score.score
import time
from game import Game
from monstre import Monstre
pygame.init()

#info fenetre
pygame.display.set_caption("One Soul",'Goblin_Epee.png')
screen=pygame.display.set_mode((1280,700))

running =True

# Image de fond
background=pygame.image.load('assets/background.png')
# Instance du jeu
game = Game()
# On initialise le score
Score.score.initialisationFichier()
#Permet de garder la fenetre ouverte
while running:
    # Met à jour le temps pour le jeu
    game.deltaTime =  time.time() - game.time
    game.time = time.time()
    # Met à jour les images
    screen.blit(background, (0,0))
    screen.blit(game.player.image,(game.player.rect))
    game.player.all_projectiles.draw(screen)

    for monster in game.monsters:
        # On vérifie les collisions
        if (game.player.rect.colliderect(monster.rect)):
            monster.attack(game.player)
        monster.gotoPlayer(game)
        screen.blit(monster.image,(monster.rect))

    #rafraichir l'ecran de jeux
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type== pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running= False
            pygame.quit()

        if event.type==pygame.KEYDOWN:
            game.pressed[event.key]= True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            if event.key == pygame.K_r:
                Monstre((0,0),screen)
        if event.type==pygame.KEYUP:
            game.pressed[event.key]= False

    if game.pressed.get(pygame.K_RIGHT):
        game.player.move("right",game.player.velocity)
    if game.pressed.get(pygame.K_LEFT):
        game.player.move("left",game.player.velocity)
    if game.pressed.get(pygame.K_UP):
        game.player.move("up",game.player.velocity)
    if game.pressed.get(pygame.K_DOWN):
        game.player.move("down",game.player.velocity)

