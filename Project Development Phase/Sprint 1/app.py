from flask import Flask,render_template, request, redirect, url_for, session
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=yms18726;PWD=Qht1YjPwqC5jZErM",'','')

app = Flask(__name__)

@app.route("/")
def log():
    return render_template('login.html')

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/register',methods = ['POST', 'GET'])
def register():
  if request.method == 'POST':

    name = request.form['username']
    email = request.form['email']
    password = request.form['password']
 
    sql = "SELECT * FROM register WHERE email =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      return render_template('login.html', msg="You are already signed up, please login using your correct details")
    else:
      insert_sql = "INSERT INTO register VALUES (?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, email)
      ibm_db.bind_param(prep_stmt, 3, password)
      ibm_db.execute(prep_stmt)
    
    return render_template('login.html', msg="Hurry! your details saved successfully...Please login using your details")

@app.route('/login',methods=['POST'])
def login():
  
    email = request.form['email']
    password = request.form['password']

    sql = "SELECT * FROM register WHERE email =? AND password=?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.bind_param(stmt,2,password)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    if account:
            return render_template('home.html') 
    else:
        return render_template('login.html', msg="Login unsuccessful. Incorrect username / password !")


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()