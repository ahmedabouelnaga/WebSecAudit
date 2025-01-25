from flask import render_template, request, session, redirect
from webapp import app
from webapp.db import insert_db, query_db
import bcrypt
import secrets
def log_action(action, username=False):
    user_agent = request.headers.get('User-Agent','none')
    if not username:
        username = session.get("username")
    try:
        insert_db(app, 'insert into log (username,action,user_agent) values (?,?,?)',[username, action, user_agent])
    except Exception as err:
        print("error logging user activity: {}".format(str(err)))
@app.route("/", methods = ["GET"])
def index(flash=False):
    chats = []
    if session.get("username") != None:
        chats = query_db(app, 'select * from messages ORDER BY id DESC')
    return render_template('index.html', flash=flash, session=session, chats=chats)
@app.route("/post", methods = ["POST"])
def post_msg():
    if session.get("username") != None:
        msg = request.form.get("msg")
        if msg:
            insert_db(app, 'insert into messages (username,msg) values (?,?) ', [session.get("username"), msg])
    return redirect("/")
@app.route("/profile", methods = ["GET"])
def profile():
    if session.get("username") == None:
        return redirect("/login")
    login_history = query_db(app, 'select * from log where username = ? ORDER BY id DESC',[session.get("username")])
    return render_template('profile.html',logs=login_history, session=session)
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        if session.get("username") != None:
            return redirect("/")
        return render_template("login.html")
    username = request.form.get("name")
    password = request.form.get("pass")
    if not username or not password:
        return render_template("login.html", flash=("error", "Invalid credentials"))
    try:
        users = query_db(app, 'select * from users where username = ? LIMIT 1',[username])
        if not users:
            return render_template("login.html", flash=("error", "Invalid credentials"))
        user = users[0]
        db_password = user["password"]
        if isinstance(db_password, str):
            db_password = db_password.encode()
        if bcrypt.checkpw(password.encode(), db_password):
            session["username"] = user["username"]
            log_action("login")
            return index(flash=("success", "Welcome back!"))
        return render_template("login.html", flash=("error", "Invalid credentials"))
    except Exception:
        return render_template("login.html", flash=("error", "Invalid credentials"))
@app.route('/check_exists', methods = ['POST'])
def check_username_exists():
    try:
        username = request.form.get("name")
        if username != None:
            user = query_db(app, 'select * from users where username = ? limit 1',[username])
            if user != None and len(user)>0:
                return "taken"
    except:
        return "error"
    return "free" 
@app.route('/logout', methods = ['GET'])
def logout():
    log_action("logout")
    session.clear()
    return redirect("/")
@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == 'GET':
        if session.get("username") != None:
            return redirect("/")
        return render_template("register.html")
    username = request.form.get("name")
    password = request.form.get("pass")
    if not username or not password:
        return render_template("register.html", flash=("error", "Invalid input"))
    try:
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        insert_db(app, 'insert into users (username,password) values (?,?)',[username, hashed_pw])
        log_action("register", username=username)
        return render_template("login.html",flash=("success", "Registration successful"))
    except Exception:
        return render_template("register.html", flash=("error", "Registration failed"))
