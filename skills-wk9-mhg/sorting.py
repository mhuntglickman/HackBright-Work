####################################################
# MHG 6/2016
#Sorting  wk9
####################################################

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """


    # Running this as for with nested for and if loop.  Run Time of a large data set would 
    # be terrible. And took me a bit using the visual python editor
    
    for x in range(len(lst)-1, 0, -1):
        # print x
        
        for i in range(x):
        # print i  
            # compare two elements
            if lst[i] > lst[i+1]:
                # print lst[i], lst[i+1]
                
                temp = lst[i]
                # print temp

                # Moving on
                lst[i] = lst[i+1]
                # print lst[i]
                # 
                lst[i+1] = temp
                # print lst[i+1]
    return lst

def merge_lists(list1, list2):
    """Given two sorted lists of integers, return a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """
    #Intialize the empty list for holding results
    list_Results = []

    # While the lists still have items in them
    while len(list1) > 0 or len(list2) > 0:
        
        #  if list 1 is empty take element 0 from list 2 and pop it into the result list
        if list1 == []:

            list_Results.append(list2.pop(0))
        
        #  if list 2 is empty take element 0 from list 1 and pop it into the result list
        elif list2 == []:

            list_Results.append(list1.pop(0))

        #  compare list 1 to list 2 and pop list 1 if it is smaller
        elif list1[0] < list2[0]:

            
            list_Results.append(list1.pop(0))

        #  compare list 2 to list 1 and pop list 2 if it is smaller    
        else:

            list_Results.append(list2.pop(0))

    
    return list_Results
 


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, return a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    
    """
    list_results = []

    # if length of lst is 1 return the list and pop out of funciton
    if len(lst) < 2:  
    
        return lst

    # cut the list in half 
    mid = int(len(lst) / 2)


    # slice the list using the midpoint
    lst1 = merge_sort(lst[:mid])  
    lst2 = merge_sort(lst[mid:])  

    # Compare 1st items from each list
    list_results = merge_lists(lst1, lst2)


    return list_results




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print