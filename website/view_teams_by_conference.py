import sys
import traceback
import logging
import Sports

mysql_username = 'aemorton'
mysql_password = 'eT5wisee'

try:
    Sports.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database
    conference = sys.argv[1]
    query = f"SELECT t1.Nickname, g.Score1, g.Score2, t2.Nickname FROM Game g Join Team t1 on t1.TeamId=g.TeamId1 Join Team t2 on t2.TeamId=g.TeamId2 WHERE t1.Conference='{conference}';"
    
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

    <h2>Team Players</h2>

    <table style="width:100%">
    <tr>
        <th>Team Name</th>
        <th>Score1</th>
        <th>Score2</th>
        <th>Team Name</th>
    </tr>
    {''.join([f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>' for row in res])}
    </table>

    </body>
    </html>
    '''
    
    print(html_content)
    Sports.close_db()  # close db
except Exception as e:
    print("Error in add_game.py")
    logging.error(traceback.format_exc())
