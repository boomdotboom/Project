import sys
import traceback
import logging
import python_db

mysql_username = 'aemorton'
mysql_password = 'eT5wisee'

try:
    python_db.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database
    team = sys.argv[1]
    query = f"SELECT Nickname, Name FROM Team t NATURAL JOIN Player p WHERE t.Nickname = '{team}';"
    
    res = python_db.executeSelect(query)
    rows = [tuple(row.split(' ', 1)) for row in res.split('\n')[2:] if row.strip()]  # Split each row by the first space and remove header and empty rows
    
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
        <th>Player Name</th>
    </tr>
    {''.join([f'<tr><td>{row[0]}</td><td>{row[1]}</td></tr>' for row in rows])}
    </table>

    </body>
    </html>
    '''
    
    print(html_content)
    python_db.close_db()  # close db
except Exception as e:
    print("Error in add_game.py")
    logging.error(traceback.format_exc())
