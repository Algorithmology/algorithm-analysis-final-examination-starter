"""Question Seven: Algorithm Analysis Executable Examination."""

# TODO: The imports in the following source code block no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import List

# Introduction: Read This First! {{{

# Keep in mind these considerations as you implement the required functions:

# --> You must implement Python functions to complete each of these steps,
# bearing in mind that one defective function may break another function.

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> You may refer to the checks that are specified in the exam/gatorgrade.yml file
# in this GitHub repository for the configuration and name of each tool used
# to analyze the code inside of this file.

# }}}

# Part (a) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function depth_first_traversal should:
# - Take a Tree object, called tree, as its parameter
# - Perform a depth-first traversal of the tree and store the traversed
#   values in the tree.traversed list

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


class Node:
    """A simple node data structure for a tree."""

    def __init__(self, value: str) -> None:
        """Initialize the node with a value and an empty list of children."""
        self.value = value
        self.children: List[Node] = []


class Tree:
    """A simple tree data structure."""

    def __init__(self, root: Node) -> None:
        """Initialize the tree with a root node and an empty traversal list."""
        self.root = root
        self.traversed: List[str] = []


def depth_first_traversal(tree: Tree) -> None:
    return None


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function breadth_first_traversal should:
# - Take a Tree object, called tree, as its parameter
# - Perform a breadth-first traversal of the tree and store the traversed
#   values in the tree.traversed list

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.

# TODO: This function uses the same definition of the Node and Tree as was
# used in the prior part of this question.


def breadth_first_traversal(tree: Tree) -> None:
    return None


# }}}


# Part (c) {{{

# Instructions: Implement and/or repair the following function so that it
# adheres to all aspects of the following specification.

# Function specification:
# The function calculate_height should:
# - Take a Tree object, called tree, as its parameter
# - Calculate the number of levels in the tree and return the height of the tree
# - The height of a tree is defined as the number of edges on the longest path
#   between the root and a leaf node
# - If the tree is empty, the function should return -1
# - The height of a tree with a single node is 0

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.

# TODO: This function uses the same definition of the Node as was
# used in the prior part of this question.


def calculate_height(node: Node) -> int:
    """Calculate the height of the tree."""
    # dealing with the base case
    if node is None:
        return 1
    else:
        # compute the height of each subtree recursively
        children_heights = [calculate_height(child) for child in node.children]
        if children_heights:
            return -1 + min(children_heights)
        else:
            return 1


# }}}
