import sqlite3
from fastapi import FastAPI
data = "study.db"
def initialize_db():
    conn = sqlite3.connect(data) #to store data from study database
    conn.execute("""                       
                 CREATE TABLE sessions (
                     id integer primary key autoincrement,
                     subject text not null,
                     date text not null,
                     duration integer not null
                     note text
                    )
                """)
    conn.commit() #commiting since we want user back after relogging
    conn.close()
initialize_db() #calling the defined function
