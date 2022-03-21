#Laget av Vinjar Hammer og Carl Thyness

import numpy as np
import matplotlib.pyplot as plt

#beregner generell polynomfunksjon
def g(koeffisienter, x):
    res = 0
    for i in range(len(koeffisienter)):
        res += koeffisienter[i]*x**(len(koeffisienter)-i-1)
    return res

#plotter generell polynomfunksjon
def plotFunc(params):
    x = np.linspace(-5,5,100)
    plot_y = g(params,x)
    plt.plot(x,plot_y)
    
    
#plotter punkter (x,y)
def plotPunkt(x,y):
    plt.plot(x,y,"rx")
    
plt.grid()

print("Hei! Nå skal vi lage et andregradspolynom på formen ax\u00b2+bx+c") #\u00b gir "opphøyd i"
a = float(input("Skriv inn din a: "))
b = float(input("Skriv inn din b: "))
c = float(input("Skriv inn din c: "))
plotFunc([a,b,c])
plt.show()
N = int(input("Skriv inn antall punkter du ønsker: "))
n_regresjon = int(input("Hvilken orden skal det være på regresjonsfunksjonen?"))

sample_x = [-4.5,4.5]

sample_x = np.append(sample_x, np.random.uniform(-5,5,N-2))      #her har vi valgt intervall [-5,5]


sample_y = np.round(g([a,b,c],sample_x)) + np.random.uniform(-1,1,N)   #runder av til nærmeste heltall

plotPunkt(sample_x,sample_y)
plotFunc([a,b,c])
plt.show()

f_reg = np.polyfit(sample_x,sample_y,n_regresjon) #gir polynomfunksjon av grad n-1 ved regresjonsanalyse

plotPunkt(sample_x,sample_y)
plotFunc([a,b,c])
plotFunc(f_reg)
plt.show()



        











#t = np.linspace(-5,5)


