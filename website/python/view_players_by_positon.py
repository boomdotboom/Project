import sys
import Sports

position = sys.argv[1]
Sports.view_players_by_position(position)
# res = res.split('\n')  # split the header and data for printing
# print("<br/>" + "<br/>")
# print("<br/>" + "Table Player after:"+"<br/>" +
#           res[0] + "<br/>"+res[1] + "<br/>")
# for i in range(len(res)-2):
#     print(res[i+2]+"<br/>")