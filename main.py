import pygame,Score.score,time,math
from game import Game
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
    # Met à jour les différents temps pour le jeu
    game.deltaTime =  time.time() - game.time
    game.time = time.time()
    game.gameDuration = math.ceil(game.time - game.startTime)
    # Met à jour le fond
    screen.blit(background, (0,0))
    screen.blit(game.player.image,(game.player.rect))

    #fait bouger les projectiles
    for projectile in game.player.all_projectiles:
        projectile.move()

    game.player.all_projectiles.draw(screen)

    for monster in game.monsters:
        screen.blit(monster.image,(monster.rect))
        # Va vers le joueur
        monster.gotoPlayer(game)
        # On vérifie les collisions
        if (game.player.rect.colliderect(monster.rect)):
            monster.attack(game.player,game)
        # Est ce que le monstre est mort ?
        if (monster.health <= 0):
            monster.onDeath(game.player,game)
            print(game.player.score) 
    if (game.player.health <= 0 and game.player.isDead == False):
        game.player.onDeath()
        game.reset()

    # Rafraichir l'ecran de jeux
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type== pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running= False
            pygame.quit()

        if event.type==pygame.KEYDOWN:
            game.pressed[event.key]= True
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

            # A supprimer
            if event.key == pygame.K_a:
                game.reset()
            if event.key == pygame.K_r:
                game.spawnMonster(fenetre=screen)
        # Permet de check si une touche est toujours enfoncé
        if event.type==pygame.KEYUP:
            game.pressed[event.key]= False

    # Bouger le joueur en fonction des contrôles
    if game.pressed.get(pygame.K_RIGHT) or game.pressed.get(pygame.K_d):
        game.player.move("right",game.player.velocity)
    if game.pressed.get(pygame.K_LEFT) or game.pressed.get(pygame.K_q):
        game.player.move("left",game.player.velocity)
    if game.pressed.get(pygame.K_UP) or game.pressed.get(pygame.K_z):
        game.player.move("up",game.player.velocity)
    if game.pressed.get(pygame.K_DOWN) or game.pressed.get(pygame.K_s):
        game.player.move("down",game.player.velocity)

