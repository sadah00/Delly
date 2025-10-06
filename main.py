from flask import Flask,render_template,request,redirect ,url_for,flash,session
from database import insert_user,check_user
from flask_bcrypt import Bcrypt

app = Flask(__name__)

bcrypt = Bcrypt(app)

app.secret_key = 'delicate'

@app.route('/') 
def home():  
    return render_template("index.html")

@app.route('/contact') 
def contact():  
    return render_template("contact.html")

@app.route('/login', methods=['GET', 'POST'])
def login():  
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        
        registered_user = check_user(email)
        print(registered_user)
        if not registered_user:
            flash("User doesn't exist,Please Register","danger")
            return redirect(url_for('register'))
        else:
            if bcrypt.check_password_hash(registered_user[-1],password):
                flash("Logged in Successfully","Success")
                session["email"]=email
                return redirect(url_for("shop"))
            else:
                flash("Password incorrect,try again","danger")
        
    return render_template("login.html")

@app.route('/register',methods=['GET', 'POST']) 
def register(): 
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        password = request.form['password']
        existing_user = check_user(email)

        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (name,email,phone_number,hashed_password)
            insert_user(new_user)
            flash("User registered successfully","success")
            return redirect(url_for('register'))
        
        else:
            flash("User already exists,please login","danger") 
    return render_template("register.html")

@app.route('/shop') 
def shop():  
    return render_template("shop.html")

app.run(debug=True)