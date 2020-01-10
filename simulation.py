import pygame
from functions import *


def simulation_graphique(rand,fire_takes_corner,screen):
    NB_TREES_INIT,NB_TREES_RESTANT = 0,0

    matrix,NB_TREES_INIT,NB_TREES_RESTANT = generate_map(M,rand,NB_TREES_INIT,NB_TREES_RESTANT)


    for y in range(10,height-10,10):
        for x in range(10,width-10,10):
            if matrix[y/10-1][x/10-1] == TREE:
                pygame.draw.circle(screen,(0,255,0),(x+5,y+5),5)

    pygame.display.flip()


    fire_pos = np.random.randint(low=0, high=M, size=2)

    x = fire_pos[0]
    y = fire_pos[1]

    if matrix[x][y] == TREE:
        NB_TREES_RESTANT-=1
    matrix[x][y] = FIRE

    fires = [(x,y)]
    while(len(fires)>0):

        new_fires = []
        for fire_pos in fires:
            x_fire = fire_pos[0]
            y_fire = fire_pos[1]
            
            for i in range(x_fire-1,x_fire+2):
                for j in range(y_fire-1,y_fire+2):
                    if i>=0 and i<M and j>=0 and j<M and matrix[i][j] == TREE and not is_corner(i,j,(x_fire,y_fire),fire_takes_corner):
                        new_fires.append((i,j))
                        matrix[i][j] = FIRE
                        NB_TREES_RESTANT-=1
            matrix[x_fire][y_fire] = EMPTY
        fires = new_fires
        for y in range(10,height-10,10):
            for x in range(10,width-10,10):
                if matrix[y/10-1][x/10-1] == TREE:
                    pygame.draw.circle(screen,(0,255,0),(x+5,y+5),5)
                if matrix[y/10-1][x/10-1] == FIRE:
                    pygame.draw.circle(screen,(255,0,0),(x+5,y+5),5)
                if matrix[y/10-1][x/10-1] == EMPTY:
                    pygame.draw.circle(screen,(255,222,173),(x+5,y+5),5)
        pygame.display.flip()


background_colour = (255,222,173)

M = 78
(width, height) = ((M+2)*10, (M+2)*10)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Feu de Foret')
screen.fill(background_colour)


rand = 0.65
fire_takes_corner = False

simulation_graphique(rand,fire_takes_corner,screen)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False