"""
to practice recursion, your task is to implement a recursive version of the "binary_search" algorithm
to search an element in an array (ie., a Python list, such as [89, 78, 67, 90]).
The binary search works only on SORTED arrays (in ascending or descending order), so you should also implement
 a function to check whether an array is sorted.

To understand how a binary search works, check p.155 of the book GTG
On p.156 there is a possible solution in Python, but, since it uses advanced Python constructs,
I strongly advise you NOT to look at it. Try instead to implement your own version!!!
"""
from time import sleep

def is_sorted(array):
    """
    Check if an array is sorted in ascending order (assumes an array of numbers, such as integers or float)
    :param array: the array to be checked
    :return: a message ("Array is sorted" or "Array is not sorted")
    """
    for i in range(1,len(array)):
        if array[i-1] > array[i]:
            print("Array is not sorted")
            return False
    print("Array is sorted")
    return True

def binary_search(array, elem, first, last):
    """
    Search for an element in an array using binary search
    :param array: array to look for element
    :param elem: the lement to look for
    :param first: the index of the first position in the array
    :param last: the index of the last position in the array
    :return: a message showing the element (if found) or "Element not found" (if not found)
    """
    #print( " {0} {1} {2} ".format(elem,first,last))

    if is_sorted(array):
        if first == last:
            if array[first] == elem :
                print(" {0} is found in Array in {1} ".format(elem,first))
                return first
            else:
                print(" {0} is not found in Array".format(elem))
                return -1
        else:
            mid = (first + last) // 2
            #print( "{0} {1} {2} {3} {4}".format(mid , array[mid] , first, last, elem ))
            if array[mid] >= elem:
                return binary_search(array, elem, first, mid )
            return binary_search(array, elem, mid+1 , last )
    else:
        print("Give me a sorted array please!")


""" main() to test the implementation"""
if __name__ == '__main__':
    # A is sorted
    A = (1,5,6,7,9,13,16,17)
    # B is not sorted
    B = (1,6,7,8,2)


   # print(is_sorted(A))
   # print(is_sorted(B))

    sleep(2)
    # Search for element 16 in A
    print(binary_search(A, 16, 0, len(A) - 1))
    #Serach for element 56 in A
    sleep(2)
    print(binary_search(A, 56, 0, len(A) - 1))

'''
    if is_sorted(A):
        binary
'''





