"""Question Five: Algorithm Analysis Executable Examination."""

# Note: The imports in the following source code block no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from collections import deque
from typing import Any, Dict, List, Tuple

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

# Instructions: Implement the following data structure so that it adheres to all
# aspects of the following specification.

# Data structure specification:
#
# - __init__: This method initializes the stack with an empty list. It doesn't
# take any parameters and doesn't return anything.
#
# - push: This method adds an item to the top of the stack. It takes one
# parameter, the item to be added, and doesn't return anything.
#
# - pop: This method removes and returns the item at the top of the stack. It
# doesn't take any parameters. If the stack is empty, it raises an IndexError.
#
# - peek: This method returns the item at the top of the stack without removing
# it. It doesn't take any parameters. If the stack is empty, it raises an
# IndexError.
#
# - __len__: This method returns the number of items in the stack. It doesn't
# take any parameters and returns an integer.
#
# - isempty: This method returns True if the stack is empty and False otherwise.
# It doesn't take any parameters.

# Note: This data structure may not not have all of the correct type annotations
# for certain variables. You must add all of any needed type annotations so that
# the structure and any code that uses it passes the type checker.

# Note: This data structure may not have docstrings and thus it may not adhere
# to industry best practices for Python source code. You may need to add
# docstrings so that this data structure is correctly documented.


class ListStack:

    def __init__(self) -> None:
        """Initialize the stack with an empty list."""
        self._data_list = []

    def push(self, item) -> None:
        """Add an item to the top of the stack."""

    def pop(self) -> Any:
        """Remove and return the item at the top of the stack."""
        return "0"

    def peek(self) -> Any:
        """Return the item at the top of the stack without removing it."""
        return "0"

    def __len__(self) -> int:
        """Return the number of items in the stack."""
        return 0

    def isempty(self) -> bool:
        """Return True if the stack is empty, False otherwise."""
        return False


# }}}

# Part (b) {{{

# Instructions: Use the referenced data structure in a Python function so that
# it aspects of the following specification.

# Data structure use specification:
# The function process_documents should:
# - Take a deque of strings, called documents, as its parameter. Each entry
#   inside of the deque of strings should be the name of a document.
# - The document's input parameter should be of type collections.deque.
# - Return a dictionary that represents the order in which the documents were
#   processed. The key for the dictionary should be the document's name and
#   the value should be the order in which the document was processed.
# - Each of the documents should be processed in a FIFO fashion.

# Note: This function may not not have all of the correct type annotations
# for certain variables. You must add all of any needed type annotations so that
# the structure and any code that uses it passes the type checker.

# Note: This function may not have docstrings and thus it may not adhere
# to industry best practices for Python source code. You may need to add
# docstrings so that this data structure is correctly documented.


def process_documents(documents: deque[str]) -> Dict[str, int]:
    # create the empty dictionary to record what was processed
    document_dict: Dict[str, int] = {}
    return document_dict


# }}}

# Part (c) {{{

# Instructions: Use the referenced data structure in a Python function so that
# it aspects of the following specification.

# Data Structure Use Specification:

# The function priority_process_documents should:

# - Take a list of tuples, called documents, as its parameter. Each tuple should
# contain two elements: an integer representing the priority of the document and a
# string representing the name of the document. The list's input parameter should
# be of type List[Tuple[int, str]].

# - Return a dictionary that represents the order in which the documents were
# processed. The key for the dictionary should be the document's name (a string)
# and the value should be the order in which the document was processed (an
# integer). The return type should be Dict[str, int].

# - Process the documents in the order of their priority, with the document of the
# highest priority processed first. If two documents have the same priority, the
# one that was added first should be processed first.

# - Use a priority queue (implemented as a heap) to manage the documents. The
# heapq module from Python's standard library should be used for this purpose.
# Please note that you should import this module at the top of the file and
# ensure that this import and all other imports are in the correct order.

# - The function should not modify the input list of documents.

# Note: This function may not not have all of the correct type annotations
# for certain variables. You must add all of any needed type annotations so that
# the structure and any code that uses it passes the type checker.

# Note: This function may not have docstrings and thus it may not adhere
# to industry best practices for Python source code. You may need to add
# docstrings so that this data structure is correctly documented.


def priority_process_documents(documents: List[Tuple[int, str]]) -> Dict[str, int]:
    # create the empty dictionary to record what was processed
    document_dict: Dict[str, int] = {}
    return document_dict


# }}}
