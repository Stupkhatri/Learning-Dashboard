import sqlite3
from fastapi import FastAPI
#First database, created database
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
    conn.commit()
    conn.close()
initialize_db() #calling the defined function
app = FastAPI()

#Now view feature
@app.get("/entries")
def fetch_dashboard():
    conn = sqlite3.connect(db)
    tb_row = conn.execute("SELECT * FROM study_table").fetchall() #assigned variable name bcuz we had to return value
    conn.close()
    return tb_row
#View done, cuz returned what was in db


#Now editing feature,
@app.put("/entries/{entry_id}")
def edit_entry(entry_id: int):
    conn = sqlite3.connect(db)
    conn.execute('UPDATE study_table set subject = ?, date = ?, duration = ?, note = ? where id = ?', (study_table.subject, study_table.date, study_table.duration, study_table.note, entry_id))
    conn.commit()
    conn.close()
    return {"message": "Entry updated"}
#Edit done, cuz UPDATE replace with new session

#Now delete feature
@app.delete("/entries/{entry_id}")
def del_entry(entry_id: int):
    conn = sqlite3.connect(db)
    conn.execute(" DELETE * FROM study_table where id = ?", (entry_id,))
    conn.commit()
    conn.close()
    return {"message": "Entry deleted"}
#Deleting entry feature done
