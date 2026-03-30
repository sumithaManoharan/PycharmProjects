##################### Extra Hard Starting Project ######################
import smtplib,random,pandas as pd,os
from email.message import EmailMessage
from datetime import datetime as dt

my_email = "sumitha.manoharan@zohomail.in"
zoho_password="7sb2uDCFvT15"
bdays = pd.read_csv('birthdays.csv')



# 1. Update the birthdays.csv
def update_status(today_filter):
    bdays.loc[today_filter, "status"] = f"Sent {dt.now().year}"
    # 3. Save the changes
    bdays.to_csv("birthdays.csv", index=False)



def choose_file(row):
    text_files = os.listdir('letter_templates')
    text_file = random.choice(text_files)

    with open("letter_templates/" + text_file, "r") as file:
        text = file.read()
    final_message = text.replace("[NAME]", row["name"])
    msg = EmailMessage()
    msg.set_content(final_message)
    msg['Subject'] = "Happy Birthday!"
    msg['From'] = my_email
    msg['To'] = row["email"]
    return msg


# 2. Check if today matches a birthday in the birthdays.csv
def send_email():
    day,month = dt.now().day,dt.now().month
    today_filter = (bdays["month"] == month) & (bdays["day"] == day)
    birthday_rows = bdays[today_filter]

    if not birthday_rows.empty:
            with smtplib.SMTP('smtp.zoho.in',587) as connection:
                connection.starttls()
                connection.login(my_email,zoho_password)
                for index,row in birthday_rows.iterrows():
                    msg = choose_file(row)
                    connection.send_message(msg)
                update_status(today_filter)



send_email()




