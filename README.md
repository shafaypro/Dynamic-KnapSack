# Dynamic-KnapSack
A knapSack OOP followed approach which is used to solve in the Problems  in the Data set to get the optimized value from a specified weight cost  !

# Requirements: 
  All modules are builtin in both Python3 and python2 packages.

# Creating Object:
   ## KS =  KnapSack()


# Guide:
  1 - Create KnapSack Instance : 
      # KS = KnapSack() 
  2 - If your data is not in form of tuple of tuple instead its seperate lists then :  ")
  3 - Apply lists zipping by passing in all three lists as : 
    # master_tuple = tuple(KS.create_knap_tuple(list1,list2,list3))
  4 - Apply knap stack on the dataset to get three parameters in reuturn : 
    # items_on, value, weight =    KS.apply_knap_sack(max_weight=400,master_list=master_tuple)
  ## Return values
    4.1 : items_on :  names or numbers of the items which were considered in getting the optimized best result
    4.2 : value : value achieved best in case of specific weigh
    4.3 : weight: weight which is being used to achieve the best value.
