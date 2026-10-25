import pandas as pd

# @TODO Exercise (file-based):
# Objective: Implement and test transformation helpers for score creation and aggregation.
# Edit files:
# - src/data_pipeline/transformation.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_transformation.py
# Solution:
# - src/data_pipeline/transformation_solution.py


def is_greater_than_average(series: pd.Series) -> pd.Series:
    # Return one flag per row so the result can be compared with assert_series_equal.
    # Return 0 for values <= mean(series), else 1.
    average = series.mean()
    return pd.Series([0 if value <= average else 1 for value in series])


def get_sum_score_by_brand_and_gender(
    frame: pd.DataFrame,
    brand_col="brand",
    gender_col="menWomen",
    score_by="size_greater_than_average",
) -> pd.DataFrame:
    # Aggregate the row-level score into one total per (brand, gender) pair.
    # Group by brand and gender, then sum the score column.
    return frame.groupby(by=[brand_col, gender_col], as_index=False)[score_by].sum()
