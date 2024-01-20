import numpy as np

pointsx = [1,2,3,4,5,6,7,8,9,10]
points1 = [0.940,0.940,0.925,1.020,1.010,1.050,1.080,1.130,1.160,1.210] #DOPLER
points2 = [0.117,0.116,0.119,0.117,0.115,0.115,0.115,0.114,0.116,0.116] #KAIROMEZ

    
n = 10
def polyfit(data,k):
    A= []
    for i in range(k+1):
        row = []
        for j in range(k+1):
            if j ==0 and i == 0:
                row.append(n)
            else:
                sum = 0
                for z in pointsx:
                    sum += pow(z,i+j)
                row.append(sum)
        A.append(row)
    b = []
    for i in range(k+1):
        sum = 0
        for j in pointsx:
            sum+= pow(j,i) * data[10-j]
        b.append(sum)
    return np.linalg.solve(A,b)

def evaluation(coefs,x):
    d = 0
    s = 0
    for coef in coefs:
        s+= coef*pow(x,d)
        d+=1
    return s
    
    
    
s1 = 0
s2 = 0
s3 = 0
for i in range(1,11):
    s1+= abs(evaluation(polyfit(points1,3),i) - points1[i-1])
    s2+= abs(evaluation(polyfit(points1,4),i) - points1[i-1])
    s3+= abs(evaluation(polyfit(points1,5),i) - points1[i-1])
s1/=10
s2/=10
s3/=10
#print(s1)
#print(s2)
#print(s3)
#realvalue = 0.940
#print(abs(realvalue - evaluation(polyfit(points1,3),11)))
#print(abs(realvalue - evaluation(polyfit(points1,4),11)))
#print(abs(realvalue - evaluation(polyfit(points1,5),11)))

s1 = 0
s2 = 0
s3 = 0
for i in range(1,11):
    s1+= abs(evaluation(polyfit(points2,3),i) - points2[i-1])
    s2+= abs(evaluation(polyfit(points2,4),i) - points2[i-1])
    s3+= abs(evaluation(polyfit(points2,5),i) - points2[i-1])
s1/=10
s2/=10
s3/=10
#print(s1)
#print(s2)
#print(s3)
#realvalue = 0.117
#print(abs(realvalue - evaluation(polyfit(points2,3),11)))
#print(abs(realvalue - evaluation(polyfit(points2,4),11)))
#print(abs(realvalue - evaluation(polyfit(points2,5),11)))


#next 5 are 5,6,7,8,11 september 2023

realvalues1 = [0.860,0.785,0.710,0.730,0.660]
realvalues2 = [0.117,0.117,0.117,0.115,0.113]
'''
step = 12
ind = 0
for i in range(5,9):
    print("Error for DOPLER,September",i,"th is ",abs(evaluation(polyfit(points1,3),step) - realvalues1[ind]))
    step+=1
    ind+=1
print("Error for DOPLER,September 11th is ",abs(evaluation(polyfit(points1,3),16) - realvalues1[ind]))

step = 12
ind = 0
for i in range(5,9):
    print("Error for KAIROMEZ,September",i,"th is ",abs(evaluation(polyfit(points2,3),step) - realvalues2[ind]))
    step+=1
    ind+=1
print("Error for KAIROMEZ,September 11th is ",abs(evaluation(polyfit(points2,3),16) - realvalues2[ind]))
'''