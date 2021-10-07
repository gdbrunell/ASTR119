x = [0.0, 3.0, 5.0, 2.5, 3.7] #define array
print(type(x))

#print x
print("Originally x = ",x)

#remove third element
x.pop(2)
print(x)

#remove element equal to 2.5
x.remove(2.5)
print(x)

#add element at the end
x.append(1.2)
print(x)

#get copy
y = x.copy()
print(y)

#how many elements equal 0.0
print(y.count(0.0))

#print index with value 3.7
print(y.index(3.7))

#sort list
y.sort()
print(y)

#reverse sort
y.reverse()
print(y)

#remove all elements
y.clear()
print(y)