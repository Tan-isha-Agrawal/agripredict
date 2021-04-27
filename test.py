import pandas as pd 
import numpy as np
from numpy.linalg import inv

data = pd.read_csv('MVRprices.csv') 
colums = (data.columns[0])
#finding minimum and maximum fom each column
max= [data[c].max() for c in data.columns] 
min= [data[c].min() for c in data.columns]
i=0
#print(max,min)
#normalizing the data
for c in data.columns:
    while(i<len(data.columns)): 
        data[c]=(data[c]-min[i])/(max[i]-min[i])
        i=i+1
        break
#print(data)
arr = data.values
#print(arr)
#Now, split the dataset and store the features and target values in different list. Here, I have stored the features in x_train list and the target values in y1.
x_train=[]
y1=[]
a=data.shape
for i in range(a[0]):                      
    x_train.append((arr[i][:-1]).tolist())
    
    y1.append(arr[i][-1])
#Concatenate the x_train list with matrix of 1ˢ and compute the coefficient matrix using the normal equation . numpy built-in functions for matrix operations.
#Input the test data and thereby store it in a list, x_test. Predict the target variable using the test data and the coefficient matrix and thereby stored the result in Y1
m=np.ones((12,1))
b=np.matrix(x_train)
b=np.concatenate((m,b),axis=1)     
d=b.T#transpose
e=np.linalg.inv(np.matmul(d,b))#inverse
y1=np.matrix(y1)
y1=y1.T
f=np.matmul(e,d)
c1=np.matmul(f,y1)
x_test=[[1],]
for j in range (6):
    inp=[float(input("Enter Value:"))]
    x_test.append(inp)
for i in range(6):
    x_test[i+1][0]=(x_test[i+1][0]-min[i])/(max[i]-min[i])
x_test=np.matrix(x_test)
Y1=np.matmul(c1.T,x_test)

print(Y1*(max[-1]-min[-1])+min[-1])


