#ASK1
import numpy as np 

arr = [-(np.pi),-3*(np.pi)/4.0,-(np.pi)/2.0,-(np.pi)/4.0,-(np.pi)/6.0,(np.pi)/6.0,(np.pi)/4.0,(np.pi)/2.0,3*(np.pi)/4.0,np.pi]
def lagrange(x):
    while (x>np.pi):
        x-=np.pi
    while (x<-(np.pi)):
        x+=np.pi
    sum = 0
    for i in range(10):
        temp = 1
        for j in range(10):
            if j==i:
                continue
            temp *= (x-arr[j])/(arr[i]-arr[j])
        sum+=temp*np.sin(arr[i])
    return sum
#print(lagrange(2))

def splines(x):
    n = 10
    while (x>np.pi):
        x-=np.pi
    while (x<-(np.pi)):
        x+=np.pi
    a = [np.sin(x) for x in arr]
    a = []
    b = []
    d = []
    A = []
    temp1 = []
    temp2 = []
    temp1.append(1)
    for i in range(n-1):
        temp1.append(0)
        temp2.append(0)
    A.append(temp1)
    temp2.append(1)
    c = 0
    h = []
    for i in range(n-1):
        h.append(arr[i+1] - arr[i])
    for i in range(1,n-1):
        row = []
        for j in range(c):
            row.append(0)
        row.append(h[c-1])
        row.append(2*(h[c-1] + h[c]))
        row.append(h[c])
        for j in range(c+3,n):
            row.append(0)
        A.append(row)
        c+=1    
    A.append(temp2)
    y = []
    for i in range(n-1):
        y.append(np.sin(arr[i+1]) - np.sin(arr[i]))
    b = []
    b.append(0)
    for i in range(n-2):
        b.append(3*((y[i+1]/h[i+1]) - (y[i]/h[i])))
    b.append(0)
    c = np.linalg.solve(A,b)
    for i in range(n-1):
        a.append(np.sin(arr[i]))
        d.append((c[i+1] - c[i])/(3*h[i]))
        b.append((y[i]/h[i]) - (h[i] * (2*c[i] + c[i+1]) / 3))
    for i in range(n-1):
        if (x >= arr[i] and x <= arr[i+1]):
            interval = i
    return a[interval] * x + b[interval] * (x - arr[interval]) + c[interval] * ((x-arr[interval])**2) + d[interval] * ((x - arr[interval])**3)
#print(splines(2))
        

def lsquares(x,k):
    while (x>np.pi):
        x-=np.pi
    while (x<-(np.pi)):
        x+=np.pi
    A= []
    for i in range(k+1):
        row = []
        for j in range(k+1):
            if j ==0 and i == 0:
                row.append(10)
            else:
                sum = 0
                for z in arr:
                    sum += pow(z,i+j)
                row.append(sum)
        A.append(row)
    b = []
    for i in range(k+1):
        sum = 0
        for j in arr:
            sum+= pow(j,i) * np.sin(j)
        b.append(sum)
    def evaluation(coefs,x):
        d = 0
        s = 0   
        for coef in coefs:
            s+= coef*pow(x,d)
            d+=1
        return s 
    return evaluation(np.linalg.solve(A,b),x)
#print(lsquares(2,10))

