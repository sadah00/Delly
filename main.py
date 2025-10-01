from flask import Flask,render_template,request

app = Flask(__name__)

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

        
    return render_template("login.html")

@app.route('/register') 
def register():  
    return render_template("register.html")

@app.route('/shop') 
def shop():  
    return render_template("shop.html")

app.run(debug=True)