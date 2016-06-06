##########################################################
# Recursion wk9
# MHG 6/2016
# 
##########################################################

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """

    # If you've got i is less than or equal to length of list STOP!
    if i >= len(my_list): 
        return

    print my_list[i]

    #Otherwise play it again and add 1
    print_item(my_list, i+1)



# 2. Write a function that uses recursion to print each node in a tree.
def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """

    """Print items in tree from this node."""

    print tree.data
    
    for child in tree.children:
        # This should be printing the child but it's just looping like crazy
        print_all_tree_data(child)
    
    


# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """
    #When you've got nothing left return
    if not my_list:
        return 0  

    
    return (1 + list_length(my_list[1:]) )



# 4. Write a function that uses recursion to count how many nodes are in a tree.
# Seriously trying to put a hole in so the rest of my brains can fall out and I can finish
def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
    """


    sum = 1
    
    for child in tree.children:
        
        sum = sum + num_nodes(child)
    
    return sum


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
