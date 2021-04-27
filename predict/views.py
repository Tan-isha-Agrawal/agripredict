from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults2
import numpy as np
from numpy.linalg import inv

def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        area = float(request.POST.get('area'))
        Fertilizers = float(request.POST.get('Fertilizers'))
        Rainfall = float(request.POST.get('Rainfall'))
        Storage = float(request.POST.get('Storage'))
        Electricity = float(request.POST.get('Electricity'))
       # yeild = float(request.POST.get('yeild'))



        data = pd.read_csv('E:\python\YT-Django-Iris-App-3xj9B0qqps-master - Copy\predict\MVRprices1.csv') 
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
        inp=[area,Fertilizers,Rainfall,Storage,Electricity]
        print(inp,x_test)
        for j in range (5):
            
            x_test.append([inp[j]])
        
        print(x_test)

        for i in range(5):
            x_test[i+1][0]=(x_test[i+1][0]-min[i])/(max[i]-min[i])
        x_test=np.matrix(x_test)
        Y1=np.matmul(c1.T,x_test)

        print(Y1*(max[-1]-min[-1])+min[-1])
        k= Y1*(max[-1]-min[-1])+min[-1]
        #area,Fertilizers,Rainfall,Storage,Electricity,yeild,Prices
        # Unpickle model
        #model = pd.read_pickle(r"E:\python\YT-Django-Iris-App-3xj9B0qqps-master\new_model.pickle")
        # Make prediction
       # result = model.predict([[area,Fertilizers,Rainfall,Storage,Electricity,yeild]])

        yeild = float(k)
        print(float(k))

        
        data1 = pd.read_csv('E:\python\YT-Django-Iris-App-3xj9B0qqps-master - Copy\predict\MVRprices.csv') 
        colums1 = (data1.columns[0])
        #finding minimum and maximum fom each column
        max= [data1[c].max() for c in data1.columns] 
        min= [data1[c].min() for c in data1.columns]
        i=0
        #print(max,min)
        #normalizing the data
        for c in data1.columns:
            while(i<len(data1.columns)): 
              data1[c]=(data1[c]-min[i])/(max[i]-min[i])
              i=i+1
              break
        #print(data)
        arr1 = data1.values
        #print(arr)
        #Now, split the dataset and store the features and target values in different list. Here, I have stored the features in x_train list and the target values in y1.
        x_train1=[]
        y11=[]
        a1=data1.shape
        for i in range(a1[0]):                      
            x_train1.append((arr1[i][:-1]).tolist())
    
            y11.append(arr1[i][-1])
        #Concatenate the x_train list with matrix of 1ˢ and compute the coefficient matrix using the normal equation . numpy built-in functions for matrix operations.
        #Input the test data and thereby store it in a list, x_test. Predict the target variable using the test data and the coefficient matrix and thereby stored the result in Y1
        m1=np.ones((12,1))
        b1=np.matrix(x_train1)
        b1=np.concatenate((m1,b1),axis=1)     
        d1=b1.T#transpose
        e1=np.linalg.inv(np.matmul(d1,b1))#inverse
        y11=np.matrix(y11)
        y11=y11.T
        f1=np.matmul(e1,d1)
        c11=np.matmul(f1,y11)
        x_test1=[[1],]
        inp1=[area,Fertilizers,Rainfall,Storage,Electricity,yeild]
        print(inp1,x_test1)
        for j in range (6):
            
            x_test1.append([inp1[j]])
        
        print(x_test1)

        for i in range(6):
            x_test1[i+1][0]=(x_test1[i+1][0]-min[i])/(max[i]-min[i])
        x_test1=np.matrix(x_test1)
        Y11=np.matmul(c11.T,x_test1)

        print(Y11*(max[-1]-min[-1])+min[-1])
        k1= Y11*(max[-1]-min[-1])+min[-1]
        #area,Fertilizers,Rainfall,Storage,Electricity,yeild,Prices
        # Unpickle model
        #model = pd.read_pickle(r"E:\python\YT-Django-Iris-App-3xj9B0qqps-master\new_model.pickle")
        # Make prediction
       # result = model.predict([[area,Fertilizers,Rainfall,Storage,Electricity,yeild]])

        prices = float(k1)
        print(float(k1))

        PredResults2.objects.create(area=area,Fertilizers=Fertilizers,Rainfall=Rainfall,Storage=Storage,Electricity=Electricity,yeild=yeild, prices=prices)

        return JsonResponse({'prices': prices,'area' : area,'Fertilizers' : Fertilizers,'Rainfall' : Rainfall, 'Storage' : Storage,'Electricity' : Electricity, 'yeild': yeild },
                            safe=False)

def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults2.objects.all()}
    return render(request, "results.html", data)
