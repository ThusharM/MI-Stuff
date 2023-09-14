import numpy as np
def f1(X1,coef1,X2,coef2,seed1,seed2,seed3,shape1,shape2):
	#note: shape is of the forest (x1,x2)
	#return W1 x (X1 ** coef1) + W2 x (X2 ** coef2) +b
	# where W1 is random matrix of shape shape1 with seed1
   
    np.random.seed(seed1)
    W1=np.random.rand(*shape1)
	# where W2 is random matrix of shape shape2 with seed2
    np.random.seed(seed2)
    W2=np.random.rand(*shape2)
    ans=np.dot(W1,np.linalg.matrix_power(X1,coef1))+np.dot(W2,np.linalg.matrix_power(X2,coef2))
	# where B is a random matrix of comaptible shape with seed3
    shape_ans=np.shape(ans)
    print(shape_ans)
    np.random.seed(seed3)
    #B=np.random.rand(shape_ans)
	# if dimension mismatch occur return -1
    
    
    
    #ans+=B
    
    ''' if(ans):
        
        return ans
    else:
	
        return -1

 '''
f1(np.array([[1,2],[3,4]]),3,np.array([[1,2],[3,4]]),2,1,2,3,(3,2),(3,2))
