import sys
import Sports

Sports.open_database()
conference = sys.args[1]
res= Sports.view_teams_by_conference(conference)
print("<br/>" + "<br/>")
print("<br/>" + "Table Game after:"+"<br/>" +
          res[0] + "<br/>"+res[1] + "<br/>")
for i in range(len(res)-2):
    print(res[i+2]+"<br/>")