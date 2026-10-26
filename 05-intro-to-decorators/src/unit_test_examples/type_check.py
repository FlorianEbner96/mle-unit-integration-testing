"""Decorator factory for validating the return type of a wrapped function."""

# @TODO Implementation Target (file-based):
# Objective: Implement a decorator that validates decorated function return types.
# Edit files:
# - src/unit_test_examples/type_check.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_type_check.py
# Solution:
# - src/unit_test_examples/type_check_solution.py


def type_check(correct_type):
    def decorator(function):
        def wrapper(*args, **kwargs):
            type = function(*args, **kwargs)
            if isinstance(type, correct_type):
                return type
            print("Bad Type")
            return None

        return wrapper

    return decorator
