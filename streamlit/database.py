import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Enterspace@2203",
    database="invento"
)
c = mydb.cursor(buffered=True)

wip_queue = []

def get_details():
    c.execute('SELECT * FROM part_desc order by customer')
    columns = c.description 
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in c.fetchall()]
    return result

def get_part_track():
    c.execute('SELECT * FROM part_track_2')
    columns = c.description 
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in c.fetchall()]
    return result

def get_wip_entry():
    c.execute('SELECT * FROM wip_entry')
    columns = c.description 
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in c.fetchall()]
    return result

def get_fg_entry():
    c.execute('SELECT * FROM fg_entry')
    columns = c.description 
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in c.fetchall()]
    return result

def get_sales_entry():
    c.execute('SELECT * FROM sales_entry')
    columns = c.description 
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in c.fetchall()]
    return result

def get_parts():
    c.execute('SELECT part_name FROM part_desc')
    data = c.fetchall()
    return data

def update_wip(part_name, amount, current_date, operator, machine, current_time):
    global wip_queue
    sql = '''
    INSERT INTO part_track_2 (part_name, date, wip, fg, ng, sales)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    wip = wip + %s
    '''

    parameters = (part_name, current_date, amount, 0, 0, 0, amount)

    c.execute(sql, parameters)  
    wip_queue.append(amount)
    c.execute('INSERT INTO Wip_entry VALUES (%s, %s, %s, %s, %s, %s)', (current_date, current_time, operator, machine, part_name, amount))
    
    mydb.commit()
    return str(c.rowcount)

def update_ng1(part_name, amount, current_date, current_time, operator):
    global wip_queue
    wip_value = wip_queue.pop(0)
    c.execute('UPDATE part_track_2 SET fg = fg + %s - %s WHERE part_name = %s AND date = %s', (wip_value, amount, part_name, current_date))

    c.execute('INSERT INTO fg_entry VALUES (%s, %s, %s, %s, %s - %s)', (current_date, current_time, operator, part_name, wip_value, amount))

    c.execute('UPDATE part_track_2 SET ng = ng + %s WHERE part_name = %s AND date = %s', (amount, part_name, current_date))
    mydb.commit()
    return str(c.rowcount)

def update_ng2(part_name, part_numbers):
    c.execute('UPDATE part_track SET ng2 = ng2 + %s WHERE part_name = %s', (part_numbers, part_name))
    mydb.commit()
    return str(c.rowcount)


#What to do: Ask samith about whether or not there is only one place where wip is converted to fg and only one place where fg is converted to sales.