#!/usr/bin/env python
# coding: utf-8

import logging
from api_data import API
from clean_data import DataCleaner
from update_SQL import UpdateSQL

class Main:
    def __init__(self) -> None:
        """Execute the main code with a logger for logging information"""
        logging.basicConfig(
            filename= 'C:/Users/charmingstar/dev/pipeline_log.log',
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info("Starting data pipeline...")

        # Initialize the classes
        api = API()
        dc = DataCleaner()
        ds = UpdateSQL()

        try:
            """Fetch and process data."""
            csv_file = 'C:/Users/charmingstar/dev/business-financial-data-june-2024-quarter-csv.csv'
            db_name = 'C:/Users/charmingstar/dev/business-financial-data-june-2024-quarter.db'
            table_name = 'my_table'

            data = api.fetch_data(csv_file)

            cleaned_data = dc.clean_data(data)
            if cleaned_data is not None:
                self.logger.info(f"Cleaned data columns: {cleaned_data.columns}")
            else:
                self.logger.error("Cleaned data is None.")
                return

            ds.update_sql_table(cleaned_data, table_name, db_name)
            self.logger.info("Pipeline executed successfully")
            
        except Exception as e:
            self.logger.error(f"Error occurred: {e}")

if __name__ =="__main__":
    Main()