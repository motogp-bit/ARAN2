import numpy as np
step = np.pi/20.0
a = 0
arr = []
arr.append(a)
while (a+step <(np.pi)/2.0):
    arr.append(a+step)
    a+=step
def simpson():
    sum = np.sin(0) + np.sin(np.pi/2)
    for i in range(1,10):
        if i % 2 == 1:
            sum+= 4*np.sin(arr[i])
        elif i % 2 == 0:
            sum+= 2*np.sin(arr[i])
    return (step/3) *sum
#print(simpson())



def trapezoid():
    sum= np.sin(0) + np.sin(np.pi/2)
    for i in range(1,10):
        sum+= 2*np.sin(arr[i])
    sum*= step/2
    return sum
#print(trapezoid())