import sys
import traceback
import logging
import Sports

def add_player(playerId,teamId,name,position):
    try:
        Sports.open_database()  # open database
        
        values = "'"+ str(playerId) + "','" + str(teamId) + "," + name + "','" +  position +  "'"

        Sports.insert("Team", values)
        res = Sports.executeSelect('SELECT * FROM Team;')
        res = res.split('\n') 
        print("<br/>" + "<br/>")
        print("<br/>" + "Table Team after:"+"<br/>" + res[0] + "<br/>"+res[1] + "<br/>")
        for i in range(len(res)-2):
            print(res[i+2]+"<br/>")
            
        html_content = '''        '''
        Sports.close_db()  # close db
    except Exception as e:
        print("Error in add_player.py")
        logging.error(traceback.format_exc())

# Parse command line arguments
playerId = sys.argv[1]
teamId = sys.argv[2]
name = sys.argv[3]
position = sys.argv[4]

# Add the game
add_player(playerId=playerId, teamId=teamId, name=name, position=position)