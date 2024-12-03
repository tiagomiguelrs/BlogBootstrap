from flask import Flask, render_template, request
import requests
from datetime import datetime
from smtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()
USER_EMAIL = os.environ["USER_EMAIL"]
USER_PASSWORD = os.environ["USER_PASSWORD"]
HOST = os.getenv("HOST")

response = requests.get(url="https://api.npoint.io/efdc6d91a41ba077cbfc")
all_posts = response.json()
all_dates = [datetime.fromisoformat(post["date"]) for post in all_posts]
formated_dates = [date.strftime("%B %d, %Y") for date in all_dates]

def send_email(**kwargs):
    name = kwargs["name"]
    email = kwargs["email"]
    phone = kwargs["phone"]
    message = kwargs["message"]
    full_message = (f"Subject: Blog contact from {email}\n\n"
                    f"{name.title()} with e-mail: {email} and phone number: {phone} sent a message.\n"
                    f"{message}")
    with SMTP(HOST) as smtp:
        smtp.starttls()
        smtp.login(user=USER_EMAIL, password=USER_PASSWORD)
        smtp.sendmail(from_addr=USER_EMAIL, to_addrs=USER_EMAIL, msg=full_message)


app = Flask(__name__)
app.jinja_env.filters['zip'] = zip

@app.route("/")
def home():
    return render_template("index.html",
                           page_titles=("Chuckola Cola Diaries", "Come find the adventures of Mario & Luigi in the Beanbean Kingdom"),
                           image="home",
                           all_posts=all_posts,
                           formated_dates=formated_dates)

@app.route("/about")
def about():
    return render_template("about.html",
                           page_titles=("About Me", "The handsomest prince there is"),
                           image="about")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_email(name=name, email=email, phone=phone, message=message)
        return render_template("contact-sent.html",
                               page_titles=("I see a message", "I will be reading it with a Chuckola Cola"),
                               image="contact",
                               name=name, email=email, phone=phone, message=message)
    else:
        return render_template("contact.html",
                               page_titles=("Contact Me", "I will be flying around"),
                               image="contact")

@app.route("/post/<int:_id>")
def post(_id):
    return render_template("post.html",
                           all_posts=all_posts,
                           formated_dates=formated_dates,
                           _id=_id,
                           image=f"post-{_id}")


if __name__ == "__main__":
    app.run(debug=True)