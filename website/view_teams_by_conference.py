import sys
import traceback
import logging
import Sports

mysql_username = 'aemorton'
mysql_password = 'eT5wisee'

try:
    Sports.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database
    conference = sys.argv[1]
    query = f"SELECT t2.Nickname,SUM(IF(g.Score1 < g.Score2, 1, 0)) AS Record FROM Game g, Team t2 WHERE (t2.TeamId = g.TeamId2 OR t2.TeamId=g.TeamId1) AND t2.Conference = '{conference}' GROUP BY t2.Nickname;"
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

    <h2>{conference}</h2>

    <table style="width:100%">
    <tr>
        <th>Team Name</th>
        <th>Result</th>
    </tr>
    {''.join([f'<tr><td>{row[0]}</td><td>{row[1]}</td></tr>' for row in res])}
    </table>

    </body>
    </html>
    '''
    
    print(html_content)
    Sports.close_db()  # close db
except Exception as e:
    print("Error in view_teams_by_conference.py")
    logging.error(traceback.format_exc())
