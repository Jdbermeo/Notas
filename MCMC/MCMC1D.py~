from pylab import *
import random
import matplotlib.pyplot as plt

x = linspace(-4.0,45,1000)
def fx(x):
    return exp(-((x-30.0)**2)/100)

x_walk = empty((0))
x_walk = append(x_walk,8*(random.random()-0.5))

n_iterations = 200000 #this is the number of iterations I want to make
for i in range(n_iterations):
	#genera el numero aleatorio nuevo a comparar
	x_prime = np.random.normal(x_walk[i], 0.89) #0.1 is the sigma in the normal distribution, 
	alpha = fx(x_prime)/fx(x_walk[i])
	if(alpha>=1.0):
		x_walk  = append(x_walk,x_prime)
	else:
	        beta = random.random()
	        if(beta<=alpha):
			x_walk = append(x_walk,x_prime)
		else:
			x_walk = append(x_walk,x_walk[i])

f = fx(x)
norm = sum(f*(x[1]-x[0]))
plot(x,f/norm,color = 'r')
count, bins, ignored = plt.hist(x_walk, 1000, normed=True)
plt.show()
plt.close()
