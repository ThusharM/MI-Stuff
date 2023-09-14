"""
You can create any other helper funtions.
Do not modify the given functions
"""
def s_h(fr,pth):
        for indx in range(len(fr)):
                if fr[indx][1]==pth:
                        return pth


def A_star_Traversal(cost, heuristic, start_point, goals):
	"""
	Perform A* Traversal and find the optimal path 
	Args:
		cost: cost matrix (list of floats/int)
		heuristic: heuristics for A* (list of floats/int)
		start_point: Staring node (int)
		goals: Goal states (list of ints)
	Returns:
		path: path to goal state obtained from A*(list of ints)
	"""
	v=[]
	
	path = [start_point]
	fr_val=[[heuristic[start_point],path]]
	while len(fr_val)>0:
                c_cost,c_path=fr_val.pop(0)
                n=c_path[-1]
                if n in goals:
                        return c_path
                v.append(n)
                k=[i for i in range(len(cost[0])) if cost[n][i] not in [0,-1]]
                for i in k:
                        n_c_pth=c_path+[i]
                        n_pth_cst=c_cost+cost[n][i]+heuristic[i]
                        if i not in v and n_c_pth not in [i[1] for i in fr_val]:
                                fr_val.append((n_pth_cst,n_c_pth))
                                fr_val=sorted(fr_val,key=lamda x:(x[0],x[1]))
                        elif n_c_pth in [i[1] for i in fr_val]:
                                indx=s_h(fr_val,n_c_pth)
                                fr_val[indx][0]=min(fr_val[indx][0],n_pth_cst)
                                fr_val=sorted(fr_val,key=lamdax:(x[0],x[1]))

	# TODO
	
	return path

def d_h(g,i,pth_lst,v,end):
    v[i]=1
    pth_lst.append(i)
    if(i not in end):
            dst=g[i]
            for k in range(len(dst)):
                    if(dst[k]>0 and v[k]==0):
                            end_value=d_h(g,k,pth_lst,v,end)
                            if(end_value==-1):
                                    return -1
                                    
                   
                            pth_lst.pop()
    else:
             return -1

def DFS_Traversal(cost, start_point, goals):
	"""
	Perform DFS Traversal and find the optimal path 
		cost: cost matrix (list of floats/int)
		start_point: Staring node (int)
		goals: Goal states (list of ints)
	Returns:
		path: path to goal state obtained from DFS(list of ints)
	"""
	path = []
	# TODO
	v=[0 for i in range(len(cost[start_point]))]
	d_h(cost,start_point,path,v,goals)
	return path
     
	
