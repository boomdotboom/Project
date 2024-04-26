import sys
import traceback
import logging
import Sports

mysql_username = 'aemorton'
mysql_password = 'eT5wisee'

try:
    Sports.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database
    playerID = sys.argv[1]
    teamID = sys.argv[2]
    name = sys.argv[3]
    position= sys.argv[4]
    Sports.add_player(playerID,teamID,name,position)
    query=f"Select t.Location,t.Nickname,p.Name,p.position From Player p Join Team t on t.TeamId=p.TeamId Where p.Name='{name}';"
    res=Sports.executeSelect(query)  # Split each row by the first space and remove header and empty rows
    
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

    <h2>Player Added</h2>

    <table style="width:100%">
    <tr>
        <th>Location</th>
        <th>Team Name</th>
        <th>Name</th>
        <th>Position</th>
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
