import pygame
import settings

def playerInput(player_pos,player_speed,player_acc,dt, z_pressed,z_was_pressed):  # fait sauter l'oiseau 
    if z_pressed and not z_was_pressed:  # saut
        player_acc = settings.g - settings.j
        player_speed = (settings.g - settings.j)*dt # si on rajoute (comme un pdf intégré normal) + player_speed, on ne retrouve pas le feeling de flappy bird + on peut stack la vitesse infiniment
        player_pos.y = (1/2)*(settings.g - settings.j)*dt**2 + player_speed*dt + player_pos.y
    else:  # chute-libre
        player_acc = settings.g
        player_speed = (settings.g)*dt + player_speed
        player_pos.y = (1/2)*(settings.g)*dt**2 + player_speed*dt + player_pos.y
    return (player_pos, player_speed, player_acc)
    