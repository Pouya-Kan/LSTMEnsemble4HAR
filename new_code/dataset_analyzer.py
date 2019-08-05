# Added by Pouya

import scipy.io
import pandas as pd

file_dir = '../'
mat_file = file_dir + 'Ensemble-datasets/PAMAP2.mat'
data = scipy.io.loadmat(mat_file)

X_train = data['X_train']
X_valid = data['X_valid']
X_test = data['X_test']
y_train = data['y_train'].reshape(-1)
y_valid = data['y_valid'].reshape(-1)
y_test = data['y_test'].reshape(-1)

y_train = pd.get_dummies(y_train, prefix='labels')
y_valid = pd.get_dummies(y_valid, prefix='labels')
y_test = pd.get_dummies(y_test, prefix='labels')

print('the PAMAP2 dataset was normalized to zero-mean, unit variance')
print('loading the 33HZ PAMAP2 52d matData successfully . . .')

print(X_train[0:5])
