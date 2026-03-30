from email.message import EmailMessage
import smtplib,random,pandas as pd,os

class Post:
    def __init__(self):
        self.body = ""
        self.title = ""
        self.subtitle = ""

        self.my_email = "sumitha.manoharan@zohomail.in"
        self.zoho_password = "7sb2uDCFvT15"

    def render(self,blog_posts,pid):
        image = f"../static/assets/img/id_{pid}.jpg"
        for blog in blog_posts:
            if blog["id"] == pid:
                self.body = blog["body"]
                self.title = blog["title"]
                self.subtitle = blog["subtitle"]
        return self.body,self.title,self.subtitle,image

    def send_email(self,name,email,phone,message):
        with smtplib.SMTP('smtp.zoho.in', 587) as connection:
            connection.starttls()
            connection.login(self.my_email, self.zoho_password)
            msg = EmailMessage()
            msg.set_content(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
            msg['Subject'] = "Blog Message"
            msg['From'] = self.my_email
            msg['To'] = "sumithamanoharan76@gmail.com"
            connection.send_message(msg)



