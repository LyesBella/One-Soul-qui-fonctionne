import pygame
from game import Game
pygame.init()

#info fenetre
pygame.display.set_caption("One Soul",'playeridle.png')
screen=pygame.display.set_mode((1280,720))

running =True
background=pygame.image.load('assets/Nuit.jpg')

game = Game()

#laisser la fenetre ouverte
while running:

    screen.blit(background, (0,0))
    screen.blit(game.player.image,(game.player.rect))
    game.player.all_projectiles.draw(screen)



    #rafraichir l'ecran de jeux
    pygame.display.flip()
    for event in pygame.event.get():
       if event.type== pygame.QUIT:
           running= False
           pygame.quit()
       elif event.type==pygame.KEYDOWN:
            game.pressed[event.key]= True

            if event.key == pygame.K_SPACE:
                 game.player.launch_projectile()

       elif event.type==pygame.KEYUP:
            game.pressed[event.key]= False


    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()
    elif game.pressed.get(pygame.K_UP):
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN):
        game.player.move_down()

