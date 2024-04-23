import sys
import traceback
import logging
import Sports
from util import mysql_username, mysql_password

def add_game(gameID, date, location, team1, score1, team2, score2):
    try:
        Sports.open_database()  # open database
        
        next_id = Sports.nextId("Game")
        
        values = "'"+ str(next_id) + "','" + date + "," + location + "','" +  team1 + "','" + team2 + "','" + score1 + "','" + score2 + "','" + date + "'"

        Sports.insert("Game", values)
        res = Sports.executeSelect('SELECT * FROM Game;')
        res = res.split('\n') 
        print("<br/>" + "<br/>")
        print("<br/>" + "Table Game after:"+"<br/>" + res[0] + "<br/>"+res[1] + "<br/>")
        for i in range(len(res)-2):
            print(res[i+2]+"<br/>")
            
        html_content = '''        '''
        Sports.close_db()  # close db
    except Exception as e:
        print("Error in add_game.py")
        logging.error(traceback.format_exc())

# Parse command line arguments
gameID = sys.argv[1]
date = sys.argv[2]
location = sys.argv[3]
team1 = sys.argv[4]
score1 = sys.argv[5]
team2 = sys.argv[6]
score2 = sys.argv[7]

# Add the game
add_game(gameID=gameID, date=date, location=location, team1=team1, score1=score1, team2=team2, score2=score2)