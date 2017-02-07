
# coding: utf-8

# # Axis Function

# This function calculates the mean and standard deviation of a dataset along a specified axis.

# In[124]:

import numpy as np

# Create a dataset with numbers and two axes

arr = np.array([[1,2,3,4,5,6,7,8,9,10],[1,2,5,23,78,12,34,89,12,1]])


# In[125]:

#print arr
        


# In[126]:

def calc_axis(arr,x = 0):

    return np.mean(arr,axis = x),  np.std(arr,axis = x)


# In[127]:

# # Function output for axis 0

# m , sd = calc_axis(arr,0)

# print "The mean is : " + str(m)
# print "The standard deviation is : " + str(sd)


# In[128]:

# # Function output for axis 1

# m , sd = calc_axis(arr,1)

# print "The mean is : " + str(m)
# print "The standard deviation is : " + str(sd)


# In[129]:

# # Function output for axis 'None'

# m , sd = calc_axis(arr, x = None)

# print "The mean is : " + str(m)
# print "The standard deviation is : " + str(sd)


# In[130]:

# # Function output for default axis (zero)

# m , sd = calc_axis(arr)

# print "The mean is : " + str(m)
# print "The standard deviation is : " + str(sd)

