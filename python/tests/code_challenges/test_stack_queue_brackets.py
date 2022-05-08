import pytest
from code_challenges.stack_queue_brackets import multi_bracket_validation
from code_challenges.duckduckgoose import duck_duck_goose


def test_validates_josephuss():
    namelist = 'A', 'B', 'C', 'D', 'E'
    actual = duck_duck_goose(namelist, 3)
    expected = 'D'
    assert actual == expected

def test_validates_two_square_brackets():
    actual = multi_bracket_validation("[]")
    expected = True
    assert actual == expected


def test_fails_two_square_brackets_flipped():
    actual = multi_bracket_validation("][")
    expected = False
    assert actual == expected


def test_validates_two_braces():
    actual = multi_bracket_validation("{}")
    expected = True
    assert actual == expected


def test_fails_two_braces_flipped():
    actual = multi_bracket_validation("}{")
    expected = False
    assert actual == expected


def test_validates_two_parentheses():
    actual = multi_bracket_validation("()")
    expected = True
    assert actual == expected


def test_fails_two_parentheses_flipped():
    actual = multi_bracket_validation(")(")
    expected = False
    assert actual == expected



def test_multi():
    actual = multi_bracket_validation("{}(){}")
    expected = True
    assert actual == expected


def test_nested():
    actual = multi_bracket_validation("{([])}")
    expected = True
    assert actual == expected


def test_round_nested():
  actual = multi_bracket_validation("((((((((((()))))))))))")
  expected = True
  assert actual == expected


def test_round_nested_uneven():
  actual = multi_bracket_validation("(((((((((())))))")
  expected = False
  assert actual == expected

def test_mismatched():
    actual = multi_bracket_validation("[}")
    expected = False
    assert actual == expected

def test_random():
  actual = multi_bracket_validation("(([[[((([}}})))")
  expected = False
  assert actual == expected
