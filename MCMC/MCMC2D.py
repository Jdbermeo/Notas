from pylab import *
import random
import matplotlib.pyplot as plt

x1 = linspace(-4.0,45,1000)

def fx(x1,x2):
    return exp(-(100/20)*(x2-x1**2)**2-(1/20)*(1-x1)**2)
	
#Graficar en una grafica de contorno los saltos de la cadena de Markov
X, Y = np.meshgrid(x1, x1)
Z = fx(X,Y)
plt.figure()
CS = plt.contour(X, Y, Z)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Simplest default with labels')

x_walk1 = empty((0))
x_walk1 = append(x_walk1,8*(random.random()-0.5))
x_walk2 = empty((0))
x_walk2 = append(x_walk2,8*(random.random()-0.5))

n_iterations = 20000 #this is the number of iterations I want to make
for i in range(n_iterations):
	#genera el numero aleatorio nuevo a comparar
	x_prime1 = np.random.normal(x_walk1[i], 0.1) #0.1 is the sigma in the normal distribution, 
	x_prime2 = np.random.normal(x_walk2[i], 0.1)
	alpha = fx(x_prime1,x_prime2)/fx(x_walk1[i],x_walk2[i])
	if(alpha>=1.0):
		x_walk1  = append(x_walk1,x_prime1)
		x_walk2  = append(x_walk2,x_prime2)
	else:
	        beta = random.random()
	        if(beta<=alpha):
			x_walk1 = append(x_walk1,x_prime1)
			x_walk2 = append(x_walk2,x_prime2)
		else:
			x_walk1 = append(x_walk1,x_walk1[i])
			x_walk2 = append(x_walk2,x_walk2[i])


#Graficar en una grafica de contorno los saltos de la cadena de Markov

X1, Y1 = np.meshgrid(x_walk1,x_walk2)
Z1 = fx(X1,Y1)
plt.figure()
CS = plt.contour(X1, Y1, Z1)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Simplest default with labels')

#norm = sum(f*(x[1]-x[0]))
#plot(x,f/norm,color = 'r')
#count, bins, ignored = plt.hist(x_walk, 1000, normed=True)

plt.show()
plt.close()


