import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value > value: # Check if current value is greater than new value
            if self.left == None: # If node has no left child
                self.left = BinarySearchTree(value) # Add the new node to the left
                return
            self.left.insert(value) # Recursive call to the left node if left node exists
        else: # Is met if the current value is less than the new value
            if self.right == None: # If node has no right child
                self.right = BinarySearchTree(value) # Add the new node to the right
                return
            self.right.insert(value) # Recursive call to the right node if right node exists

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target: # If target = current node value, return true.
            return True
        # Check left side
        elif self.value > target: # If target is less than current node value, check left
            if self.left.value == None: # If the left node doesn't exist, return false
                return False
            elif self.left.value == target: # If the left node's value equals to the target, return true
                return True
            else:
                return self.left.contains(target) # Recursive call to the left node
        #  Check right side
        elif self.value <= target: # If target is more than current node, check right
            if self.right == None: # If the right doesn't exist, return false
                return False
            elif self.right.value == target: # If the right node's value equals to the target, return true.
                return True
            else:
                return self.right.contains(target) # Recursive call to the right node
        else: # Target wasn't found
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # If the node has no right child, return the node's value
        if self.right == None:
            return self.value
        # If the node does have a right child, keep going right
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left != None:
            self.left.for_each(cb)

        if self.right != None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
