import sys
import traceback
import logging
import Sports
mysql_username = 'aemorton'  # please change to your username
mysql_password = 'eT5wisee'  # please change to your MySQL password
try:
    Sports.open_database('localhost',mysql_username,mysql_password,mysql_username) # open database
    
    gameID = sys.argv[1]
    date = sys.argv[2]
    team1 = sys.argv[3]
    score1 = sys.argv[4]
    team2 = sys.argv[5]
    score2 = sys.argv[6]
    Sports.add_game(gameID,date,team1,score1,team2,score2)
    res = Sports.executeSelect("SELECT g.Date, t1.Location, t1.Nickname, g.Score1, t2.Location, t2.Nickname, g.Score2, IF(g.Score1>g.Score2, Concat(t1.Nickname,' Won'),Concat(t2.Nickname,' Won')) AS Result FROM Game g JOIN Team t1 on t1.TeamId= g.TeamId1 JOIN Team t2 on t2.TeamId= g.TeamId2;")     
    html_content = f'''<!DOCTYPE html>
    <html>
    <style>
    table, th, td {{
        border:1px solid black;
        border-collapse: collapse;
        padding: 8px;
    }}
    </style>
    <body>

    <h2>Games</h2>

    <table style="width:100%">
    <tr>
        <th>Date</th>
        <th>Team1 Location</th>
        <th>Team1 Nickname</th>
        <th>Team1 Score</th>
        <th>Team2 Location</th>
        <th>Team2 Nickname</th>
        <th>Team2 Score</th>
        <th>Results</th>
    </tr>
    {''.join([f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td><td>{row[5]}</td><td>{row[6]}</td><td>{row[7]}</td></tr>' for row in res])}
    
    </table>

    </body>
    </html>'''
    print(html_content)
    Sports.close_db()  # close db
except Exception as e:
    print("Error in add_game.py")
    logging.error(traceback.format_exc())

# Parse command line arguments

#Sports.add_game(gameID,date,team1,score1,team2,score2)