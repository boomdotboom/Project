import sys
import traceback
import logging
import Sports

try:
    Sports.open_database('localhost','aemorton','eT5wisee','aemorton') # open database
    
    gameID = sys.argv[1]
    date = sys.argv[2]
    team1 = sys.argv[3]
    score1 = sys.argv[4]
    team2 = sys.argv[5]
    score2 = sys.argv[6]
    next_id = Sports.nextId("Game" )
    
    values = "'"+ str(next_id) + "','" + str(date)  + "','" +  str(team1) + "','" + str(team2) + "','" + str(score1) + "','" + str(score2) + "','" + str(date) + "'"

    Sports.insert("Game", values)
    res = Sports.executeSelect('SELECT * FROM Game;')
    res = res.split('\n') 
    print("<br/>" + "<br/>")
    print("<br/>" + "Table Game after:"+"<br/>" + res[0] + "<br/>"+res[1] + "<br/>")
    for i in range(len(res)-2):
        print(res[i+2]+"<br/>")
        
    html_content = '''        '''
    print(html_content)
    Sports.close_db()  # close db
except Exception as e:
    print("Error in add_game.py")
    logging.error(traceback.format_exc())

# Parse command line arguments

#Sports.add_game(gameID,date,team1,score1,team2,score2)