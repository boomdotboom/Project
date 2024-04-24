import sys
import traceback
import logging
import Sports

try:
    Sports.open_database()  # open database
    playerId = sys.argv[1]
    teamId = sys.argv[2]
    name = sys.argv[3]
    position = sys.argv[4]
    values = "'"+ str(playerId) + "','" + str(teamId) + "," + name + "','" +  position +  "'"

    Sports.insert("Player", values)
    res = Sports.executeSelect('SELECT * FROM Player;')
    res = res.split('\n') 
    print("<br/>" + "<br/>")
    print("<br/>" + "Table Player after:"+"<br/>" + res[0] + "<br/>"+res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
        
    html_content = '''        '''
    Sports.close_db()  # close db
except Exception as e:
    print("Error in add_player.py")
    logging.error(traceback.format_exc())

# Parse command line arguments

# Add the game
#Sports.add_player(playerId, teamId, name, position)