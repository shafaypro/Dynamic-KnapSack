# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:48:01 2017

@author: Shafay.Amjad

"""

import time

class KnapSack:
    cache = {}
    """ A simple Representation for a KnapStack class which would be used
    to solve in the dynamic Knapsack cost optimizaions
    """
    def __init__(self):
        print("--KnapStack Instance--")
    
    
    def total_value(self, items, max_weight):
        return  sum([x[2] for x in items]) if sum([x[1] for x in items]) < max_weight else 0
    
    # cache = {}
    def solve(self, items, max_weight):
        if not items:
            return ()
        if (items,max_weight) not in self.cache:
            head = items[0]
            tail = items[1:]
            include = (head,) + self.solve(tail, max_weight - head[1])
            dont_include = self.solve(tail, max_weight)
            if self.total_value(include, max_weight) > self.total_value(dont_include, max_weight):
                answer = include
            else:
                answer = dont_include
            self.cache[(items,max_weight)] = answer
        return self.cache[(items,max_weight)]
    
    # Accepts the list of knapsack requirements ID or names , weights , value 
    
    # Shaping the result data set 
    def create_knap_tuple(self, *args):
        no_of_args = len(args) # number of arguments
        if no_of_args == 3:    
            master_list = [tuple(i) for i in zip(args[0], args[1], args[2])]
            return tuple(master_list) # Re
        else:
            print("Invalid number of arguments passed in knap sack")
        
    
    # Applying knap sack problem
    # Access max_weight : cost limit  , master_list= items tupple()
    # Returns three arguments 
    def apply_knap_sack(self,max_weight, master_list = None):
        if master_list is not None: 
            solution = self.solve(master_list, max_weight)
            item_on_list = []
            for x in solution:
                item_on_list.append(x[0])
            print("value:", self.total_value(solution, max_weight))
            print ("weight:", sum([x[1] for x in solution]))
            return item_on_list, self.total_value(solution, max_weight), sum([x[1] for x in solution])
        else:
            print("There isn't any knapsack data list being passed in there. ")
            time.sleep(2) # ERROR pause to show the error


# Testing case 1
def test():
    KS = KnapSack() # Created the knap sack object
    items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )            
    items_on, value, weight = KS.apply_knap_sack(max_weight=400,master_list=items)
    print(items_on,value,weight)
# Testing Case 2
def test2():
    list1 = [' map ',' compass ',' water ',' sandwich ',' glucose ',' tin ',' banana ',' apple ',' cheese ',' beer ',' suntan cream ',' camera ',' t-shirt ',' trousers ',' umbrella ',' waterproof trousers ',' waterproof overclothes ',' note-case ',' sunglasses ',' towel ',' socks ',' book ']
    list2 = [9 ,13 ,153 ,50 ,15 ,68 ,27 ,39 ,23 ,52 ,11 ,32 ,24 ,48 ,73 ,42 ,43 ,22 ,7 ,18 ,4 ,30]
    list3 = [150 ,35 ,200 ,160 ,60 ,45 ,60 ,40 ,30 ,10 ,70 ,30 ,15 ,10 ,40 ,70 ,75 ,80 ,20 ,12 ,50 ,10]
        
    KS = KnapSack() # Created the knap sack object
    # Converting the Knap Sack it
    master_tuple = tuple(KS.create_knap_tuple(list1,list2,list3))
    items_on, value, weight = KS.apply_knap_sack(max_weight=400,master_list=master_tuple)
    print(items_on,value,weight)
def guide():
    print("1 - Create KnapSack Instance : \n\tKS = KnapSack() ")
    print("2 - If your data is not in form of tuple of tuple instead its seperate lists then :  ")
    print("3 - Apply lists zipping by passing in all three lists as : \n \tmaster_tuple = tuple(KS.create_knap_tuple(list1,list2,list3))")
    print("4 - Apply knap stack on the dataset to get three parameters in reuturn : \n\titems_on, value, weight = KS.apply_knap_sack(max_weight=400,master_list=master_tuple)")
    print("4.1 : items_on :  names or numbers of the items which were considered in getting the optimized best result")
    print("4.2 : value : value achieved best in case of specific weight")
    print("4.3 : weight: weight which is being used to achieve the best value. ")
    

guide()
#test()
#test2()
