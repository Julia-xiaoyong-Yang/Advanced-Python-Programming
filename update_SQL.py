#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import sqlite3
import logging

class UpdateSQL:
    """Define a class to update the SQL data."""
    def __init__(self) -> None:
        """Initialize 'UpdateSQL' class with a logger for logging information"""
        logging.basicConfig(
            filename= 'C:/Users/charmingstar/dev/update_SQL_log.log',
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)
        
    def update_sql_table(self, data, table_name, db_name):
        """Update the SQL data or create the database file."""
        try:
            self.logger.info(f"Connecting to database: {db_name}")
            conn = sqlite3.connect(db_name)
            self.logger.info(f"Database connected successfully: {db_name}")

            # Save the cleaned data to the SQL table
            data.to_sql(table_name, conn, if_exists='replace', index=False)
            self.logger.info(f"Data saved to table '{table_name}' successfully.")
            
            conn.close()
            self.logger.info(f"SQL table updated successfully.")
        except Exception as e:
            self.logger.error(f"Error during updating SQL table: {e}")
            raise