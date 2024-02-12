import numpy as np 
import math as mt 

data = []
def makedomain():
	domain = np.linspace(0, 2*mt.pi, 500)
	for t in domain:
		x = 2.14* mt.cos(t)
		y = 18.1877* mt.sin(t)
		point = [x,y]
		data.append(point)
makedomain()

with open("domain.txt", "w") as txt_file:
    for line in data:
        txt_file.write('['+ str(line[0]) + "," + str(line[1]) +']' + '\n')