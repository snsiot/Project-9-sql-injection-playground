from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Create database and table
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
c.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'admin123')")
conn.commit()
conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        # 🚨 VULNERABLE LINE 🚨
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        c.execute(query)
        result = c.fetchone()
        conn.close()

        if result:
            return "✅ Login successful!"
        else:
            error = "❌ Invalid credentials."

    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
