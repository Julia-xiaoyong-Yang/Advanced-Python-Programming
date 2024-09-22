#!/usr/bin/env python
# coding: utf-8
 
import logging
import pandas as pd

class API:
    """Set class to fetch data from API."""
    def __init__(self) -> None:
        """Initialize API class with a logger for logging information"""
        logging.basicConfig(
            filename= 'C:/Users/charmingstar/dev/fetch_data_log.log',
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)

    def fetch_data(self, csv_file):
        """Fetch data from a CSV file."""
        try:
            data = pd.read_csv(csv_file)
            self.logger.info("Data from CSV file has been read.")
            return data
        except Exception as e:
            self.logger.error(f"Error during fetch data from CSV file: {e}.")
            return None
