"""Confirm the correctness of functions in question_eight."""

import pytest

# ruff: noqa: PLR2004
from questions.question_eight import (
    iterative_binary_search,
    recursive_binary_search_efficient,
    recursive_binary_search_inefficient,
)


def assert_and_print(expected, actual, message):
    """Print a diagnostic message and assert that the expected and actual values are equal."""
    print(f"{message}: Expected {expected}, got {actual}")
    assert expected == actual


def demarcate():
    """Demarcate test output."""
    print("test_question_eight.py")


@pytest.mark.question_eight_part_a
def test_recursive_binary_search_inefficient():
    """Test a function."""
    # check 1: item in list
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item = 5
    assert_and_print(
        True, recursive_binary_search_inefficient(data, item), "Item in list"
    )
    # check 2: item not in list
    item = 11
    assert_and_print(
        False, recursive_binary_search_inefficient(data, item), "Item not in list"
    )
    # check 3: empty list
    data = []
    item = 1
    assert_and_print(
        False, recursive_binary_search_inefficient(data, item), "Empty list"
    )
    # check 4: list with one element, item in list
    data = [1]
    item = 1
    assert_and_print(
        True,
        recursive_binary_search_inefficient(data, item),
        "List with one element, item in list",
    )
    # check 5: list with one element, item not in list
    item = 2
    assert_and_print(
        False,
        recursive_binary_search_inefficient(data, item),
        "List with one element, item not in list",
    )


@pytest.mark.question_eight_part_b
def test_recursive_binary_search_efficient():
    """Test a function."""
    # check 1: item in list
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item = 5
    assert_and_print(
        True, recursive_binary_search_efficient(data, item), "Item in list"
    )
    # check 2: item not in list
    item = 11
    assert_and_print(
        False, recursive_binary_search_efficient(data, item), "Item not in list"
    )
    # check 3: empty list
    data = []
    item = 1
    assert_and_print(False, recursive_binary_search_efficient(data, item), "Empty list")
    # check 4: list with one element, item in list
    data = [1]
    item = 1
    assert_and_print(
        True,
        recursive_binary_search_efficient(data, item),
        "List with one element, item in list",
    )
    # check 5: list with one element, item not in list
    item = 2
    assert_and_print(
        False,
        recursive_binary_search_efficient(data, item),
        "List with one element, item not in list",
    )


@pytest.mark.question_eight_part_c
def test_iterative_binary_search():
    """Test a function."""
    # check 1: item in list
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item = 5
    assert_and_print(True, iterative_binary_search(data, item), "Item in list")
    # check 2: item not in list
    item = 11
    assert_and_print(False, iterative_binary_search(data, item), "Item not in list")
    # check 3: empty list
    data = []
    item = 1
    assert_and_print(False, iterative_binary_search(data, item), "Empty list")
    # check 4: list with one element, item in list
    data = [1]
    item = 1
    assert_and_print(
        True,
        iterative_binary_search(data, item),
        "List with one element, item in list",
    )
    # check 5: list with one element, item not in list
    item = 2
    assert_and_print(
        False,
        iterative_binary_search(data, item),
        "List with one element, item not in list",
    )
