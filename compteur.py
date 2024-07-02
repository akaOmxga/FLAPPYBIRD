import pygame
import settings

def points(pipeMap, player_pos, point):  # affichage du nombre de points en (x = screenLength/2, y = screenHeigth/10)
    for i in range(len(pipeMap)):
        down, up = pipeMap[i]
        xUp, yUp, lUp, hUp, counted = up
        if (player_pos.x > xUp + lUp / 2) and counted == False:
            point += 1
            counted = True
            newUpPipe = xUp, yUp, lUp, hUp, counted
            pipeMap[i] = (down,newUpPipe)
    return(point, pipeMap)