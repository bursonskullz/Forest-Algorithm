import numpy as np 

# use psuedo algorithm 
# 1) intaitate data p_0 and h and read omega from a file. Print data and plot to make sure it works 
# 2) make function to take in omega and p_o that returns the slops of the line 
# put inside while loop and compute p_{n+1} = p_n + m_n * h 

# make checking method to make sure h is small compared to lambda or the first radius.
# while |p_n-\omega(t)|>\epsilon for all t in domain then keep going. 
# this ensures p_n is close to boundary before ending loop

p_0 = (1,1)
h = 0.001
epsilon = 0.0000001
# make seperate code to push omega into file and read it in next line
print('we took in the point and domain')

domain = open("domain.txt", "r")
converted_domain = []
points = domain.readlines()

for i in range(0,len(points)): 
	xcordinate = ''
	ycordinate = ''
	for j in range(0, len(points[i])):
		if (points[i][j] == '['):
			pass
		elif (points[i][j] == ','):
			#print("we found a comma")
			for l in range(j+1,len(points[i])):
				if(points[i][l] == ']'):
					pass
				else:
					ycordinate = ycordinate + points[i][l]
		else:
			if (points[i][j] == ']'):
				pass
			else:
				xcordinate = xcordinate + points[i][j]
	print xcordinate # now we need to convert to numbers and then we can save to array
	#print ycordinate
	#converted_x_cordinate = float(xcordinate)
	#converted_y_cordinate = float(ycordinate)
	#converted_domain.append([converted_x_cordinate,converted_y_cordinate])

domain.close()
print converted_domain