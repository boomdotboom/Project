import sys
import Sports

Sports.open_database()


date = sys.args[1]
res= Sports.view_results_by_date()
res = res.split('\n')  # split the header and data for printing
print("<br/>" + "<br/>")
print("<br/>" + "Table Game after:"+"<br/>" +
          res[0] + "<br/>"+res[1] + "<br/>")
for i in range(len(res)-2):
    print(res[i+2]+"<br/>")
