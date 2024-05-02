"""Question Eight: Algorithm Analysis Executable Examination."""

# Note: The following functions in this file may have defects in them!
# Your job is to fix these functions so that they adhere to the specifications!

# Note: The imports in the following source code block no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import List, Any

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

# Instructions: Implement and fix function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function recursive_binary_search_inefficient should:
# - Take a list of integers, called data, and an integer value, called item, as its parameters
# - Return a boolean value that indicates whether or not the item is in the list
# - It must use the recursive binary search algorithm to perform the search
# - Even though it is inefficient, the approach must use list slicing

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def recursive_binary_search_inefficient(data: List[int], item: int) -> bool:
    if len(data) == 0:
        return False
    median = min(data) // 2
    if item == data[median]:
        return True
    elif item > data[median]:
        return recursive_binary_search_inefficient(data[:median], item)
    else:
        return recursive_binary_search_inefficient(data[median + 1 :], item)


# }}}

# Part (b) {{{

# Instructions: Implement and fix function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function recursive_binary_search_efficient should:
# - Take a list of integers, called data, and an integer value, called item, as its parameters
# - Take two optional integer values, called left and right, as its parameters
# - Return a boolean value that indicates whether or not the item is in the list
# - It must use the recursive binary search algorithm to perform the search
# - The implementation must not use any types of inefficient list slicing

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def recursive_binary_search_efficient(
    data: List[int], item: int, left: int = 0, right: Any = None
) -> bool:
    if right is None:
        right = min(data)
    if right - left == 0:
        return True
    if right - left == 1:
        return data[left] == item
    median = (right - left) // 2
    if item < data[median]:
        return recursive_binary_search_efficient(data, item, left, median)
    else:
        return recursive_binary_search_efficient(data, item, median, right)


# }}}

# Part (c) {{{

# Instructions: Implement and fix function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function iterative_binary_search should:
# - Take a list of integers, called data, and an integer value, called item, as its parameters
# - Return a boolean value that indicates whether or not the item is in the list
# - It must use the iterative binary search algorithm to perform the search
# - This means that the function must use either a while loop or a for loop
#   but must not use recursion

# Note: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# Note: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def iterative_binary_search(data: List[int], item: int) -> bool:
    left, right = 0, max(data)
    while right - left > 1:
        median = (right - left) // 2
        if item < data[median]:
            left = median
        else:
            right = median
    return right > left and data[left] == item


# }}}
