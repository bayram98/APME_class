"""
Your task is to implement two functions using the LinkedBinaryTree class.
The first function (build_UNIST_tree) simply returns the organisational structure of schools and departments at UNIST.
The second function (LCA) finds the common ancestor in a tree of two positions.

- Implement the first function
- check the main to test your implementation
- Implement the second function
- Complete the main to test your implementation of the second function
"""

from module06_trees.part00_preclass.linked_binary_tree import LinkedBinaryTree


def build_UNIST_tree():
    """
    This function should return a binary tree that contains (a simplified and fictitious  version of) the organisational
    structure of schools and departments at UNIST. In particular, this function should return the following tree:

    UNIST
    --Engineering
    ----Management Engineering
    ------Big data
    ------Business process management
    ----Materials Engineering
    ------Wood
    ------Plastic
    --Business
    ----Business Administration

    :return: the UNIST tree
    """

    tree = LinkedBinaryTree()
    root = tree._add_root("UNIST")


    root_left = tree._add_left(root,"Engineering")
    root_right = tree._add_right(root, "Business")

    ME = tree._add_left(root_left,"Management Engineering")
    MaE = tree._add_right(root_left, "Management Engineering")

    tree._add_left(ME,"Big data" )
    tree._add_right(ME, "Business process management")

    tree._add_left(MaE, "Wood")
    tree._add_right(MaE, "Plastic")

    tree._add_left(root_right, "Business Administration")

    return tree


def LCA(T, n1, n2):
    """
    This function should return the lowest common ancestor of two positions in a tree n1 and n2.
    The LCA is the lowest position in T that has both n1 and n2 as descendants.
    :param T: the binary tree
    :param n1: position 1 in T
    :param n2: position 2 in tree
    :return: the LCA of n1 and n2
    """
    pass


def preorder_indent(T, p, d):
    """
    This function allows you to print in a "pretty" way the content of a tree.
    Elements of a tree are traversed in the "preorder" way and printed using indentation.
    It is given, you DO NOT have to complete it!

    To print the entire tree from the root use preorder_indent(tree,tree.root(),0)
    Note: you can use this function to print a sub-tree of T rooted an any position p

    Try to understand the code (in particular, note the recursive implementation!)
    """
    print(2 * d * '-' + str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d + 1)



if __name__ == '__main__':

    tree = build_UNIST_tree()

    # print the tree
    preorder_indent(tree,tree.root(),0)

    """ some code showing how to find positions in a binary tree, please check"""
    root = tree.root()                              # the root position of tree
    p_engineering = tree.left(root)                 # the left child position of the root position
    p_business = tree.right(root)                   # the right child position of the root position
    print(p_engineering.element())
    print(p_business.element())
    p_man_eng = tree.left(p_engineering)            # the left child position of the p_engineering position
    print(p_man_eng.element())

    """ implement here the code to test the LCA function that you implemented """
