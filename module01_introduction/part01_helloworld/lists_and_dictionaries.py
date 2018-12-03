#some examples about sequences

def examples_with_lists():
    # To know more: http://www.tutorialspoint.com/python/python_lists.htm
    # Each element of a list is assigned a number, i.e., its "index"
    # Indexes start from 0 and are used to access the content of a list
    # List can contain anything, check the following examples:
    l1 = ["a", "b", "c", "d"]                           # a list of characters
    l2 = [100, 125, 4, 56]                              # a list of integers
    l3 = ["Marco", "John", 29, 786]                     # a list with mixed content
    l4 = [["Marco", 3], ["John", 2], ["James", 5]]      # a list of lists
    l5 = [[3, 6, 8], [7, 9, 3], [8, 1, 0]]              # a list of lists (a 3 x 3 "matrix")
    print(l1[0])                                        # outputs "a"
    print(l1[2])                                        # outputs "c"
    print(l2[len(l2)-1])                                # outputs 56 (note len(list) returns the number of elements of a list)
    print(l4[2])                                        # output ['James', 5]
    l4.append(["Tom", 67])                              # add an element at the end of a list
    print(l4)                                           # print the entire list
    print(l2[-1])                                       # negative indexes start from the end of the list
    # lists can be "sliced" with :
    print(l1[1:])                                       # print elements from index 1 to the end
    print(l3[:3])                                       # print element from index 0 (start) to 2 (=3-1)
    print(l5[1][0])                                     # outputs 7 (note double indexing for list of lists



def examples_with_dict():
    # Dictionaries in Python are "Hash maps", that is, sequences using generic keys (not only numbers)
    # In other words, indexes in dictionaries are called "keys" and can be anything
    # for more information: http://www.tutorialspoint.com/python/python_dictionary.htm
    # check the syntax:
    d1 = {"Marco" : "010-1234-5678", "Tom" : "010-4456-9876", "Jin" : "010-2312-7654"}      # a telephone directory
    print(d1["Marco"])                                                                      # outputs "010-1234-5678"
    d2 = {"A" : [0, 1, 2], "B" : [3, 4, 5], "C" : [4, 3, 1]}
    print(d2["B"])                                                                          # outputs [3, 4, 5]
    d2["D"] = [2, 4, 8]# add new entry

    print(d2)                                                                               # print all content

if __name__ == '__main__':
    # There are two types of sequences in Python:
    # lists (not to be confounded with "linked lists" of week 05) and dictionaries
    examples_with_lists()
    examples_with_dict()
