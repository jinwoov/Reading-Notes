import pytest

from stack import Stack

def test_stack_instance():
    stack = Stack()

def test_is_empty():
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_is_empty_afer_push():
    stack = Stack()
    stack.push("apples")
    actual = stack.is_empty()
    expected = False
    assert actual == expected

def test_peek_with_stuff():
    stack = Stack()
    stack.push("banana")
    actual = stack.peek()
    expected = "banana"
    assert actual = expected

def test_peek_when_empty():
    stack = Stack()
    
    with pytest.raises(IndexError)
        actual = stack.peek()

def test_pop_with_stuff():
    stack = Stack()
    stack.push("cucumbers")
    expected = "cucumber"
    assert actual == expected 

def test_pop_empty():
    stack = Stack()
    
    with pytest.raises(IndexError)
    actual = stack.pop()