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

'''
def splines(x):
    while (x>np.pi):
        x-=np.pi
    while (x<-(np.pi)):
        x+=np.pi
    a = [np.sin(x) for x in arr]
    A = []
    h = []
    for i in range(9):
        h.append(arr[i+1] - arr[i])
    c = 0
    for i in range(10):
        row = []
        if i == 0:
            row.append(1)
            for j in range(1,10):
                row.append(0)
        elif i == 9:
            for j in range(9):
                row.append(0)
            row.append(1)
        else:
            for j in range(10):
                if j == c:
                    row.append(h[c])
                elif j == c+1:
                    row.append(2*(h[c] + h[c+1]))
                elif j == c+2:
                    row.append(h[c+1])
                else:
                    row.append(0)
            c+=1   
        A.append(row)
    b = []
    di = []
    for i in range(10):
        di.append(np.sin(arr[i]))
    for i in range(10):
        if i == 0 or i == 9:
            b.append(0)
        else:
            b.append((3/h[i])*(di[i+1] - di[i]) - (3/h[i-1])* (di[i] - di[i-1]))
    bi = np.linalg.solve(A,b)
    ai = []
    for i in range(10):
        ai =
    print(A)
splines(0)  

def splines(x):
    while (x>np.pi):
        x-=np.pi
    while (x<-(np.pi)):
        x+=np.pi
    ai = []
    bi = []
    ci = []
    di = []
    hi = []
    yi = []
    for i in range(9):
        hi.append(arr[i+1] - arr[i])
        yi.append(sin(arr[i]))
    yi.append(sin(arr[9]))
    for i in range(9):
        A = []
        temp1= []
        temp1.append(1)
        for j in range(1,4):
            temp1.append(0)
        A.append(temp1)
        temp2 = []
        temp2.append(h[i])
        temp2.append(1)
        temp2.append(h[i]**2)
        temp2.append(h[i]**3)
        A.append(temp2)
        temp3 = []
        temp3.append(0)
        temp3.append(1)
        temp3.append(2*h[i])
        temp3.append(3*(h[i]**2))
        A.append(temp3)
        temp4 = []
        temp4.append(0)
        temp4.append(0)
        temp4.append(2)
        temp4.append(6*h[i])
        A.append(temp4)
        b = []
        b.append(y[i])
        b.append(y[i+1])
        '''

#This is the ai solution
def splines(x):
    def cubic_spline_coefficients(x, y):
        n = len(x) - 1  
        coefficients = []
        h = np.diff(x)
        delta = np.diff(y) / h
        lower_diagonal = h[:-2]
        main_diagonal = np.concatenate(([h[0] + h[1]], 2 * (h[1:-1] + h[:-2]), [h[-2] + h[-3]]))
        upper_diagonal = h[1:-1]

        A = np.diag(lower_diagonal, -1) + np.diag(main_diagonal, 0) + np.diag(upper_diagonal, 1)
        B = 6 * np.diff(delta)

        m = np.zeros(n+1)
        m[1:-1] = np.linalg.solve(A, B)

        for i in range(n):
            hi = x[i+1] - x[i]

            A_i = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, hi, 2*hi**2, 3*hi**3],
                [0, 0, 2, 6*hi],
            ])

            b_i = np.array([y[i], y[i+1], m[i], m[i+1]])
            x_i = np.linalg.solve(A_i, b_i)
            coefficients.append(x_i)

        return coefficients           
#ai solution ends
    c = 0
    for i in range(len(arr) - 1):
        if x >= arr[i] and x <= arr[i+1]
        c = i
        break
    d = 0
    s = 0
    for elem in cubic_spline_coefficients(arr,[np.sin(x) for x in arr])[c]:
        s+= elem*pow(x,d)
        d+=1
    return s
    

        

def lsquares(x,k):
    while (x>np.pi):
        x-=np.pi
    while (x<-(np.pi)):
        x+=np.pi
    A= []
    for i in range(k):
        row = []
        for j in range(k):
            if j ==0 and i == 0:
                row.append(10)
            else:
                sum = 0
                for z in arr:
                    sum += pow(z,i+j)
                row.append(sum)
        A.append(row)
    b = []
    for i in range(k):
        sum = 0
        for j in arr:
            sum+= pow(j,i) * np.sin(j-1)
        b.append(sum)
    def evaluation(coefs,x):
        d = 0
        s = 0   
        for coef in coefs:
            s+= coef*pow(x,d)
            d+=1
        return s 
    return evaluation(np.linalg.solve(A,b),x)
print(lsquares(2,6))

