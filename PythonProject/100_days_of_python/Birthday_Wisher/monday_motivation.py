import smtplib, random
from email.message import EmailMessage
from datetime import datetime as dt
#----------------------constants----------------------------------#
my_email = "sumitha.manoharan@zohomail.in"
gmail_email = "technocrat.parthiban@zohomail.in"
load_dotenv()
app.config['SECRET_KEY'] = os.environ.get('ZOHO_PASSWORD')

#----------------------------QOD-----------------------------------#

if dt.now().weekday() == 4:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        qod = random.choice(quotes)
    msg = EmailMessage()
    msg["Subject"] = "Monday Motivation Quote"
    msg["From"] = my_email
    msg["To"] = gmail_email
    msg.set_content(qod)
    print(qod)

    with smtplib.SMTP("smtp.zoho.in", 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=zoho_password)
        connection.send_message(msg)






