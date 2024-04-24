import sys
import traceback
import logging
import Sports

Sports.open_database()
Sports.create_tables()
Sports.insert_data()
Sports.close_db()