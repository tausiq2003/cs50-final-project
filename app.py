from flask import Flask, render_template, request
import sqlite3
import re
import os
from sent_mail import send

currentDirectory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method=="POST":
        # validate email address
        email = request.form.get("email")
        # here is the domain name list 
        mail_list = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "outlook.com", "icloud.com", "zoho.com", "fastmail.com", "mail.com", "protonmail.com", "rediffmail.com"]
        #regex will search for this pattern
        pattern = r'^[a-zA-Z0-9]+@(?:' + '|'.join(mail_list) + ')$'
        validPattern = re.compile(pattern)
        connection = sqlite3.connect('signup.db')
        cursor = connection.cursor()
        # this command will check if multiple users available or not, if not then proceed
        cursor.execute("SELECT * FROM emails WHERE email = ?", (email,))
        rows = cursor.fetchall()
        connection.commit()
        connection.close()
        #this checks if the pattern matches and data is not there
        if ((validPattern.match(email) != None) and (len(rows) == 0)):
            conn = sqlite3.connect('signup.db')
            c = conn.cursor()
            #it inserts to the database with emails; email, is due to the tuple
            c.execute("INSERT INTO emails(email) VALUES(?)", (email,))
            conn.commit()
            conn.close()
            #this function sends the email
            send()
            return render_template("success.html")
        else:
            return render_template("failure.html")


    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)