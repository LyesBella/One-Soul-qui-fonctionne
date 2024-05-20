import pygame
from game import Game
from monstre import Monstre
pygame.init()

#info fenetre
pygame.display.set_caption("One Soul",'Goblin_Epee.png')
screen=pygame.display.set_mode((1280,700))

running =True
background=pygame.image.load('assets/background.png')

game = Game()

#laisser la fenetre ouverte
while running:

    screen.blit(background, (0,0))
    screen.blit(game.player.image,(game.player.rect))
    for monster in game.monsters:
        screen.blit(monster.image,(monster.rect))
    game.player.all_projectiles.draw(screen)

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
                Monstre((game.player.rect),screen)

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

