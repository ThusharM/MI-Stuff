'''
Assume df is a pandas dataframe object of the dataset given
'''

import numpy as np
import pandas as pd
import random
eps = np.finfo(float).eps


'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float
def get_entropy_of_dataset(df):
    # TODO
    Class=df.keys()[-1]
    entropy=0
    values=df[Class].unique()
    for value in values:
        fraction=df[Class].value_counts()[value]/len(df[Class])
        entropy+=-fraction*np.log2(fraction)
        
    return entropy



'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    # TODO
    Class = df.keys()[-1]   #To make the code generic, changing target variable class name
    target_variables = df[Class].unique()  #This gives all 'Yes' and 'No'
    variables = df[attribute].unique()    #This gives different features in that attribute (like 'Hot','Cold' in Temperature)
    entropy2 = 0
    for variable in variables:
        entropy = 0
        for target_variable in target_variables:
            num = len(df[attribute][df[attribute]==variable][df[Class] ==target_variable])
            den = len(df[attribute][df[attribute]==variable])
            fraction = num/(den+eps)
            entropy += -fraction*np.log2(fraction+eps)
        fraction2 = den/len(df)
        entropy2 += -fraction2*entropy
    avg_info=abs(entropy2)
    return avg_info


'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    # TODO
   
  
        
    information_gain=get_entropy_of_dataset(df)-get_avg_info_of_attribute(df,attribute)   
    return information_gain

def get_attr_with_max_ig(df):
    keys=df.keys()[:-1]
    IG=[]
    for key in keys:
        IG.append(get_entropy_of_dataset(df)-get_avg_info_of_attribute(df,key))
    return keys[np.argmax(IG)]    
    


#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    # TODO
    keys=df.keys()[:-1]
    dictionary={}
    for key in keys:
        dictionary[key]=get_information_gain(df,key) 
    attr=get_attr_with_max_ig(df)
    return (dictionary,attr)    
          
    pass
