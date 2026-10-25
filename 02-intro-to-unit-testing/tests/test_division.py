"""Baseline divide tests for the parametrization refactor."""

# @TODO Exercise (file-based):
# Objective: Refactor this baseline test into a parameterized pytest test.
# Edit files:
# - tests/test_division.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_division.py
# Solution:
# - tests/test_division_solution.py
# - 02-intro-to-unit-testing.ipynb (<summary>Solution</summary> block)

from src.unit_test_examples.division import divide
import pytest


@pytest.mark.parametrize(
    "x, y, expected_result",
    [
        (3, 2, 1.5),
        (5, 5, 1),
        (6, 2, 3),
        (-2, 0, "Cannot divide by zero"),
        (10, -2, -5),
    ],
)
def test_divide_parametrized(x, y, expected_result):
    assert divide(x, y) == expected_result
