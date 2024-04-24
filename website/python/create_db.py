import sys
import traceback
import logging
import Sports

Sports.open_database()

Sports.create_tables()
Sports.insert_data()

res=Sports.executeSelect('Select * From Team;')
res = res.split('\n')  # split the header and data for printing
print("<br/>" + "<br/>")
print("<br/>" + "Table Team after:"+"<br/>" + res[0] + "<br/>"+res[1] + "<br/>")
for i in range(len(res)-2):
    print(res[i+2]+"<br/>")

Sports.close_db()