"""
Your task is to complete the implementation of the functions below, which do some kind of
manipulation of linked lists and Doubly Linked lists
(that is, you need to use the LinkedList class defined in the preclass session)
"""

from module05_linked_lists.part00_preclass.linked_list import LinkedList
from module03_stacks_and_queues.part00_preclass.stack import ArrayStack
from module05_linked_lists.part00_preclass.doubly_linked_list import DoublyLinkedList
from module05_linked_lists.part00_preclass.doubly_linked_list import Node


def find(L, e):
    """
    This function should look for an element in a linked list and prints on the console the result of the search
     e.g. "Element not found in the list", "Element X found in the list at position Y"
    :param L: the list
    :param e: the element to look for
    """
    cur = L.find(e)
    if cur == None:
        print("Element not found in the list")
    else:
        print("ELement {0} found in the list at position {1}".format(e, cur))


def cat(L1,L2):
    """
    This function should append the content of one list L2 at the end of the list L1. in other words, this
    function "concatenates" L1 and L2.
    (Therefore, L1 is modified as an effect of the execution of this function)
    Example: L1 = 10 -> 20 -> 5   ; L2 = 89 -> 56 -> 80
    After executiing the function, it will be: L1 = 10 -> 20 -> 5  -> 89 -> 56 -> 80 ; L2 = 89 -> 56 -> 80
    """
    temp = L2._head
    t = L2.__len__()
    print(t)
    while t > 0:
        L1.add_last(temp._data)
        temp = temp._next
        t -= 1

def copy(L):
    """
    This function returns a new list which is a copy of the list L.
    This function returns a "deep" copy of the list L, that is, a new list whose element are the same
    as L (and in the same order).
    Hint for the implementation: The LinkedList allows to add elements only at the "head" of a linked list...so...
    :param L: the list to copy
    :return: a "deep" copy of the list L
    """
    temp = L
    return temp



def copy_and_cat(L1,L2):
    """
    This function should return a new list that is the concatenation of two lists L1 and L2.
    That is, the lists L1 and L2 should NOT be modified by this function
    (Hint: make a "deep copy" of the two lists and build the returned lists using these copies...)
    :param L1:
    :param L2:
    :return: a list containing the concatenation of L1 and L2
    """
    temp = copy(L1)
    cat(temp, L2)
    return temp


def swap_first_with_last(DL):
    """
    This function should swap the content of the head of the doubly linked list with the content of its tail.
    E.g. swap_first_with_last() applied to 10 <-> 67 <-> 87 <-> 9 returns 9 <-> 67 <-> 87 <-> 10]
    :param DL: a doubly linked list
    """
    data = DL._head._data
    data1 = DL._tail._data

    DL.remove_first()
    DL.remove_last()
    DL.insert_front(data1)
    DL.insert_last(data)

    # DL.delet_node(DL._head)


def insert_at_position(DL, n, data):
    """
    This function should insert an element in a doubly linked list at a specific position.
    E.g. After executing insert_at_position(DL, 2, 88) with DL = 10 <-> 67 <-> 87 <-> 9
    It should be DL =  10 <-> 88 <-> 67 <-> 87 <-> 9
    Note 1: try to implement this function in the fastest way possible (...how?)
    Note 2: be careful at how you manage insertion at the head of the list (position 1) and at the tail (position DL.__len__())
    :param DL: a doubly linked list
    :param n: the position at which n should be inserted
    :param data: the element to insert
    """
    DL.insert(data, n - 1)




def special_copy(DL1,DL2):
    """
    This function should return a new doubly linked list which contains the same element of DL1 concatenated with
    the elements of DL2 in reverse order.
     Ex. DL1 = 4 <-> 5 <-> 6, DL2 = 9 <-> 4 <-> 6 >>> returns DL3 = 4 <-> 5 <-> 6 <-> 6 <-> 4 <-> 9]
    Note: this function does not modify L1 or L2
    Note2: the method "add" of the DoublyLinkedList class adds element *at the tail* of the list
    :param DL1: a doubly linked list
    :param DL2: a doubly linked list
    """
    # DL2.reverse()
    l = []
    # l.append(DL2._tail._data)
    current_node = DL2._head
    while current_node is not None:
        if current_node._next == None:
            l.append(current_node._data)
        else:
            l.append(current_node._data)
        current_node = current_node._next
    l.reverse()
    for x in l:
        DL1.add(x)
    return DL1

""" main() to do some testing"""
if __name__ == '__main__':



    L1 = LinkedList()
    L2 = LinkedList()
    L1.add_first("Jin")
    L1.add_first("Jun")
    L1.add_first("Jan")
    L1.print()
    L2.add_first(118)
    L2.add_first(115)
    L2.add_first(89)
    L2.add_first(87)
    L2.print()
    find(L1,"Jin")
    find(L1, 908)
    cat(L1,L2)
    L1.print()
    print("""Test deep copy and copy_cat""")
    L3 = copy(L1)
    L3.print()
    L3.add_first("new")
    L3.print()
    L1.print()
    L4 = copy_and_cat(L1,L3)
    L4.print()
    """ create two doubly linked lists and add some data"""
    DL1 = DoublyLinkedList()
    DL2 = DoublyLinkedList()
    DL1.add("A")
    DL1.add("B")
    DL1.add("Y")
    DL1.add("Z")
    DL1.print()
    DL2.add(67)
    DL2.add(69)
    DL2.add(25)
    DL2.add(29)
    DL2.add(76)
    DL2.print()

    """ test swap """
    print("========== Test swap() ===================================")
    swap_first_with_last(DL2)
    DL2.print()
    print(str(DL2.__len__()))
    swap_first_with_last(DL2)
    DL2.print()

    """ test insert at position"""
    print("========== Test insert_at_position() ===================================")
    insert_at_position(DL2, 2, "marco")  # insert walking from head
    DL2.print()
    insert_at_position(DL2, 6, "james")  # insert walking from tail
    print(str(DL2.__len__()))
    DL2.print()
    insert_at_position(DL2, 1, "2345")  # insert at head
    DL2.print()
    insert_at_position(DL2, DL2.__len__(), "Bob")  # insert at tail
    DL2.print()
    insert_at_position(DL2, 4, "4")
    insert_at_position(DL2, 7, "7777")
    DL2.print()

    """ test cat """
    print("========== Test special_copy() ===================================")
    DL1.print()
    DL2.print()
    DL3 = special_copy(DL1, DL2)
    DL3.print()

