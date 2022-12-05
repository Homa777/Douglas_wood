# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:00:35 2022

@author: Diana
"""

## Question 2

# from matplotlib_venn import venn3
# from matplotlib import pyplot as plt


# venn3(subsets=[0.38, 0.40,0.12,0.37,0.10,0.14,0.06],set_labels=['TikTok', 'Instagram', 'Other platforms'], set_colors=['red', 'blue', 'green'])
# plt.show()


## Question 4
# part a
# importing module
# from pandas import *
# import numpy as np
 
# # reading CSV file
# data = read_csv("wood.csv")
 
# # converting column data to list to make a dataset of 100 wood loads
# loads = data['load'].tolist()
# loads=np.array(loads)
# print('loads:', loads)

# #importing required libraries

# #importing required libraries
# from matplotlib import pyplot as plt
# import numpy as np

# # A dataset of 10 students

# fig, axis = plt.subplots(figsize =(20, 10))
# axis.hist(loads, bins=[28914.799,29161.018,29407.237,29653.456,29899.675,30145.894,30392.113,30638.332,30884.551,31130.77],align='mid', color='yellow', edgecolor='black', linewidth=2)

# # Displaying the graph
# plt.show()

# # Does it appear safe to assume the normality condition is satisfied?
# import numpy as np
# standard_deviation = np.std(loads, ddof=1)
# print("standard_deviation=",standard_deviation )


# #part b 

# import scipy.stats as st
  
  
# # create 99% confidence interval
# # for population mean weight
# A=st.norm.interval(alpha=0.99, 
#                   loc=np.mean(loads),
#                   scale=st.sem(loads))

# print("99% confidence interval=",A)

## Question 5
import numpy as np

def bootstrap(data, n=1000, func=np.mean):
    simulations = list()
    sample_size = len(data)
    
    for c in range(n):
        itersample = np.random.choice(data, size=sample_size, replace=True)
        simulations.append(func(itersample))
    simulations.sort()
# Define a function to return 2-sided symmetric confidence interval specified by p=95% 
# bootstrap confidence interval
    def ci(p):
        u_pval = (1+p)/2.
        l_pval = (1-u_pval)
        l_indx = int(np.floor(n*l_pval))
        u_indx = int(np.floor(n*u_pval))
        return(simulations[l_indx], simulations[u_indx])
    return(ci)
# calling function
v = [30, 30, 42, 35, 22, 33, 31, 29, 19, 23]
boot = bootstrap(v, 1000)
print("confidence interval specified by p=95% is = ", boot(0.95) )