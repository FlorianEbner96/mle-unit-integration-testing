# @TODO Exercise (file-based):
# Objective: Build and verify an SQLite-to-CSV integration pipeline end-to-end.
# Edit files:
# - src/integration_test_example/db_pipeline.py
# Validate with:
# - ../.venv/bin/python -m pytest -q tests/test_integration_db_pipeline.py
# Solution:
# - 04-intro-to-integration-testing.ipynb (Solution toggle block)

import pandas as pd
from sqlalchemy import create_engine


class DataPipelineDB:
    def __init__(self, input_path, output_path, table_name):
        self.input_path = input_path
        self.output_path = output_path
        self.table_name = table_name

    def run(self):
        data = self.read_data()
        processed_data = self.process_data(data)
        self.write_data(processed_data)
        return processed_data

    def read_data(self):
        engine = create_engine("sqlite:///" + self.input_path, echo=False)
        with engine.connect() as connection:
            return pd.read_sql_table(self.table_name, con=connection)

    def process_data(self, data):
        processed_data = data.copy()
        processed_data["names"] = processed_data["names"].str.upper()
        return processed_data

    def write_data(self, processed_data):
        processed_data.to_csv(self.output_path, index=False)
