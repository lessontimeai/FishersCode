x=1 
print(x)
x = 1/2

if x>0 and x<1:
    print("x is x>0 and x<1")
else:
    print("x is not x>0 and x<1")

for i in range(100): # For loop
    print(i)

x = [1,2,3,4] # arrays

x = 100 
l = []
while x>0: # While loop, conditional iteration
    x -= 2 # Assignment 
    print(x)
    l.append(x)

import matplotlib.pyplot as plt

plt.plot(l)
plt.show()

print(2/3)
print(200//3)

prompt = int(input("Enter a number: "))
if (prompt%3)==0:
    print("It is divisible to 3")
else:
    print("Not divisible")


import numpy as np
l = np.array(l)/20
l = np.sin(l)
plt.plot(l)
plt.show()

