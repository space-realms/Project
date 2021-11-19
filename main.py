#Servers contains 
#Controllers (all Local summary of content)
#Cluster+nodes(Content stroes)
#Client PC

#Caching on each nodes(repeated requests)name of node/name of file/numberOfRequests
#Calculate Hops
#Calculate hit ratio

from os.path import exists as file_exists
import math
import string
import random
import sys
import matplotlib.pyplot as plt
import numpy as np


dataSummary3=""
dataSummary2=""

def downloadFromServer(node):
    letters = string.ascii_uppercase
    z=''.join(random.choice(letters) for i in range(10))
    f=open(node,"a")
    f.write(z)
    f.close()
def cluster2(name):
    node1_CS=""
    node2_CS=""
    node3_cs=""
def cluster3(name):
    node1_CS=""
    node2_CS=""
    node3_cs=""
    
def SDNController3(name,hop,node):
    Filefound=False
    path=""  #to be returned

    #data sumamary
    nodeA_CS='Cluster3/node1A_CS/'+name
    nodeB_CS='Cluster3/node2A_CS/'+name
    nodeC_CS='Cluster3/node3A_CS/'+name
    nodeD_CS='Cluster3/node4A_CS/'+name
    nodeE_CS='Cluster3/node5A_CS/'+name
    nodeF_CS='Cluster3/node6A_CS/'+name
    nodeG_CS='Cluster3/node7A_CS/'+name
    nodeH_CS='Cluster3/node8A_CS/'+name
    nodeI_CS='Cluster3/node9A_CS/'+name
    nodeJ_CS='Cluster3/node10A_CS/'+name
    nodeK_CS='Cluster3/node11A_CS/'+name
    nodeL_CS='Cluster3/node12A_CS/'+name
    nodeM_CS='Cluster3/node13A_CS/'+name
    nodeN_CS='Cluster3/node14A_CS/'+name
    nodeO_CS='Cluster3/node15A_CS/'+name
    nodeP_CS='Cluster3/node16A_CS/'+name
    nodeQ_CS='Cluster3/node17A_CS/'+name
    nodeR_CS='Cluster3/node18A_CS/'+name
    nodeS_CS='Cluster3/node19A_CS/'+name
    nodeT_CS='Cluster3/node20A_CS/'+name
    Cluster=[nodeA_CS,nodeB_CS,nodeC_CS,nodeD_CS,nodeE_CS,nodeF_CS,nodeG_CS,nodeH_CS,nodeI_CS,nodeJ_CS,nodeK_CS,nodeL_CS,nodeM_CS,nodeN_CS,nodeO_CS,nodeP_CS,nodeQ_CS,nodeR_CS,nodeS_CS,nodeT_CS]
    #start by node1
    for i in range(len(Cluster)):
        if (file_exists(Cluster[i])==True):
            hop+=len(Cluster)-node+1+i
            path=Cluster[i]
            Filefound=True
            break
    if (Filefound==True):
        return hop,path,True
    else:
        return hop,"",False

def SDNController2(name,hop,node):
    Filefound=False
    path=""  #to be returned
    
    #data sumamary
    nodeA_CS='Cluster2/node1A_CS/'+name
    nodeB_CS='Cluster2/node2A_CS/'+name
    nodeC_CS='Cluster2/node3A_CS/'+name
    nodeD_CS='Cluster2/node4A_CS/'+name
    nodeE_CS='Cluster2/node5A_CS/'+name
    nodeF_CS='Cluster2/node6A_CS/'+name
    nodeG_CS='Cluster2/node7A_CS/'+name
    nodeH_CS='Cluster2/node8A_CS/'+name
    nodeI_CS='Cluster2/node9A_CS/'+name
    nodeJ_CS='Cluster2/node10A_CS/'+name
    nodeK_CS='Cluster2/node11A_CS/'+name
    nodeL_CS='Cluster2/node12A_CS/'+name
    nodeM_CS='Cluster2/node13A_CS/'+name
    nodeN_CS='Cluster2/node14A_CS/'+name
    nodeO_CS='Cluster2/node15A_CS/'+name
    nodeP_CS='Cluster2/node16A_CS/'+name
    nodeQ_CS='Cluster2/node17A_CS/'+name
    nodeR_CS='Cluster2/node18A_CS/'+name
    nodeS_CS='Cluster2/node19A_CS/'+name
    nodeT_CS='Cluster2/node20A_CS/'+name
    
    Cluster=[nodeA_CS,nodeB_CS,nodeC_CS,nodeD_CS,nodeE_CS,nodeF_CS,nodeG_CS,nodeH_CS,nodeI_CS,nodeJ_CS,nodeK_CS,nodeL_CS,nodeM_CS,nodeN_CS,nodeO_CS,nodeP_CS,nodeQ_CS,nodeR_CS,nodeS_CS,nodeT_CS]
    #start by node1
    for i in range(len(Cluster)):
        if (file_exists(Cluster[i])==True):
            hop+=len(Cluster)-node+1+i
            path=Cluster[i]
            Filefound=True
            break
    if (Filefound==True):
        return hop,path,"True"
    else:  #Checking summary of SDN2,SDN3,....
        return 0,"",False
    
def SDNController1(name,hop,node):
    Filefound=False
    path=""  #to be returned

    #data sumamary
    nodeA_CS='Cluster1/node1A_CS/'+name
    nodeB_CS='Cluster1/node2A_CS/'+name
    nodeC_CS='Cluster1/node3A_CS/'+name
    nodeD_CS='Cluster1/node4A_CS/'+name
    nodeE_CS='Cluster1/node5A_CS/'+name
    nodeF_CS='Cluster1/node6A_CS/'+name
    nodeG_CS='Cluster1/node7A_CS/'+name
    nodeH_CS='Cluster1/node8A_CS/'+name
    nodeI_CS='Cluster1/node9A_CS/'+name
    nodeJ_CS='Cluster1/node10A_CS/'+name
    nodeK_CS='Cluster1/node11A_CS/'+name
    nodeL_CS='Cluster1/node12A_CS/'+name
    nodeM_CS='Cluster1/node13A_CS/'+name
    nodeN_CS='Cluster1/node14A_CS/'+name
    nodeO_CS='Cluster1/node15A_CS/'+name
    nodeP_CS='Cluster1/node16A_CS/'+name
    nodeQ_CS='Cluster1/node17A_CS/'+name
    nodeR_CS='Cluster1/node18A_CS/'+name
    nodeS_CS='Cluster1/node19A_CS/'+name
    nodeT_CS='Cluster1/node20A_CS/'+name
    NodesOfCluster=[nodeA_CS,nodeB_CS,nodeC_CS,nodeD_CS,nodeE_CS,nodeF_CS,nodeG_CS,nodeH_CS,nodeI_CS,nodeJ_CS,nodeK_CS,nodeL_CS,nodeM_CS,nodeN_CS,nodeO_CS,nodeP_CS,nodeQ_CS,nodeR_CS,nodeS_CS,nodeT_CS]
    #start by node1
    for i in range(len(NodesOfCluster)):
        if (file_exists(NodesOfCluster[i])==True):
            hop+=len(NodesOfCluster)-node+1+i
            path=NodesOfCluster[i]
            Filefound=True
            break
    if (Filefound==True):
        return hop,path
    else:  #Checking summary of SDN2,SDN3,....
        hop+=len(NodesOfCluster)
      
        hop,path,x=SDNController2(name,hop,node)
        if (x==False): #sdn2  
            hop+=2*len(NodesOfCluster)
            hop,path,x=SDNController3(name,hop,node)
            if (x==False): #sdn3 
                 return hop,"False"
            else: #found on sd3  
                return hop,path
        else: #found on sdn2
            return hop,path

    
        
#Inform here how many nodes available here
#Cache Hit ratio should be returned
def cluster1(name,node,hop):
    path=''
    loc='Cluster1/node'+str(node)+'A_CS/'+name
    if (file_exists(loc)==True):
        print("\nCache Hit")
        f=open("Cache/cache.txt","w")
        f.write("1")
        f.close()
        hop+=1
        loc=loc+"@12"
        return hop,loc     
    else:
        hop,path=SDNController1(name,hop,node)
        return hop,path

    
def user(name,node):
    hopping=0
    hop,path=cluster1(name,node,hopping)
    loc='Cluster1/node'+str(node)+'A_CS/'+name
    if path=="False":
        downloadFromServer(loc)
        hop=hop*3
        print("\nCache Miss:::::::provided by server")
        print("Stretch:: ("+name+") "+str(hop/hop))
        print("Total Hops from request to Content node = "+str(hop))
        print("Total Hops from node to Server = "+str(hop))
        return 0
    else:
        if not "@12" in path:
            print("\nCache Miss")
            print("Stretch:: ("+name+") "+str(round(hop/(hop*3),2)))
            print("Total Hops from request to Content node = "+str(hop))
            print("Total Hops from node to Server = "+str(hop*3))
            print("Path = "+path+"\n")
        else:
            path=path.replace("@12","")
            print("Stretch:: ("+name+") "+str(round(hop/(hop*15),2)))
            print("Total Hops from request to Content node = "+str(hop))
            print("Total Hops from node to Server = "+str(hop*15))
            print("Path = "+path+"\n")
        return 1

        
def main(names,node):
    Cache_HIT=0
    Cache_MISS=0

    for i in range(len(names)):
        name=names[i]
        if user(name,node)==1:
            f=open("Cache/cache.txt","r")
            z=f.readlines()[0]
            if (z=='1'):
                Cache_HIT+=1
            
    Cache_MISS=len(names)-Cache_HIT
    print("\nCache Hit Ratio ::")
    print("Total Hits: "+str(Cache_HIT))
    print("Total Misses: "+str(Cache_MISS))
    print("Ratio : "+str(round(Cache_HIT/(Cache_HIT+Cache_MISS),2)))

if __name__ == '__main__':
   File_names = []
   print("Node number = ", int(sys.argv[len(sys.argv)-1]))
   print("Number of requests = ", len(sys.argv)-2,"\n")
   n = len(sys.argv)
   if n<=2:
       print("\nError Message:")
       print("Invalid number of arguments")
   elif (sys.argv[1]==""):  #file name
       print("\nError Message:")
       print("File name not specified")
   elif (int(sys.argv[len(sys.argv)-1])>20 or int(sys.argv[len(sys.argv)-1])<1): #node number     
        print("\nError Message:")
        print("Invalid Node number")    
   else:
       name=sys.argv[1]
       node=sys.argv[len(sys.argv)-1]
       requests=len(sys.argv)-2
       try:
           node=int(node)
       except:
           print("Plz enter integer number for node")
       for i in range(1, len(sys.argv)-1):
           File_names.append(sys.argv[i])
       main(File_names,node)

       #clear cache for next run
       f=open("Cache/cache.txt","w")
       f.write("clear")
       f.close()
        
    






    
    
    


