"""Confirm the correctness of functions in question_seven."""

import pytest

# ruff: noqa: PLR2004
from questions.question_seven import (
    Node,
    Tree,
    breadth_first_traversal,
    calculate_height,
    depth_first_traversal,
)


def assert_and_print(expected, actual, message):
    """Print a diagnostic message and assert that the expected and actual values are equal."""
    print(f"{message}: Expected {expected}, got {actual}")
    assert expected == actual


def demarcate():
    """Demarcate test output."""
    print("test_question_seven.py")


@pytest.mark.question_seven_part_a
def test_depth_first_traversal():
    """Test the depth_first_traversal function."""
    # create a tree
    root = Node("1")
    child1 = Node("2")
    child2 = Node("3")
    child1.children = [Node("4"), Node("5")]
    child2.children = [Node("6"), Node("7")]
    root.children = [child1, child2]
    tree = Tree(root)
    # call the function
    depth_first_traversal(tree)
    # check the output
    expected_output = ["1", "2", "4", "5", "3", "6", "7"]
    assert_and_print(expected_output, tree.traversed, "Depth-first traversal output")


@pytest.mark.question_seven_part_b
def test_breadth_first_traversal():
    """Test the breadth_first_traversal function."""
    # create a tree
    root = Node("1")
    child1 = Node("2")
    child2 = Node("3")
    child1.children = [Node("4"), Node("5")]
    child2.children = [Node("6"), Node("7")]
    root.children = [child1, child2]
    tree = Tree(root)
    # call the function
    breadth_first_traversal(tree)
    # check the output
    expected_output = ["1", "2", "3", "4", "5", "6", "7"]
    assert_and_print(expected_output, tree.traversed, "Depth-first traversal output")


@pytest.mark.question_seven_part_c
def test_calculate_height():
    """Test the height calculation function."""
    # create a tree
    root = Node("1")
    child1 = Node("2")
    child2 = Node("3")
    child1.children = [Node("4"), Node("5")]
    child2.children = [Node("6"), Node("7")]
    root.children = [child1, child2]
    tree = Tree(root)
    # call the function
    tree_height = calculate_height(tree.root)
    # check the output
    expected_output = 2
    assert_and_print(expected_output, tree_height, "Height calculation output")
