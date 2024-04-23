import sys
import Sports
Sports.open_database()

player_id = sys.args[1]
team_id= sys.args[2]
name = sys.args[3]
position= sys.args[4]
Sports.add_player(player_id,team_id,name, position)
res=Sports.executeSelect('Select * From Player')
res = res.split('\n')  # split the header and data for printing
print("<br/>" + "<br/>")
print("<br/>" + "Table Player after:"+"<br/>" +
          res[0] + "<br/>"+res[1] + "<br/>")
for i in range(len(res)-2):
    print(res[i+2]+"<br/>")