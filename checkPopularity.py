from csv import reader
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np


def plots(reader,NodeArray,node):
    #matplotlib array
    x_values=[]
    y_values=[]
    


    ###
    totalFILESOnNode=0
    i=0
    filename="Contents Popularity.csv"
    f=open(filename,'r')
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        if(i>0):
            if row[2]==str(node):
                totalFILESOnNode+=1
        i+=1
    if (totalFILESOnNode<4):
        print("Not enough Record")
        return None
    f=open(filename,'r')
    reader = csv.reader(f, delimiter="\t")
    for row1 in reader:
        if (totalFILESOnNode==0):
            break
        if row1[2]==str(node):
            x_values.append(str(row1[0]))
            y_values.append(eval(row1[4]))
            totalFILESOnNode-=1

    x = np.array(x_values)
    y = np.array(y_values)
    plt.bar(x,y)
    plt.title("Node "+str(node)+" Popularity")
    plt.show()        
            
        

def main(node):
    i=0
    AllNodes=[]
    Files=[]
    name=""
    filename="Contents Popularity.csv"
    f=open(filename,'r')
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        i+=1
        if(i>1):
            if not int(row[2]) in AllNodes:
                AllNodes.append(int(row[2]))
                
    if not node in AllNodes:
        print("No Record for this node")
        return
    else:
        #plots on Node array            
        plots(reader,AllNodes,node)
    f.close()


if __name__ == '__main__':
    node=eval(sys.argv[1])
    main(node)
    n = len(sys.argv)
    if n>2:
        print("Invalid number of arguments")

    

