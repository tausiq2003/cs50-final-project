
from flask import Flask, render_template, request
from flask_mail import Mail, Message

import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
#write your email address here
app.config['MAIL_USERNAME'] = 'EMAIL ADDRESS'
#write your password here, app password
app.config['MAIL_PASSWORD'] = 'PASSWORD'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/sent', methods=['GET', 'POST'])
def send():
    #if the method is post
    if request.method=='POST':
        if "email" in request.form:
            # Get the email
            email = request.form.get("email")
            # message header
            msg = Message("You got the mail for the newsletter.", sender='noreply@gmail.com', recipients=[email])
            #message body
            msg.body="Hey how are you? You might have ran my newsletter project. Don't worry you are recieving this mail once. Thanks"
            #send the message
            mail.send(msg)
            return render_template("success.html")
        else:
            # Return an error message if the "email" field is not found
            return "Error: The 'email' field is missing from the form data."
    else: 
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)