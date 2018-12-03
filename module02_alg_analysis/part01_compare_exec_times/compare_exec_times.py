# Note the import of the function time
# from ... import is the Python's construct to reuse "modules" (i.e., other programmes) in your own programme
# for more about it: https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/Importing_Modules
from time import time
from time import sleep

"""
In this week you will implement and test the functions example1 and example3 of p.143 in the GTG book
and test their execution time.
The functions are given, so you should only try to understand their code.
However, the main is not given, so you should implement your own main to test these functions.
Both function take as input a list S (not a dictionary!!!)

What is the Big-Oh complexity of example1 and example3?
"""



def example1(S):
    """
    EXAMPLE 1: Return the sum of the elements in S
    :param S: a sequence of numbers, e.g. [3, 9, 2]
    :return: the sum of elements in S
    """
    #time() captures the value of current system time
    start_time = time()
    n = len(S)
    total = 0
    for j in range(n):
        """sleep(0.15) delays the execution of each execution of the loop of 0.15 seconds
        This to add some constant delay, otherwise your computer will probably
        be too fast to see some meaningful time difference in executing such a simple algorithm!"""
        sleep(0.15)
        total += S[j]
    end_time = time()
    exec_time = end_time - start_time
    print("EXAMPLE 1 - Sum of elements in S is: {0}".format(total))
    print("EXAMPLE 1 - EXEC TIME: {0} seconds".format(exec_time))


def example3(S):
    """
    EXAMPLE 1: Return the sum of prefix sums in S
    :param S: a sequence of numbers, e.g. [3, 9, 2]
    :return: the sum of prefix sums in S
    """
    start_time = time()
    n = len(S)
    total = 0
    for j in range(n):
        #the sleep(0.15) delays the execution of 0.15 seconds (same reason as above)
        sleep(0.15)
        for k in range(j+1):
            #again, same reason as above
            sleep(0.15)
            total += S[k]
    end_time = time()
    exec_time = end_time - start_time
    print("EXAMPLE 2 - Sum of all prefix sums in S is: {0}".format(total))
    print("EXAMPLE 2 - EXEC TIME: {0} seconds".format(exec_time))

def intersection(A,B,C):
    """
    You have to provide the implementation of this function:
    This function tests whether the intersection of the lists A, B, and C is empty.
    It returns the boolean value True if the intersection is empty, and False otherwise.
    Assume that the 3 lists have at most 1 element in common, in case of not empty intersection the function also prints
    the value of the common element and the positions in the 3 lists at which the common element is found:
    Example:
    A = [4, 7, 8, 4], B=[89, 76], C=[6,9,67]
    intersection(A,B,C) returns True
    A = [4, 7, 8, 4], B=[9, 1, 7, 3, 4], C=[56, 33, 7]
    intersection(A,B,C) returns False and prints the message:
    “Common element found at A[1], B[2], C[2]; value: 7”

    BONUS 1: extend your implementation to print the amount of time it takes to your function to execute
    BONUS 2: What is the complexity of your algorithm in the worst case?
    """
    beginning_time = time()

    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(C)):
                if A[i] == B[j] and A[i] == C[k]:
                    end_time = time()
                    print("Common element found at A[{0}], B[{1}], C[{2}]; value: {3}".format(i,j,k,A[i]))
                    print("Execution time of intersection(A,B,C) is :{0}".format(end_time - beginning_time))
                    return False
    end_time = time()
    print("Execution time of intersection(A,B,C) is :{0}".format(end_time - beginning_time))
    return True


"""
main() function to test: this is the code that is executed when you "Run" this file
To "Run" this file, right click on the file in the left panel and click "Run compare_exec_times"
"""
if __name__ == '__main__':
    """ implement here your own code to test these two functions """
    A = [1, 2, 3, 4, 5]
    B = [2, 4, 6]
    C = [3, 5, 9, 2]

    f = intersection(A, B, C)
    print(f)


