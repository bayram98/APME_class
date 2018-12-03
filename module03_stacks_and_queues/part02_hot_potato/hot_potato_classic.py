"""
THE HOT POTATO GAME:
In this game children line up in a circle and pass an item from neighbor to neighbor as fast as they can.
At a certain point in the game, the action is stopped and the child who has the item (the potato)
is removed from the circle. Play continues until only one child (i.e., the winner) is left.

We will implement a general simulation of the Hot Potato game:
Our program will input a list of names and a constant, call it “num,” to be used for counting.
It will return the name of the last person remaining after repetitive counting by num.
What happens at that point is up to you :)

To simulate the circle, we will use a queue.
Assume that the child holding the potato will be at the front of the queue.
Upon passing the potato, the simulation will simply dequeue and then immediately enqueue that child,
putting her at the end of the line. She will then wait until all the others have been at the front before it will
be her turn again. After num dequeue/enqueue operations, the child at the front will be removed permanently
(i.e., eliminated from the game) and
another cycle will begin. This process will continue until only one name remains (i.e., the size of the queue is 1).

Good luck!
"""
from module03_stacks_and_queues.part00_preclass.stack import ArrayStack
from module03_stacks_and_queues.part00_preclass.queue import ArrayQueue

def hot_potato(name_list, num):
    """
    Hot potato simulator. While simulating, the name of the players eliminated should also be printed
    (Note: you can print more information to see the game unfolding, for instance the list of
    players to whom the hot potato is passed at each step...)

    :param name_list: a list containing the name of the players, e.g. ["John", "James", "Alice"]
    :param num: the counting constant (i.e., the length of each round of the game)
    :return: the winner (that is, the last player standing after everybody else is eliminated)
    """
    queue = ArrayQueue()
    for i in name_list:
        queue.enqueue(i)

    stop = False
    while not stop:
        for i in range(1,num):
            s = queue.dequeue()
            queue.enqueue(s)
            print(s)
        print()
        print(" Drop it {0}".format(queue.dequeue()))
        if queue.__len__() == 1:
            return queue.dequeue()




if __name__ == '__main__':
    name_list = ("Marco", "John", "Hoang", "Minji", "Hyunsuk", "Jiwoo")
    winner = hot_potato(name_list, 5)
    print("...and the winner is: {0}".format(winner))
