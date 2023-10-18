import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [50, 51, 48, 54, 67, 43, 30, 40]
plt.plot(x, y)
plt.plot(x,y,color='orange',linewidth=5,linestyle='dotted') #Custmizing  x and y axis (dotted,dash dot)
plt.show()  #dispkay plot