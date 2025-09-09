# SQL Injection Playground with Detection Engine

## 🧪 Purpose
This is a deliberately vulnerable Flask-based login application that demonstrates how SQL Injection (SQLi) works — along with a Python detection tool and a fixed version using secure coding practices.

---

## 🚀 How to Use

### 1. Install dependencies:
pip install flask requests

### 2. Run the vulnerable app:
python app.py
App runs at http://127.0.0.1:5000

### 3. Test SQL Injection:

python sqli_detector.py

### 4. Run the secure version:
python fixed_app.py
💥 Example SQLi Payloads
' OR '1'='1

' OR 1=1 --

' OR 'x'='x

###📄 Files
app.py - vulnerable Flask app

sqli_detector.py - Python script to test SQL injection

fixed_app.py - secure version using parameterized queries

templates/login.html - login page

users.db - SQLite database (auto-created)

### 🛡️ Key Takeaways
SQL Injection is real and dangerous.

You must use parameterized queries to avoid it.

Logging attacks can help detect attempts.


