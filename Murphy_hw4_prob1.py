#Created by Hope Murphy

from random import random
from numpy import arange
from pylab import plot, xlabel, ylabel, show, legend



#Number of atoms to start with
NBi213 = 10000
NTl    = 0
NPb    = 0
NBi209 = 0

#Half-life of Bi213 in seconds, Half-life = 45.583 mins
tauBi = 45.583*60

#Half-life of Tl in seconds, Half-life = 2.1617 mins
tauTl = 2.1617*60

#Half-life of Pb in seconds, Half-life = 3.25278 h
tauPb = 3.25278*60*60

#Size of time-step in seconds
h = 1

#Probability of decay in one time-step
pBi = 1-(2**(-h/tauBi))
pTl = 1-(2**(-h/tauTl))
pPb = 1-(2**(-h/tauPb))

tmax = 20000		#total time


#Lists of plot points 
tpoints = arange(0, tmax, h)
Bi213points = []
Tlpoints    = []
Pbpoints    = []
Bi209points = []


#This is the main loop
for t in tpoints:
	Bi213points.append(NBi213)
	Tlpoints.append(NTl)
	Pbpoints.append(NPb)
	Bi209points.append(NBi209)


	#This calculates the number of atoms that decay
	decay=0

	#Now we need to figure out how to decide at random (with the appropriate probability) the route that Bi213 decays.
######################################################################################################################
	for i in range(NBi213):
		if random()<pBi*.9791 and NBi213>= 0:
			decay += 1
	NBi213 -= decay
	NPb    += decay	

	for i in range(NBi213):
		if random()<pBi*0.029 and NBi213>= 0:
			decay += 1
	NBi213 -= decay
	NTl    += decay

	for i in range(NTl):
		if random()<pTl and NTl>= 0:
			decay += 1
	NTl    -= decay
	NPb    += decay	

	for i in range(NPb):
		if random()<pPb:
			decay += 1
	NPb    -= decay
	NBi209 += decay


print('NBi209=', NBi209)
print('NBi213=', NBi213)
print('NTl=', NTl)
print('NPb=', NPb)

#Lastly, make the graph 
plot(tpoints, Bi213points, label='Bi_213')
plot(tpoints, Tlpoints, label='Tl')
plot(tpoints, Pbpoints, label='Pb')
plot(tpoints, Bi209points, label='Bi_209')
xlabel('Time')
ylabel('Number of atoms')
legend = legend(loc='best')
show()


#Results are: 
#('NBi209=', 8286)
#('NBi213=', 0)
#('NTl=', -2)
#('NPb=', 1716)

