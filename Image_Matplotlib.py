
import matplotlib.pyplot as plt


#load cifar10 data with 10 classes
from keras.datasets import cifar10
import numpy as np

#you can use this data for testing the code
classes = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Download CIFAR train and test data
(Xtrain, Ytrain), (Xtest, Ytest) = cifar10.load_data()


#making subplot 
plt.figure(figsize=(12,4))
for i in range(18):
    idx = np.random.randint(7500)
    label = Ytrain[idx,0]
    
    plt.subplot(3,6,i+1)
    plt.tight_layout()
    plt.imshow(Xtrain[idx])
    plt.title("Class: {} ({})".format(label, classes[label]))
    plt.axis('off')
fig.savefig("Classes.png")  #saving figure
plt.show()         #showing plot 


