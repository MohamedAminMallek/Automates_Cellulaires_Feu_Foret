import numpy as np
import time
import matplotlib.pyplot as plt

FIRE = 2
TREE = 1
EMPTY = 0
M = 15


def generate_map(M,rand,NB_TREES_INIT,NB_TREES_RESTANT):
    matrix = np.zeros(shape=(M,M),dtype=int)
    for i in range(M):
        for j in range(M):
            r = np.random.uniform()
            if r<rand:
                matrix[i][j] = TREE
                NB_TREES_INIT+=1
                NB_TREES_RESTANT+=1
    return matrix,NB_TREES_INIT,NB_TREES_RESTANT
def is_corner(i,j,fire_pos,fire_takes_corner):
    
    if fire_takes_corner:
        return False
    
    if i==fire_pos[0]-1 and j==fire_pos[1]-1:
        return True
    if i==fire_pos[0]+1 and j==fire_pos[1]+1:
        return True
    if i==fire_pos[0]-1 and j==fire_pos[1]+1:
        return True
    if i==fire_pos[0]+1 and j==fire_pos[1]-1:
        return True
    return False
def simulation(rand,fire_takes_corner):
    nb_start_fire = 1
    fire_pos = np.random.randint(low=0, high=M, size=2)

    NB_TREES_INIT = 0
    NB_TREES_RESTANT = 0

    matrix,NB_TREES_INIT,NB_TREES_RESTANT = generate_map(M,rand,NB_TREES_INIT,NB_TREES_RESTANT)
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
    return NB_TREES_RESTANT*1.0/NB_TREES_INIT if NB_TREES_INIT>0 else 0

def moy_simulation(rand,fire_takes_corner):
    total_moy = 0
    nb_iter = 500
    for i in range(nb_iter):
        total_moy += simulation(rand,fire_takes_corner)
    return total_moy/nb_iter
