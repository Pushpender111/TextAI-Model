from flask import Flask,render_template,request,redirect,session
from db import database
import api
dbo=database()
app =Flask(__name__)
app.secret_key="Randomstringtoprovidesecuritytosystem"
@app.route('/')
def index():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/registering',methods=['POST'])
def registring():
    print("something something")
    Name=request.form.get('name')
    password=request.form.get("password")
    email=request.form.get("email")
    response=dbo.insert(Name,email,password)
    if response:
        return render_template('login.html',message="Registeration Succesfull, Kindly login now")
    else:
        return render_template('register.html',message="Email already exist, Kindly login now")
@app.route('/perform_login',methods=['POST'])
def perform_login():
    password=request.form.get("Password")
    email=request.form.get("email")
    response=dbo.user_exist(email,password)
    if response:
        session["user"]=email
        return redirect("/profile")
    else:
        return render_template('login.html',message="Incorrect email or password")
@app.route('/profile')
def profile():
    if 'user' not in session:   # agar session me user nahi hai
        return redirect('/')
    return render_template('profile.html')


@app.route('/ner')
def ner():
    if 'user' not in session:   # agar session me user nahi hai
        return redirect('/')
    return render_template('ner.html')
@app.route('/perform_ner',methods=['POST'])
def perform_ner():
    para=request.form.get("para")
    
    # print(entity)
    
    try:
        response=api.ner(para)
        # print(response)
        # return "result"
        return render_template('ner.html',message=response)
    except Exception as e:
        print("Error occurred:", e)
        return render_template('ner.html',error=e)
    
    
    


    

@app.route('/sentiment_analysis')
            
def sentiment_analysis():
    if 'user' not in session:   # agar session me user nahi hai
        return redirect('/')
    return render_template("sentiment_analysis.html")
@app.route("/analyse_sentiment" ,methods=['POST'])
def analyse_sentiment():
    para=request.form.get("para")
    try:
        response=api.sentiment_analysis(para)
        return render_template("sentiment_analysis.html",message=response)
    except Exception as e:
        print("Error Occured: ", e)
        return render_template("sentiment_analysis.html",error=e)


# @app.route('/Abuse_detection')
# def Abuse_detection():
#     return "Abuse_detection hoga yah"
app.run(debug=True)