import sqlite3
from fastapi import FastAPI
db = "study.db"
def initialize_db():
    conn = sqlite3.connect(db) #to store data from study database
    conn.execute("""                       
                 CREATE TABLE study_table (
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
app = FastAPI()

app.get("/dashboard")
def fetch_dashboard():
    conn = sqlite3.connect(db)
    tb_row = conn.execute("SELECT * FROM study_table")
    tb_row = tb_row.fetchall()
    conn.close()
    return tb_row