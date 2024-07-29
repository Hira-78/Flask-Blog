from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
import os
import math

with open("config.json", "r") as config:
    params = json.load(config)['params']


local_server = True
app = Flask(__name__)
app.secret_key = "mysecretkey"

# for sending mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = params['gmail_user']
app.config['MAIL_PASSWORD'] = params['gmail_password']
mail = Mail(app)

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email_id = db.Column(db.String(30), nullable=False)
    phone_num = db.Column(db.String(20), nullable=False)
    mesg = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    tagline = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    img_file = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())


@app.route("/")
def home():
    # Get all posts from the database
    posts = Posts.query.filter_by().all()

    # Calculate the number of posts per page
    num_of_posts = int(params['no_of_posts'])

    # Calculate the total number of pages
    last = math.ceil(len(posts) / num_of_posts)

    # Get the current page from the request arguments
    page = request.args.get('page')
    if not str(page).isnumeric():
        page = 1
    page = int(page)

    # Slice the posts list to get only the posts for the current page
    posts = posts[(page - 1) * num_of_posts:page * num_of_posts]

    # Determine the previous and next page URLs
    if page == 1:
        prev = '#'
        next = f"/?page={page + 1}"
    elif page == last:
        prev = f"/?page={page - 1}"
        next = '#'
    else:
        prev = f"/?page={page - 1}"
        next = f"/?page={page + 1}"

    # Render the template with the posts and pagination links
    return render_template("index.html", params=params, posts=posts, prev=prev, next=next)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, email_id=email, phone_num=phone, mesg=message)
        db.session.add(entry)
        db.session.commit()
        # mail.send_message("New Message from CodingThunder Blog Website from " + name, sender=email,
        #                   recipients=params['gmail_user'], body=message + "\n" + "Contact: " + phone )
    return render_template("contact.html", params=params)


# enter /post/1 in url
@app.route("/post/<string:post_slug>", methods=['GET'])
def post(post_slug):
    my_post = Posts.query.filter_by(slug=post_slug).first()
    return render_template("post.html", params=params, post=my_post)


# enter /post/1 in url
@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit_post(sno):
    if "user" in session and session['user'] == params['admin_username']:
        if request.method == "POST":
            new_title = request.form.get('title')
            new_tagline = request.form.get('tagline')
            new_slug = request.form.get('slug')
            new_content = request.form.get('content')
            new_img_file = request.form.get('img_file')
            new_datetime = datetime.now()

            if sno == "0":
                new_post = Posts(title=new_title, slug=new_slug, tagline=new_tagline, content=new_content, img_file=new_img_file, date=new_datetime)
                db.session.add(new_post)
                db.session.commit()
            else:
                new_post = Posts.query.filter_by(sno=sno).first()
                new_post.title = new_title
                new_post.tagline = new_tagline
                new_post.slug = new_slug
                new_post.content = new_content
                new_post.img_file = new_img_file
                new_post.date = new_datetime
                db.session.commit()
                return redirect("/edit/"+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template("edit.html", params=params, post=post)


@app.route('/delete/<string:sno>', methods=['GET', 'POST'])
def delete_post(sno):
    if "user" in session and session['user'] == params['admin_username']:
        post_to_delete = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post_to_delete)
        db.session.commit()

    return redirect("/dashboard")


@app.route("/about")
def about():
    return render_template("about.html", params=params)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    # Check if the user is logged in
    if "user" in session and session['user'] == params['admin_username']:
        posts = Posts.query.all()
        return render_template("dashboard.html", params=params, posts=posts)

    # Handle login form submission
    if request.method == "POST":
        username = request.form.get('name')
        password = request.form.get('password')
        if username == params['admin_username'] and password == params['admin_password']:
            session['user'] = username
            posts = Posts.query.all()
            return render_template("dashboard.html", params=params, posts=posts)

    # If not logged in or login failed, show the login page
    return render_template("login.html", params=params)




# optional file uploader
@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if "user" in session and session['user'] == params['admin_username']:
        if request.method == 'POST':
            f = request.files['file']
            f.save(os.path.join(params['upload_location'], secure_filename(f.filename)))
            return "Uploaded Successfully"


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('dashboard')


if __name__ == "__main__":
    app.run(debug=True)
