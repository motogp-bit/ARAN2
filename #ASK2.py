#ASK2
import numpy as np
step = np.pi/24.0
a = 0
arr = []
arr.append(a)
while (a+step <(np.pi)/2.0):
    arr.append(a+step)
    a+=step
#print(arr)
def simpson():
    sum = 0
    for i in range(12):
        if i==0 or i==11:
            sum+=np.sin(arr[i])
        elif i % 2 == 1:
            sum+= 4*np.sin(arr[i])
        elif i % 2 == 0:
            sum+= 2*np.sin(arr[i])
    return (np.pi/72.0) *sum
print(simpson())



def trapezoid():
    sum = 0
    for i in range(12):
        if i==0 or i==11:
            sum+=np.sin(arr[i])
        else:
            sum+= 2* np.sin(arr[i])
    sum*= step/2
    return sum
print(trapezoid())