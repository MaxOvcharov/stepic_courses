#!/usr/bin/python
#-*-coding: utf-8-*-
"""
This script create a database myblog.db with two 
simple tables: 'users' and 'messages'

"""
import os
import sqlite3

class TableCreator(object):
    """
    This class creates a tables 'users', 'messages' 
    in myblog.db with example data. The files myblog.db
    is created in the current directory.

    """

    def __init__(self):
        # Take the path of the current directory.
        self.path = os.path.join(str(os.getcwd()), "myblog.db")
    
    def create_table(self):
        '''
        This function create a table -> users, messages        
        '''
        # Connect to sqlite3, сreate myblog.db in the current directory.
        conn = sqlite3.connect(self.path)
        cur = conn.cursor()
        # Create the table 'users'
        cur.execute('''create table if not exists users
                    (uid INTEGER NOT NULL PRIMARY KEY UNIQUE,
					 name TEXT NOT NULL)''')
        # Create the table 'messages'
        cur.execute('''create table if not exists messages 
                    (uid INTEGER NOT NULL, message TEXT)''')
        # Here some data for example
        example_data1 = [(1,'Alex'), (2,'Jane'), (3,'Max'), (4,'Lui')]
        example_data2 = [(1,'Hi!!!'), (1, 'Hello...'), (1, 'See you late!:)))'),
                         (2, 'Nice to meet you John'), (2, 'Bye-bye...'),
                         (3, 'I am an engineer')]
        # Inserts example data to table -'users'
        cur.executemany('''INSERT OR IGNORE INTO users(uid, name) VALUES(?,?)''', example_data1)
        cur.executemany('''INSERT INTO messages(uid, message) VALUES(?,?)''', example_data2)
        conn.commit()
        # Takes users name and count of messages of this users
        cur.execute('SELECT users.name, count(messages.message) as count_msg FROM users LEFT JOIN messages ON users.uid = messages.uid GROUP BY users.name ORDER BY count_msg DESC')
        result = cur.fetchall()
        cur.close()

        return result

if __name__ == '__main__':

    table = TableCreator()    
    print table.create_table()
    