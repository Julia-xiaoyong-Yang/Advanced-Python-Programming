#!/usr/bin/env python
# coding: utf-8

import logging
import os
import pandas as pd
from api_data import API
from clean_data import DataCleaner
from update_SQL import UpdateSQL

def setup_logger():
    """Configure logging for the test."""
    logging.basicConfig(
            filename= 'C:/Users/charmingstar/dev/test_pipeline_log.log',
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.INFO
        )   
    return logging.getLogger(__name__)

def test_pipeline():
    """Test the entire data pipeline."""
    logger = setup_logger()
    logger.info("Starting pipeline test...")

    try:
        logger.info("Starting pipeline test.")

        # Test API class    
        api = API()
        csv_file = 'C:/Users/charmingstar/dev/business-financial-data-june-2024-quarter-csv.csv'
        data = api.fetch_data(csv_file)

        assert isinstance(data, pd.DataFrame)
        logger.info("Data fetching test passed.")


        # Test DataCleaner class
        dc = DataCleaner()
        cleaned_data = dc.clean_data(data)

        assert 'date' in cleaned_data.columns
        assert 'Series_title_5' not in cleaned_data.columns

        #Compare the first two rows to the expected values for testing
        assert cleaned_data['Series_reference'].iloc[:2].tolist() == ['SF1AA2CA', 'SF1AA2CA']

        assert all(cleaned_data['Subject'] == 'Business Data Collection')

        logger.info("Data cleaning test passed.")
        
        # Test UpdateSQL class
        ds = UpdateSQL()
        db_name = 'C:/Users/charmingstar/dev/business-financial-data-june-2024-quarter.db'
        table_name = 'my_table'
        ds.update_sql_table(cleaned_data, table_name, db_name)
        assert os.path.exists(db_name)
        
        logger.info("All tests passed successfully.")

    except Exception as e:
        logger.error(f"Test failed: {e}")
        raise

if __name__ == "__main__":
    test_pipeline()

