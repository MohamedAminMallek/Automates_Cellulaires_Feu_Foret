from functions import *



for fire_takes_corner in [False,True]:
    r = 0.1
    x_plot = []
    y_plot = []
    while(r<=1):
        moy = moy_simulation(r,False)
        print("densite = " + str(r) + " :  pourcentage des arbres restants ="+ str(moy))
        y_plot.append(moy)
        x_plot.append(r)
        r+=0.01

    plt.plot(x_plot,y_plot)
    plt.xlabel('Densite')
    plt.ylabel('Arbres restants')
    filename = ("fire_takes_corner" if fire_takes_corner else "fire_can't_takes_corner") + ".png"
    plt.savefig(filename)
    #plt.show()
