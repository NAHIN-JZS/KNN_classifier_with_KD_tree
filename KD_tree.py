# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 22:31:39 2022

@author: Nahin
"""

import math
#from queue import PriorityQueue
#import heapq

#root_node = None

class Node:
    def __init__(self,x_val,y_val,class_value=0,parent=None):
        self.root = parent
        self.ls = [x_val,y_val]
        self.class_value = class_value
        self.right = None
        self.left = None
        
    

class KNN:
    def __init__(self,k,no_of_class):
        self.no_of_class = no_of_class
        self.k = k
        self.root_node = None
        self.KD_tree = None
        self.nearest_points=[]
        self.k_nearest_points = []
        
        
            
        
    def create_KD_tree(self,root,depth, x_value = None, y_value = None,class_value=None, dimention = 2):
        newNode = Node(parent=root,x_val= x_value,y_val= y_value,class_value=class_value)
        
        
        if ( self.root_node == None):
            self.root_node = newNode
        if(root == None):
            
            return newNode
        else:
            root = self.root_node
            
            #while(1): 
            i=0
            while(1): 
                current_dimention = i % dimention
                print("depth: ",i)
                print("dim: ",current_dimention)
                print(root.ls[current_dimention])
                print(newNode.ls[current_dimention])
                i=i+1
                if(root.ls[current_dimention] > newNode.ls[current_dimention]):
                    if(root.left == None):    
                        root.left = newNode
                        break
                    else:
                        root = root.left
                else:
                    if(root.right == None):    
                        root.right = newNode
                        break
                    else:
                        root = root.right
                
                #break    
        return self.root_node
    
    def fit(self,data_points):
        #total_points = len(data_points)
        for x,y,z in data_points:
            self.KD_tree = self.create_KD_tree(self.KD_tree,0,x,y,z)

    def euclidien_distance(self,node1,node2):
        x1=int(node1.ls[0])
        x2=int(node2.ls[0])
        
        y1=int(node1.ls[1])
        y2=int(node2.ls[1])
        
        dis = math.sqrt((x1-x2)**2+(y1-y2)**2)
        print(dis, node1.ls)
        return dis

    def nearest_point_detect(self,valueNode):
        nearest_point = self.euclidien_distance(self.root_node, valueNode)
        print(nearest_point)
        root = self.root_node
        while(1):
            temp_root = root
            if(root.left != None):
                left_distance = self.euclidien_distance(root.left, valueNode)
                if(left_distance <= nearest_point):
                    nearest_point = left_distance
                    temp_root = root.left
                    
                    
                    
            if(root.right != None):
                right_distance = self.euclidien_distance(root.right, valueNode)
                if(right_distance <= nearest_point):
                    nearest_point = right_distance
                    temp_root = root.right
                    
            if(temp_root == root):
                #if(temp_root in self.nearest_points): #checking if it is already taken or not
                if(left_distance < right_distance):
                    root = root.left
                    self.k_nearest_points.append([left_distance,root])
                    #heapq.heappush(self.nearest_points, (nearest_point,root))
                    continue
                else:
                    root = root.right
                    self.k_nearest_points.append([right_distance,root])
                    #heapq.heappush(self.nearest_points, (nearest_point,root))
                    continue
                break
            #else   
            
            
            root = temp_root
            self.k_nearest_points.append([nearest_point,root])
            
                
            if(root.left == None and root.right == None):
                break
        #print(root.ls)
        self.k_nearest_points.sort(key=(lambda x:x[0]))
    
    def predict(self,testNode):
        #for i in range(self.k):    
        self.nearest_point_detect(testNode)
        #self.nearest_points.append(near_point)
        predicted_class = self.k_points()
        print("predicted class: ",predicted_class)
        
    def k_points(self):
        #kk= len(self.k_nearest_points)
        kk = self.k
        class_counter = [0] * self.no_of_class
        for i in range(0,kk):
            print(i)
            dis = self.k_nearest_points[i][0]
            node = self.k_nearest_points[i][1]
            class_counter[node.class_value] = class_counter[node.class_value] +1
             
            print("Distance : ",dis)
            print("node : ",node.ls)
            print("class : ",node.class_value)
        
        max_val = max(class_counter)
        selected_class = class_counter.index(max_val) #as has the maximum count
        print("max_count :", max_val)
        
        return selected_class
            
    
                    

        
    

points = [(12,15,0),(5,6,1),(21,24,1),(2,3,1),(13,6,0),(10,9,0),(1,2,0),(14,29,1),(15,10,0)]

model = KNN(k=3,no_of_class=2)
model.fit(points)

#euclidien_distance((12,15), ())
        
        
        
    