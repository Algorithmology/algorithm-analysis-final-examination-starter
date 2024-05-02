"""Question Four: Algorithm Analysis Executable Examination."""

# TODO: The imports in the following source code block no longer
# adhere to the industry best practices for Python source code.
# You must reorganize and/or add/delete the imports so that they
# adhere to the industry best practices for Python source code.

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
# The function detect_duplicates_int should:
# - Take a list of integers, called data, as its parameter
# - Return a boolean value that indicates whether or not there are duplicate
#   values in the list
# - If the list is empty, the function should return False to indicate that there
#   are no duplicate values
# - The implementation must use the set data structure to support the
#   detection of the duplicate values

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def detect_duplicates_int(data) -> bool:
    return False


# }}}

# Part (b) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function detect_duplicates_str should:
# - Take a list of strings, called data, as its parameter
# - Return a boolean value that indicates whether or not there are duplicate
#   values in the list
# - If the list is empty, the function should return False to indicate that
#   there are no duplicate values
# - The implementation must use the set data structure to support the
#   detection of the duplicate values

# TODO: This function may not not have all of the correct type annotations for
# certain variables. You must add all of any needed type annotations
# so that the function and any code that uses it passes the type checker.

# TODO: This function may not have a docstring and thus it may not adhere
# to industry best practices for Python source code. You may need to add a docstring
# so that this function is correctly documented by an algorithm engineer using it.


def detect_duplicates_str(data) -> bool:
    return True


# }}}

# Part (c) {{{

# Instructions: Implement the following function so that it adheres to all
# aspects of the following specification.

# Function specification:
# The function detect_duplicates_gene should:
# - Take a list of Gene values, called data, as its parameter
# - Return a boolean value that indicates whether or not there are duplicate
#   values in the list
# - If the list is empty, the function should return False to indicate that there
#   are no duplicate values
# - The function should compare the prefix of the gene name with the prefix of
#   another gene name
# - The prefix of the gene name is defined as the first n characters of the gene name,
#   where n is the gene_prefix field
# - If the prefix of the gene name is equal to the prefix of another gene name,
#   then the two gene names are considered to be duplicates. Otherwise, they are
#   not considered to be duplicates. Note that, in particular, the comparison
#   between the two genes should not consider the gene_description field.
# - The function should use iteration constructs like a for loop.

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


def compare_gene_prefix(gene: Gene, other_gene: Gene) -> bool:
    """Compare the prefix of the gene name with the prefix of another gene name."""
    # extract the prefix from the gene name
    gene_prefix = gene.gene_name[: gene.gene_name_prefix]
    # compare the prefix to the prefix of the other gene name
    gene_other_prefix = other_gene.gene_name[: other_gene.gene_name_prefix]
    return gene_prefix == gene_other_prefix


def detect_duplicates_gene(data):
    return True


# }}}
