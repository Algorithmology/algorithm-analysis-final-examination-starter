"""Confirm the correctness of functions in question_five."""

# ruff: noqa: PLR2004

from collections import deque

import pytest
from questions.question_five import (
    ListStack,
    process_documents,
    priority_process_documents,
)


def assert_and_print(expected, actual, message):
    """Print a diagnostic message and assert that the expected and actual values are equal."""
    print(f"{message}: Expected {expected}, got {actual}")
    assert expected == actual


def demarcate():
    """Demarcate test output."""
    print("test_question_five.py")


@pytest.mark.question_five_part_a
def test_find_minimum_value():
    """Confirm correctness of question part."""
    demarcate()
    stack = ListStack()
    with pytest.raises(IndexError):
        stack.pop()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    popped_element = stack.pop()
    assert_and_print(popped_element, 3, "Popped element")
    assert_and_print(stack.peek(), 2, "Peeked element")
    assert_and_print(len(stack), 2, "Length of stack")
    assert_and_print(stack.isempty(), False, "Emptiness of stack")


@pytest.mark.question_five_part_b
def test_process_documents():
    """Confirm correctness of question part."""
    documents = deque(["doc1", "doc2", "doc3"])
    expected_output = {"doc1": 1, "doc2": 2, "doc3": 3}
    assert_and_print(
        expected_output, process_documents(documents), "Document processing some"
    )
    documents = deque([])
    expected_output = {}
    assert_and_print(
        expected_output, process_documents(documents), "Document processing none"
    )


@pytest.mark.question_five_part_c
def test_process_documents_with_priority():
    """Confirm correctness of question part."""
    documents = [(3, "doc1"), (2, "doc2"), (1, "doc3")]
    expected_output = {"doc1": 3, "doc2": 2, "doc3": 1}
    assert_and_print(
        expected_output,
        priority_process_documents(documents),
        "Document processing some",
    )
    documents = []
    expected_output = {}
    assert_and_print(
        expected_output,
        priority_process_documents(documents),
        "Document processing some",
    )
