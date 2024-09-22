#!/usr/bin/env python
# coding: utf-8

import logging
import pandas as pd

class DataCleaner:
    """Define a Class to clean the data."""
    def __init__(self) -> None:
        logging.basicConfig(
            filename= 'C:/Users/charmingstar/dev/clean_log.log',
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)

    def clean_data(self, data):
        """Clean data by converting the 'Period' column to datetime."""
        try:
            data['date'] = pd.to_datetime(data['Period'])
            data = data.drop(columns=['Series_title_5'])
            data['Series_reference'] = data['Series_reference'].str.split('.', 1).str[1]
            data['Subject'] = data['Subject'].str.split('-', 1).str[0].str.strip()
            self.logger.info("Convert the 'Period' column to datatime and delete 'Series_title_5' column, removed 'BDCQ' and 'BDC' from 'Series_reference' and 'Subject' respectively.")
            return data
        except Exception as e:
            self.logger.error(f"There are error during processing data: {e}")
            raise