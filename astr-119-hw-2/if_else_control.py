#defines function
def flow_control(k):

	#defines string based on value of k
	if(k == 0):
		s = "Variable k = %d equals 0." % k

	elif(k == 1):
		s = "Variable k = %d equals 1." % k

	else:
		s = "Variable k = %d does not equal 0 or 1." % k

	#prints variable
	print(s)

#defines main function
def main():

	#declares integer
	i = 0

	#try flow_control for 0, 1, 2
	flow_control(i)
	i = 1
	flow_control(i)
	i = 2
	flow_control(i)

#runs program
if __name__ == "__main__":
	main()