from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import *
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler  
from sklearn.preprocessing import StandardScaler
 
class SVM:

    def __init__(self, dataset_path):

        self.dataset_path = dataset_path
        data = pd.read_csv(self.dataset_path)

        # X-> Contains the features
        self.X = data.iloc[:, 0:-1]
        # y-> Contains all the targets
        self.y = data.iloc[:, -1]

    def solve(self):
        """
        Build an SVM model and fit on the training data
        The data has already been loaded in from the dataset_path

        Refrain to using SVC only (with any kernel of your choice)

        You are free to use any any pre-processing you wish to use
        Note: Use sklearn Pipeline to add the pre-processing as a step in the model pipeline
        Refrain to using sklearn Pipeline only not any other custom Pipeline if you are adding preprocessing

        Returns:
            Return the model itself or the pipeline(if using preprocessing)
        """

        # TODO
        pipeline=Pipeline([("Scaler",MinMaxScaler()),("Classifier",SVC(kernel="rbf",gamma="scale",C=4))])
        
        pipeline.fit(self.X,self.y)
        
        return pipeline
        #linear kernel with minmaxscaler,64.89% accuracy
        #linear kernel with standardscaler,65.04% accuracy
        #rbf kernel with minmaxscaler,89.48% accuracy
        #rbf kernel with standardscaler,90.22% accuracy
        #polynomial kernel with minmaxscaler,85.04% accuracy
        #polynomial kernel with standardscaler,81.33% accuracy
        #sigmoid kernel with mimmaxscaler,36.44% accuracy
        #sigmoid kernel with standardscaler,44.30%% accuracy
        #c=5,89.78% accuracy
        #c=3,89.63% accuracy
        #rbf kernel with c=4 and gamma="scale" is the best model