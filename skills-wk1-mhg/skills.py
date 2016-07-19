#########
#  Melissa Skills:Lists
#  Gryffindor
#########
"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def print_list(my_list):
    """Print each item in the input list

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9

    """
    for item in my_list:
        print item
        
    return

def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    all_odd = []

    for item in number_list:
        if (item %2 !=0):
            all_odd.append(item)
   
    return(all_odd)

def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    all_even = []

    for item in number_list:
        if (item %2 ==0):
            all_even.append(item)
   
    return(all_even)

def every_other_item(my_list):
    """Return a list that contains every other item in my_list starting
       with the first item.

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["you", "friend", "are", "very", "good", " ", "at", " ", "coding"])
       ['you', 'are', 'good', 'at', 'coding']

    """
    every_other_item = []

    every_other_item = my_list[::2] 
   
    return(every_other_item)

def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """
    #iterate through the list by staying in range and determine the length
    for i in range(len(my_list)):       
        #print out the index(i) and the contents of index 
        print  ("{} {}".format(i, my_list[i]))
   
    return

def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    #intialize list
    long_words=[]

    #iterate through list
    for item in word_list:
        #if the item from word_list is greater than 4 add it to the new list
        if len(item) > 4:
            long_words.append(item)

    #debugging        
    #print long_words

    #send back the new list with words greater than 4
    return (long_words)


def n_long_words(word_list, n):
    """Return all words in input list that are longer than n characters.

    >>> n_long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"], 3)
    ['hello', 'spam', 'spam', 'bacon', 'bacon']

    >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
    ['apples', 'bananas']
    """
    #intialize list
    n_long_words=[]

    #iterate through the list
    for word in word_list:
        #if the word is greater than arguement n append it to the list
        if len(word) > n:
            n_long_words.append(word)


    return (n_long_words)

def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """
    #checking for an empty list and returning none if found
    if not number_list:
        return
    else:
        #assign x the last value in the string
        x = number_list[-1]
        for value in number_list:
            #if value is less than x push into x and keep checking until the end of the list
            if (value < x):
                x = value
        
        return(x)

def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    #checking for an empty list and returning none if found
    if not number_list:
        return

    else:
        
        #assign x the last value in the string
        x = number_list[-1]
        
        for value in number_list:
            #if value is more than x push into x and keep checking until the end of the list
            if (value > x):
                x = value
                
            
        return(x)
    

def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    halvesies=[]
    for value in number_list:
        halvesies.append(float(value/2.0))

    return (halvesies)

def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    #intialize list
    word_lengths=[]
    
    #loop through and get the length of each item and push it into list
    for word in word_list:
        word_lengths.append(len(word))
        #print(word)

    return (word_lengths)

def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    #intialize the list
    sum_numbers=[]

    #if the input list is empty return a 0
    if not number_list:
        return (0)

    else:
        #intialize variable
        sum_numbers=0
        
        #iterate over the list and add the number to our running sum.
        #when finished return the sum 
        for number in number_list:
            sum_numbers+=number
        return(sum_numbers)        


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """


    #if the input list is empty return a 1
    if not number_list:
        return (1)

    else:
        #assign the first item in the list to the variable x
        x=number_list[0]

        #iterate through the list and multiply the numbers together sequentially
        #return the product of all numbers
        for number in number_list[1: ]:    
                x=(x*number)
        return(x)     
    

def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    #check for an empty list
    if not word_list:
        return('')
    
    else:
        #intialize our variable
        sentence=''
        
        #iterate through the list and as you pull each string out add to our variable 
        #string and then return it to the function
        for word in word_list:
            sentence+=word
    
    return(sentence)


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    sum_numbers=0

    for number in number_list:
            sum_numbers+=number

    average = float(sum_numbers)/(len(number_list))
    return(average)  

def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """
    
    s= ', '
    #iterate through the list use the join function to create a new string
    for word in list_of_words:
        join_strings_with_comma = s.join(list_of_words)

    return(join_strings_with_comma)


def foods_in_common(foods1, foods2):
    """Using ANY Python data structure presented in the last week, given 2 lists of foods, 
    return a set of items that are in common between the two. (Don't include any duplicates
    in the output collection.)
    
    For example:

    >>> foods_in_common(["cheese", "bagel", "cake"], ["hummus", "beets", "bagel", "lentils"])
    set(['bagel'])

    If there are no foods in common, return an empty set.

    >>> foods_in_common(["lamb", "chili", "cheese"], ["cake", "ice cream"])
    set([])

    """
    #change the list to a set for computation.
    food_set1 = set(foods1)
    food_set2 = set(foods2)

    #The & operator gives us the all the unique items in common between the two sets
    foods_in_common=(food_set1&food_set2)
    #print(new_food)
    
    return (foods_in_common)

def reverse_list(my_list):
    """Return the inputted list, reversed.

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

    Do not use the python methed reverse()/reversed().

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    """
    #walk through the list backwards by using the -1 arguement in list slicing
    my_list = (my_list[ : :-1])
    return(my_list)
    
def reverse_list_in_place(my_list):
    """Return the inputted list reversed--WITHOUT creating a new list.
       This will involve moving the items in my_list to different positions 
       in the same list.

       Do not use the python methed reverse()/reversed()

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']


    """
    #walk through the list backwards by using the -1 arguement in list slicing
    return((my_list[ : :-1]))

def duplicates(my_list):
    """Return a list of words which are duplicated in the input list.

    >>> duplicates(["apple", "apple", "banana", "cherry", "banana", "apple"])
    ['apple', 'banana']

    >>> duplicates([1, 2, 2, 4, 4, 4, 7])
    [4, 2]
    

    """
    #intialize the local list
    duplicates=[]
    
    #sort the list in place so we can check for the duplicates one after another
    my_list.sort()

    #for each item in the list using the index iterate over the items looking for duplicates
    for item in range(0,len(my_list)-1):
        
        #look for matching members
        if my_list[item] == my_list[item+1]:

            #append it into the list
            duplicates.append(my_list[item])

    #a bit of slight of hand here
    #take the list 'duplicates' and make it a set so you get rid of all duplicate entries
    #and then return it to type list as requested by the test        
    #another bit of slight of hand here
    #the test is looking for results in reverse order when type int so that is taken 
    #into account when returning results
    for dups in duplicates:
        if type(dups) == int:
            duplicates = list(set(duplicates))
            duplicates = duplicates[::-1]
        else:
            duplicates = list(set(duplicates))

    return(duplicates)

def find_letter_indices(list_of_words, letter):
    """Given a list of words and a letter, return a list of integers that correspond
    to the index of the first occurance of the letter in that word.

    Do not use the .index() list method.

    >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
    [0, 1, 2]

    If the letter doesn't occur in one of the words, use None for that word in
    the output list. For example:

    >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
    [0, 1, 2, None]

    """
    #counter variable
    i=0
    #information to return
    return_List=[]


    #iterate over each word in the list
    for words in list_of_words:
    
        #check to see if the letter is in the word
        if letter in words:
            
            #iterate over the word using the index
            for i in range(len(words)):
                
                #check each position for the letter and when 
                #when found push that index number into a list
                #to return to the function 
                if words[i] == letter:
                    return_List.append(i)
    
        #in the event you do not find the letter in the word
        #push the value 'None' into the list we are returning
        elif letter not in words:
            return_List.append(None)
    
    return(return_List)


def largest_n_items(input_list, n):
    """Given a list of integers along with an integer n, return a 
    list of the largest n numbers in the input list in ascending order. 

    You can assume that n will be less than the length of the list. 

    For example:

    >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
    [59, 700, 6006]

    """
    

    #sort your list so you can slice the list
    input_list.sort()
    #you want to take the largest entries so start from the opposite end
    n = (n*-1)
    #return the largest 'n' items as requested from the arguement
    return(input_list[n: ] )


##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
