from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        # ✅ SECURE LINE ✅
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        conn.close()

        if result:
            return "✅ Login successful!"
        else:
            error = "❌ Invalid credentials."

    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
