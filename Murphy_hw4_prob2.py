# Created by Hope Murphy

# Note: answer should be around 0.84

from math import sqrt, e
from random import random  


def f(x):
	return (x**(-1/2))/(e**x + 1)


N = 1000000
count = 0
for i in range(N):
	x = random()
	y = random()
	if y<f(x):
		count += 1

I = 1/(2*sqrt(count))


print(I)

	

#p = 1/(2*(sqrt(x))

