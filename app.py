from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q')
    conn = sqlite3.connect('db.sqlite3')
    result = conn.execute("SELECT * FROM users WHERE name = ?", (query,))
    return str(result.fetchall())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)
