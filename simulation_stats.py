from functions import *



fire_takes_corner = True
r = 0.1
x_plot = []
y_plot = []
while(r<=1):
	moy = moy_simulation(r,fire_takes_corner)
	print("densite = " + str(r) + " :  pourcentage des arbres restants ="+ str(moy))
	y_plot.append(moy)
	x_plot.append(r)
	r+=0.01
filename = ("fire_takes_corner" if fire_takes_corner else "fire_can't_takes_corner") + ".png"
plt.plot(x_plot,y_plot)
plt.xlabel('Densite')
plt.ylabel('Arbres restants')
plt.title = filename
plt.filename = filename
plt.savefig(filename)
    #plt.show()
