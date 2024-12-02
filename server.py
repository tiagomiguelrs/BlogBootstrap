from flask import Flask, render_template
import requests
from datetime import datetime

response = requests.get(url="https://api.npoint.io/efdc6d91a41ba077cbfc")
all_posts = response.json()
all_dates = [datetime.fromisoformat(post["date"]) for post in all_posts]
formated_dates = [date.strftime("%B %d, %Y") for date in all_dates]

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

@app.route("/contact")
def contact():
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