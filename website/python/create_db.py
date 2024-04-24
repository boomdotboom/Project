import Sports

Sports.create_tables()
res= Sports.executeSelect("Show Tables;")
res = res.split('\n')  # split the header and data for printing
print("<br/>" + "<br/>")
print("<br/>" + "Table Player after:"+"<br/>" +
    res[0] + "<br/>"+res[1] + "<br/>")
for i in range(len(res)-2):
    print(res[i+2]+"<br/>")
html_content = '''        '''
print(html_content)
Sports.close_db()
