from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS visitors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT NOT NULL,
                port INTEGER NOT NULL
            )
        ''')

@app.route('/')
def index():
    visitor_ip = request.remote_addr
    visitor_port = request.environ.get('REMOTE_PORT')

    with sqlite3.connect('database.db') as conn:
        conn.execute('INSERT INTO visitors (ip_address, port) VALUES (?, ?)', (visitor_ip, visitor_port))
        cursor = conn.execute('SELECT * FROM visitors')
        visitors = [{'id': row[0], 'ip_address': row[1], 'port': row[2]} for row in cursor.fetchall()]

    return render_template('index.html', visitors=visitors)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
