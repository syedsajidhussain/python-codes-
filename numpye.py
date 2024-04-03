#Numpy is a general-purpose array-processing package.
import numpy as np
lst1=[1,2,3,4]
lst2=[5,6,7,8]
lst3=[20,11,0,1]
arr=np.array([lst1,lst2,lst3])
arr

#creating array from tuple

arr1=np.array((9,8,7,6))
arr1


arr1[1:] #start from  element located at index 1

arr1[:1]# start but end at location 1 but dont include index 1

arr[1:3, 1:2]

arr1[::2] #start,end, stepsize


a1=arr.reshape(4,3)
a1



a1[1:2,:2]
a1+=1


#Exploratory Data Analysis
arr
arr[arr<12]

##mechanism to create an array
np.arange(1,20,2).reshape(2,5)

##mechanism to create a 1D array 
np.arange(1,20,2).reshape(2,5,1)


arr1*arr1

np.ones((5,4))

np.zeros((4,5))


np.random.randint(10,50,4).reshape(2,2)

np.random.randn(5,6)




