import pygame
import settings
import collision
import map
import player
import compteur
import sys

pygame.init()
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((settings.screenLength, settings.screenHeigth))
clock = pygame.time.Clock()
pygame.display.set_caption(settings.titre)
dt = 0
player_acc = 0
player_speed = 0
point = 0
player_pos = pygame.Vector2(screen.get_width() / 4, screen.get_height() / 2)


# boucle principale 
running = True
z_pressed = False
z_was_pressed = False
pipeMap = map.pipeSpawn()

while running:
    # FPS
    dt = clock.tick(120) / 1000 # temps écoulé depuis la dernière frame lorsque l'on update le jeu à 120 fps
    
    # fermer le jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ré-initialiser l'écran
    screen.fill(settings.background_color)

    ##### UPDATE DU JEU #####

    # obtenir l'état actuel de la touche 'z'
    keys = pygame.key.get_pressed()
    z_pressed = keys[pygame.K_z]

    # update de la position du joueur
    player_pos, player_speed, player_acc = player.playerInput(player_pos, player_speed, player_acc, dt, z_pressed, z_was_pressed)  # update l'oiseau selon les inputs du joue
    z_was_pressed = z_pressed
    # affichage de la nouvelle position du joueur
    pygame.draw.circle(screen, "yellow", player_pos, 30)
    
    # update et affichage des obstacles
    pipeMap = map.obstacle(pipeMap, dt)  # spawn et update la position des tuyaux 
    for pipes in pipeMap:
        downPipe, upPipe = pipes
        xDown, yDown, lDown, hDown, = downPipe
        xUp, yUp, lUp, hUp, counted= upPipe
        # flemme de tout changer mais les pipes sont en fait en mode (x,y,l,h)
        pygame.draw.rect(screen, "green", (xDown, yDown, lDown, hDown))
        pygame.draw.rect(screen, "green", ( xUp, yUp, lUp, hUp))
    
    # teste collision 
    gameover = collision.gameOver(player_pos, pipeMap)
    if gameover:
        temps_d_attente = 100 # en secondes
        pygame.time.wait(1000*temps_d_attente) # en millisecondes

    # affichage des points : 
    point, pipeMap = compteur.points(pipeMap, player_pos, point)
    text = font.render(str(point), True,"black")
    text_rect = text.get_rect()
    text_rect.center = (screen.get_width() / 2, screen.get_height() / 10)
    # Blitter (dessiner) le texte sur l'écran
    screen.blit(text, text_rect)

    # mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()

