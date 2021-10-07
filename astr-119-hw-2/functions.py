import numpy as np
import sys

#define function that returns value

def expo(x):
	return np.exp(x) #return e^x

#define subroutine that doesn't return value
def show_expo(n):
	for i in range(n):
		print(expo(float(i))) #call expo

#define main function
def main():
	n = 10 #default value for n

	#check if command line argument has been passed
	if(len(sys.argv)>1):
		n = int(sys.argv[1])	#if argument was provided, use it for n

	show_expo(n)				#call show_expo subroutine

#run main function
if __name__ == "__main__":
	main()