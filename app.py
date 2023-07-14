from flask import Flask,render_template,request
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="honeychild")
mycursor=mydb.cursor()

app=Flask(__name__)
@app.route('/')
def web():
    return render_template("/Webpage.html")

@app.route('/Webpage')
def webp():
    return render_template('/Webpage.html')

@app.route('/category')
def cat():
    return render_template('/category.html')
@app.route('/About')
def about():
    return render_template('/About.html')

@app.route('/register')
def reg():
    return render_template('/register.html')

@app.route('/submit-register',methods=['GET'])
def sreg():
    fname=request.args.get('fname')
    lname=request.args.get('lname')
    email=request.args.get('email')
    pno=request.args.get('pno')
    spass=request.args.get('spass')
    cpass=request.args.get('cpass')
    if(spass==cpass):
        query="INSERT INTO signup (FirstName, LastName,Email,PhoneNumber,ConfirmPassword) VALUES (%s,%s,%s,%d,%s)"
        data=(fname,lname,email,pno,cpass)
        mycursor.execute(query,data)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return render_template('/LoginPage.html')
    else:
        return render_template('/register.html')
@app.route('/LoginPage')
def login():
    return render_template("/LoginPage.html")




if("__main__"==__name__):
    app.run()