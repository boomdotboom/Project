import sys
import traceback
import logging
import Sports

Sports.open_database('localhost','aemorton','eT5wisee','aemorton')
Sports.create_tables()
Sports.insert_data()
Sports.close_db()