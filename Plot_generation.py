import numpy as np 
import matplotlib.pyplot as plt 
  
X = ['Tensorflow','Resnet','Pytorch']
X_val = [20.33, 16.53,7.93]
Y_val = [15.25,7.42,3.71]
Z_val = [0,2.91,1.42]
  
X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, X_val, 0.4, label = '')
plt.bar(X_axis + 0.2, Y_val, 0.4, label = '')
plt.bar(X_axis + 0.4, Z_val, 0.4, label = '')
  
plt.xticks(X_axis, X)
plt.ylabel("Execution Time")
plt.title("Ml Model Execution Time - AWS Lambda")
plt.legend()
plt.show()
