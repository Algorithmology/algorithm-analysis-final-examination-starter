"""Question Six: Algorithm Analysis Executable Examination."""

# TODO: The imports in the following source code block no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add the imports so that they adhere
# to the industry best practices for Python source code.

from typing import Any, List

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
# The function sort_data_int should:
# - Take a list of ints, called data, as its parameter
# - Return a new list of integers that is sorted in ascending order
# - The original input list should not be modified

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def sort_data_int(data: List[int]) -> List[int]:
    """Sort the input list of integers without modifying the original list."""
    return []


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function sort_data_str should:
# - Take a list of strings, called data, as its parameter
# - Return a new list of integers that is sorted in descending order
# - The original input list should not be modified

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def sort_data_str(data: List[str]) -> List[str]:
    """Sort the input list of strings without modifying the original list."""
    return []


# }}}

# Part (c) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function sort_genes should:
# - Take a list of Gene values, called data, as its parameter
# - Perform a lexicographical sort on the list of Gene values
# - The sort should be done in ascending order according to the gene_name
#   and the gene_name_prefix
# - The original input list should not be modified

# Instructions: Implement one of the functions in the Gene class so
# that it adheres to all aspects of the following specification:

# Method specification:
# The __eq__ method should:
# - Take another Gene object, called other, as its parameter
# - Return a boolean value that indicates whether or not the two Gene objects
#   are equal
# - If the provided object is not a Gene, then the method should return False
# - If the provided object is a Gene, then the method should return True if
#   the gene_name, gene_name_prefix, and gene_description are equal

# TODO: This function will be tested with realistic gene data from this site:
# https://en.wikipedia.org/wiki/Chromosome_1

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.

# Define a class that represents a gene consisting of these fields:
# - a string field called gene_name
# - a string field called gene_name_prefix
# - a string called the gene_description


class Gene:
    """Represent a gene with a name, sequence, and description."""

    def __init__(self, gene_name: str, gene_prefix: int, gene_description: str) -> None:
        """Initialize a gene with an agreed-on name and a flexible description."""
        self.gene_name = gene_name
        self.gene_name_prefix = gene_prefix
        self.gene_description = gene_description

    def __eq__(self, other: Any) -> bool:
        return True

    def __str__(self) -> str:
        """Return a string representation of the gene."""
        return f"{self.gene_name} ({self.gene_name_prefix}): {self.gene_description}"

    def __repr__(self) -> str:
        """Return a string representation of the gene."""
        return f"{self.gene_name} ({self.gene_name_prefix}): {self.gene_description}"


def sort_genes(genes: List[Gene]) -> List[Gene]:
    return []


# }}}
