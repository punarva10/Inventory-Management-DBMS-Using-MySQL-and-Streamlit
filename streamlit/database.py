import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Enterspace@2203",
    database="invento"
)
c = mydb.cursor(buffered=True)

def get_details():
    c.execute('SELECT * FROM part_desc order by customer')
    columns = c.description 
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in c.fetchall()]
    return result

def get_count():
    c.execute('SELECT * FROM part_track')
    columns = c.description 
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in c.fetchall()]
    return result

def get_parts():
    c.execute('SELECT part_name FROM part_desc')
    data = c.fetchall()
    return data

def update_wip(part_name, part_numbers):
    c.execute('UPDATE part_track SET wip = wip + %s WHERE part_name = %s', (part_numbers, part_name))
    mydb.commit()
    return str(c.rowcount)

def update_ng1(part_name, part_numbers):
    c.execute('UPDATE part_track SET ng1 = ng1 + %s WHERE part_name = %s', (part_numbers, part_name))
    mydb.commit()
    return str(c.rowcount)

def update_ng2(part_name, part_numbers):
    c.execute('UPDATE part_track SET ng2 = ng2 + %s WHERE part_name = %s', (part_numbers, part_name))
    mydb.commit()
    return str(c.rowcount)
