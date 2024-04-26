import sys
import traceback
import logging
import Sports

mysql_username = 'aemorton'
mysql_password = 'eT5wisee'

try:
    Sports.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database
    team = sys.argv[1]
    query = f"SELECT g.Date, t1.Location, t1.Nickname, g.Score1, t2.Location, t2.Nickname, g.Score2, IF(g.Score1>g.Score2, Concat(t1.Nickname,' Won'),Concat(t1.Nickname,' Lost')) AS Result FROM Game g JOIN Team t1 on t1.TeamId= g.TeamId1 JOIN Team t2 on t2.TeamId= g.TeamId2 WHERE t1.Nickname= '{team}' OR t2.Nickname= '{team}';"
    
    res = Sports.executeSelect(query) 
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <style>
    table, th, td {{
        border:1px solid black;
        border-collapse: collapse;
        padding: 8px;
    }}
    </style>
    <body>

    <h2>Games for {team}</h2>

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
    </html>
    '''
   
    print(html_content)
    Sports.close_db()  # close db
except Exception as e:
    print("Error in view_games_by_team.py")
    logging.error(traceback.format_exc())
