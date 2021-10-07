#python exceptions let you deal with unexpected results
try:
	print(a) #will throw exception because a is not defined
except:
	print("a is not defined")

#there are specific errors
try:
	print(a) #will throw exception
except NameError:
	print("a is still not defined")
except:
	print("Something else went wrong")

#this will break the program since a is undefined
print(a)