import pygame

# dimension de l'écran
screenLength = 1200
screenHeigth = 800

# taille du cercle du joueur : 
player_radius = 30

# vitesse du jeu
gamespeed = 436  #unit/s 
# par des calculs de proportion selon les gameplays de flappy bird en prenant un oiseau de 30 unit de rayon

# titre de l'écran 
titre = "Flappy Bird"

# couleur de l'écran
background_color = (135, 206, 250)  # Bleu ciel

# difficulté : espace entre les tuyau, correspondant à (flappy bird = 4x la taille de l'oiseau = 240) ou obtenu par calculs de proportion : 228
difficulty = 200


# spawnrate des tuyaux : distance entre chaque tuyaux // obtenu par l'écran faisant 1200, on veut 4 tuyaux sur l'écran // ou 380 obtenu par calculs de proportion selon les gameplays
pipeDistance = 380

# largeur des tuyaux : calcul à partir des proportions : 180
pipeLength = 125

# hauteur des tuyaux minimun
pipeHeigthMin = 80

# gravité et jump :
g = 1000
j = 45000
