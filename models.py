import sqlite3

def save_message(name,message):
    print(name, message)
    # connecting to database, and setting up code variables
    conn = sqlite3.connect('Database.db')  # Connecting or creating a database from filepath
    cursor = conn.cursor() # not needed, but for better code

    # creates table for submissons
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                        name TEXT NOT NULL,
                        message TEXT NOT NULL
                    )''')

    # inserting and then commiting new data
    cursor.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (str(name), str(message)))
    conn.commit()  # Commit changes to the database

def login_func(username, password):
    # connecting to database, and setting up code variables
    conn = sqlite3.connect('Database.db')  # Connecting or creating a database from filepath
    cursor = conn.cursor() # not needed, but for better code

    # creates table for submissons
    cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                    )''')

    # Checking for data in rows 
    for name in (username, password): 
        cursor.execute("SELECT rowid FROM accounts WHERE (username, password) = (?, ?)", (username, password))
        data=cursor.fetchone()
        if data is None:
            print('There is no component named %s'%name)
            # inserting and then commiting new data
            cursor.execute("INSERT INTO accounts (username, password) VALUES (?, ?)", (str(username), str(password)))
            conn.commit()  # Commit changes to the database
        else:
            print('Component %s found with rowid %s'%(name,data[0]))