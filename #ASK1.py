#ASK1
import numpy as np 

arr = [-(np.pi),-3*(np.pi)/4.0,-(np.pi)/2.0,-(np.pi)/4.0,-(np.pi)/6.0,(np.pi)/6.0,(np.pi)/2.0,(np.pi)/4.0,3*(np.pi)/4.0,np.pi]
sinarr = [np.sin(x) for x in arr]
sinarr[0] = 0.0
sinarr[9] = 0.0
def lagrange(x):
    while (x>np.pi):
        x-=np.pi
    while (x<-(np.pi)):
        x+=np.pi
    sum = 0.0
    c = 0
    for i in range(10):
        temp = 0.0
        for j in range(10):
            if j==c:
                continue
            temp += (x-arr[j])/(arr[c]-arr[j])
        c+=1
        sum+=temp*sinarr[i]
    return sum
x = [k for k in range(10)]
y = [lagrange(k) for k in range(10)]

def splines(x):
    a = []
    b = []
    c = []
    d = []
    for s in range(9):
        if (s == 1 or s == 8):
            d.append(d[s-1]) #not a knot
        else:
            d.append(sinarr[s])
    h = []
    y = []
    for i in range(9):
        h.append(arr[i+1] - arr[i])
        y.append(sinarr[i+1] - sinarr[i])
        
def lsquares(x):
    
