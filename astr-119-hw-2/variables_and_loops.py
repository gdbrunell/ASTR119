import numpy as np 		#numpy can be used for lots of things

def main():
	i = 0	#integers can be delcared with number
	n = 10	#another integer
	x = 119.0 	#floating point numbers are delcared with "."

	#numpy can be used to delcare arrays quickly
	y = np.zeros(n,dtype=float)	#declares 10 zeroes as floats using np

	#for loops can be used to iterate with variable
	for i in range(n):	#i in range [0,n-1]
		y[i] = 2.0 * float(i) + 1.	#set y = 2i+1 as floats

	#it is possible to iterate using variables
	for y_element in y:
		print(y_element)

#execute main function
if __name__ == "__main__":
	main()