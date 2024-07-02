import pygame
import settings
import random

### un pipe étant donnée par (x,y,l,h) où x et y sont les coordonnées de son coin supérieur gauche, h et l sont sa hauteur et sa longueur (=pipeLength)
### pipeMap est du type [(down,up)] où down = up = (x,y,l,h)

def pipeSpawn():  # renvoye un couple de pipe initialisé = (down,up) (situé juste en dehors de l'écran (à sa gauche))
    deltaPipe = 10 # longueur de sécurité pour la taille des tuyaux graphiquement
    hauteurUp = random.randint(settings.pipeHeigthMin, settings.screenHeigth - settings.difficulty - settings.pipeHeigthMin) + deltaPipe
    hauteurDown = settings.screenHeigth - hauteurUp - settings.difficulty + deltaPipe
    up = (1200 + deltaPipe, -deltaPipe, settings.pipeLength, hauteurUp,False)
    down = (1200 + deltaPipe, hauteurUp + settings.difficulty, settings.pipeLength, hauteurDown)
    return ([(down, up)])
    
def updatedPipes(down, up, dt):
    xDown, yDown, lDown, hDown = down
    xUp, yUp, lUp, hUp, counted= up

    # calcul des nouvelles coordonnées x de Down et Up

    newxDown = xDown - settings.gamespeed*dt
    newxUp = xUp - settings.gamespeed*dt

    # nouveaux pipes
    newDown = (newxDown, yDown, lDown, hDown)
    newUp = (newxUp, yUp, lUp, hUp,counted)
    return(newDown,newUp)

def obstacle(pipeMap,dt):
    # spawn et update la position des tuyaux // renvoye une file d'attente pipeMap contenant des couples de tuyau (downPipe, upPipe) à dessiner sur la map
    # les nouveaux tuyaux qui spawn sont ajouter en fin de liste (à sa droite) car ils apparaitront à la droite de l'écran
    # dès qu'un tuyau sort de l'écran (par la gauche) ce dernier est en position 0 (pipeMap[0]) il suffira de le pop

    # update la position des pipes déjà existant
    for i in range(len(pipeMap)):
        down, up = pipeMap[i]
        pipeMap[i] = updatedPipes(down,up,dt)
    # création de nouveau pipe si nécessaire
    downLast, upLast = pipeMap[len(pipeMap) - 1]
    (xLast, yLast, lLast, hLast) = downLast
    xNewElement = settings.screenLength - settings.pipeDistance
    if xLast < xNewElement : 
        pipeMap = pipeMap + pipeSpawn()
    # suppression du premier pipe (pipeMap[0], celui le plus à droite hors de l'écran) si nécessaire
    downFirst, upFirst = pipeMap[0]
    (xFirst, yFirst, lFirst,  hFirst) = downFirst
    if xFirst < -5-settings.pipeLength : # par sécurité on ne met pas 0
        pipeMap.pop(0)
    return (pipeMap)
    
