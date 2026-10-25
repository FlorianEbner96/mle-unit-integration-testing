"""Generate emails as <first_name>.<last_name>@neuefische.de."""

# @TODO Exercise (file-based):
# Objective: Generate normalized neuefische email addresses from employee dictionaries.
# Edit files:
# - src/unit_test_examples/email_generation.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_email_generation.py
# Solution:
# - src/unit_test_examples/email_generation_solution.py


def generate_neuefische_emails(employees):
    list = []
    # Normalize each name part before you build the final address.
    for employee in employees:
        employee["first_name"] = employee["first_name"].strip().lower()
        employee["last_name"] = employee["last_name"].strip().lower()
        list.append(
            f"{employee['first_name']}.{employee['last_name']}@neuefische.de")
    return list
