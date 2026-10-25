"""Normalize text and check whether it reads the same backwards."""

# @TODO Exercise (file-based):
# Objective: Implement palindrome normalization and symmetry check.
# Edit files:
# - src/unit_test_examples/palindrome.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_is_palindrome.py
# Solution:
# - src/unit_test_examples/palindrome_solution.py


def is_palindrome(s):
    # Work step by step so the test failures tell you which assumption broke.
    # 1) Normalize to lowercase.
    s_normalized = s.lower()

    # 2) Remove spaces and punctuation.
    s_nomalized = "".join(c for c in s_normalized if c.isalnum())

    # 3) Compare normalized string with its reverse.
    return s_nomalized == s_nomalized[::-1]
