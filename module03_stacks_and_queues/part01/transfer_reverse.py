"""
Your task is to implement the two functions below.

Note below the import statement to reuse the code that you have already seen in this week's "preclass"
"""
from module03_stacks_and_queues.part00_preclass.stack import ArrayStack


def transfer(S,T):
    """
    this function tranfers all the elements from stack S to stack T such that the elements at the top of S is the first
    to be inserted onto T, and the element at the bottom of S ends up at the top of T
    (that is, T will look like S with elements in reverse order)
    Note: you can assume that T is always EMPTY
    :param S: the stack to transfer
    :param T: the empty stack where to transfer the element of S
    """
    while not S.is_empty():
        T.push(S.pop())

def print_reverse_order():
    """
    This function reads a sequence of words provided through command line terminated by the "stop" word
    and prints them in reverse order.
    Each word is separated by the "enter", see the main() below for how to read user input from command line
    Note: this solution can be improved by (i) making sure that only 1 single words can be entered each time
    (this implementation accpets any string, including spaces) and (ii) ensuring that the last word "stop"
    is not printed....can you do it?
    """
    print("\n\n +++ WELCOME TO THE REVERSE PRINTER! +++")
    string_storage = ArrayStack()
    stop = False
    while not stop:
        new_word = input("Please provide a new word ('stop' to terminate): ")
        if new_word == 'stop':
            stop = True
        string_storage.push(new_word)
    print("\n#### Printing reverse.....")
    while(not string_storage.is_empty()):
        print(string_storage.pop())
    print("#### END printing reverse ###")


if __name__ == '__main__':
    stack = ArrayStack()
    """
    Run this to understand how to read user input from command line
    """
    print_reverse_order()
    """ Test of transfer()"""
    S = ArrayStack()
    T = ArrayStack()
    # Let's push some elements in S....
    S.push(23)
    S.push(15)
    S.push(76)
    S.push(765)
    S.print_contents()  # contents [23, 15, 76, 765]
    T.print_contents()
    # Now let's call transfer()
    transfer(S, T)
    T.print_contents()  # contents [765, 76, 15, 23]




