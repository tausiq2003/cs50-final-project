**Newsletter System**


####VIDEO DEMO: https://youtu.be/tTEnW0iJ8jg

#### DESCRIPTION:

One Liner: This is my final project for cs50x, and I have implementated  a newsletter system. Don't worry, it will send you email once.

Usage: To use the application give your email and password at line 11 and 13 in sent_mail.py

So, this is my own cs50x 's final project, in this project I have implementated a newsletter system, at first when you ran the application index.html, gets loaded up and you will see a good designed page using CSS. Also, you will see an input field, if you type something outside of that mail domain list, like here ```mail_list = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "outlook.com", "icloud.com", "zoho.com", "fastmail.com", "mail.com", "protonmail.com", "rediffmail.com"]```, then you will get an error, Secondly, if you type an email that is being used you will get an error.

So, whats in the app.py, if the request method is post, it gets the email fields checks the email using regular expressions, and then using that email it retrieves from the table if there is same email that you are signed up or not, if email is correct and no redundancy is there, it goes to sent_mail.py, where as mentioned above in Usage, you type your mail and password and then you will get an email, where msg contains the header, sender and recipients and body contains the message. I have placed noreply@gmail.com, where you can mention your mail, or leave as it is. Then, you are good to go, mail is sent and its successful.

I have used flask_mail, sqlite3 and re modules and SQLite3 for this project. Also, added an animation with css, because I want it to better than other newsletter websites.

Thank you.
