import sqlite3
def create_table():
    conn = sqlite3.connect('documents.db')
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXIST DOCUMENT(
            id TEXT PRIMARY KEY,
            name TEXT,
            role TEXT,
            gender TEXT,
            status TEXT)''')
    conn.commit()
    conn.close()


def fetch_employees():
    conn = sqlite3.connect('documents.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM DOCUMENT')
    employees = cursor.fetchall()
    conn.close()
    return employees


def insert_employee(id, name, role, gender, status):
    conn = sqlite3.connect('documents.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO DOCUMENT (id, name,role, gender,status) VALUES (?,?,?,?,?)',
                       (id, name,role, gender, status))
    conn.commit()
    conn.close()


def delete_employee(id):
    conn = sqlite3.connect('documents.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM DOCUMENT WHERE id = ?',(id,))
    conn.commit()
    conn.close()

def update_employees(new_name, new_role, new_gender,new_status,id):
    conn = sqlite3.connect('documents.db')
    cursor =conn.cursor()
    cursor.execute('UPDATE DOCUMENT  SET name =?, role =?, gender=?, status =? WHERE id =?',
                   (new_name,new_role,new_gender,new_status,id))
    conn.commit()
    conn.close()



def id_exist(id):
    conn = sqlite3.connect('documents.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM DOCUMENT WHERE id =?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0



