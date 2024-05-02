"""Confirm the correctness of functions in question_six."""

import pytest

# ruff: noqa: PLR2004
from questions.question_six import (
    Gene,
    sort_data_int,
    sort_data_str,
    sort_genes,
)


def assert_and_print(expected, actual, message):
    """Print a diagnostic message and assert that the expected and actual values are equal."""
    print(f"{message}: Expected {expected}, got {actual}")
    assert expected == actual


def demarcate():
    """Demarcate test output."""
    print("test_question_six.py")


@pytest.mark.question_six_part_a
def test_sorting_int():
    """Confirm correctness of question part."""
    demarcate()
    # check 1: small list
    data = [9, 1, 2, 8, 3, 7, 4, 6, 5, 1]
    sorted_data = sort_data_int(data)
    expected = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert_and_print(expected, sorted_data, "Small list sorting")
    # check 2: larger list
    data = [100, 10, 20, 90, 30, 80, 40, 70, 50, 60, 10]
    sorted_data = sort_data_int(data)
    expected = [10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    assert_and_print(expected, sorted_data, "Large list sorting")
    # check 3: list without duplicates
    data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sorted_data = sort_data_int(data)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert_and_print(expected, sorted_data, "Non-duplicate list sorting")
    # check 4: empty list
    data = []
    sorted_data = sort_data_int(data)
    expected = []
    assert_and_print(expected, sorted_data, "Empty list sorting")


@pytest.mark.question_six_part_b
def test_sort_data_str():
    """Confirm correctness of sort_data_str function."""
    # check 1: small list
    data = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_data = sort_data_str(data)
    expected = ["elderberry", "date", "cherry", "banana", "apple"]
    assert_and_print(expected, sorted_data, "Small list sorting")
    # check 2: larger list
    data = [
        "banana",
        "apple",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew",
        "ice cream",
        "jackfruit",
    ]
    sorted_data = sort_data_str(data)
    expected = [
        "jackfruit",
        "ice cream",
        "honeydew",
        "grape",
        "fig",
        "elderberry",
        "date",
        "cherry",
        "banana",
        "apple",
    ]
    assert_and_print(expected, sorted_data, "Larger list sorting")
    # check 3: list without duplicates
    data = ["apple", "banana", "cherry", "date", "elderberry"]
    sorted_data = sort_data_str(data)
    expected = ["elderberry", "date", "cherry", "banana", "apple"]
    assert_and_print(expected, sorted_data, "List without duplicates sorting")
    # check 4: empty list
    data = []
    sorted_data = sort_data_str(data)
    expected = []
    assert_and_print(expected, sorted_data, "Empty list sorting")


@pytest.mark.question_six_part_c
def test_sort_genes():
    """Confirm correctness of sort_genes function."""
    # check 1: small list
    data = [
        Gene("AADACL4", 5, "Arylacetamide deacetylase-like 4"),
        Gene("AADACL3", 5, "Arylacetamide deacetylase-like 3"),
    ]
    sorted_genes = sort_genes(data)
    expected = [
        Gene("AADACL3", 5, "Arylacetamide deacetylase-like 3"),
        Gene("AADACL4", 5, "Arylacetamide deacetylase-like 4"),
    ]
    # check 2: singleton list
    data = [
        Gene("AADACL4", 5, "Arylacetamide deacetylase-like 4"),
    ]
    sorted_genes = sort_genes(data)
    expected = [
        Gene("AADACL4", 5, "Arylacetamide deacetylase-like 4"),
    ]
    assert_and_print(expected, sorted_genes, "Small list sorting")
    # check 2: empty list
    data = []
    sorted_genes = sort_genes(data)
    expected = []
    assert_and_print(expected, sorted_genes, "Empty list sorting")
