import mariadb
import dbcreds
import json

from flask import Flask
app = Flask(__name__)

@app.get('/cars')
def get_cars():
    conn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()
    cursor.execute('CALL get_all_cars()')
    results = cursor.fetchall()
    results_J = json.dumps(results,default=str)
    return(results_J)

app.run(debug=True,port=5006)