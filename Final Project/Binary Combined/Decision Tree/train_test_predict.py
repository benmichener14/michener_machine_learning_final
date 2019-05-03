import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz 

# use the following commands first:
# sudo pip3 install pydot 
# sudo apt-get install graphviz
import pydot 

X = np.loadtxt('Com_X.csv',skiprows=1, unpack=False, delimiter=',')
y = np.loadtxt('Com_Y.csv',skiprows=1, unpack=False, delimiter=',')
#names = np.loadtxt('words.csv',skiprows=0, unpack=False, dtype=str)

nameKey = open("words.csv", mode="r")

names = []
for name in nameKey:
    names.append(name)



mvp = {"data" : X, "target" : y, "target_names" : names}
X_train , X_test , y_train , y_test = train_test_split(mvp["data"], mvp["target"], stratify=mvp["target"], random_state=42) 

print('Training...')
tree1 = DecisionTreeClassifier( random_state = 0 )
tree2 = DecisionTreeClassifier( max_depth = 5, random_state = 0 )
tree1.fit (X_train, y_train ) 
tree2.fit (X_train, y_train ) 

print('Testing...')
print("Accuracy on training set: {:.3f}".format(tree1.score( X_train , y_train)))
print( "Accuracy on test set: {:.3f}".format(tree1.score( X_test , y_test)))
print("Accuracy on training set with pruning: {:.3f}".format(tree2.score( X_train , y_train)))
print( "Accuracy on test set with pruning: {:.3f}".format(tree2.score( X_test , y_test)))

print( "Feature importances: \n {}".format (tree2.feature_importances_ )) 


# now create a bar chart and save it to a file
n_features = mvp["data"].shape[ 1 ] 
plt.barh( range( n_features ), tree2.feature_importances_ , align = 'center' ) 
plt.yticks( np.arange( n_features ), mvp['target_names'] ) 


export_graphviz(tree2 , out_file = "tree.dot", class_names = [ "Not Spam" , "Spam" ], feature_names = mvp["target_names"] , impurity = False , filled = True ) 

(graph,) = pydot.graph_from_dot_file('./tree.dot')
graph.write_png('./tree.png')




