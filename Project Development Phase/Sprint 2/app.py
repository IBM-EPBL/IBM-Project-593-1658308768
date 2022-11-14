

from flask import Flask, redirect, render_template, request, session, url_for
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=yms18726;PWD=Qht1YjPwqC5jZErM",'','')

app = Flask(__name__)

@app.route("/")
def log():
    return render_template('home.html')


@app.route('/loginn')
def loginn():
  return render_template('login.html')

@app.route('/reques')
def reques():
  return render_template('request.html')

@app.route('/donor')
def donor():
  return render_template('donor.html')

@app.route('/about')
def about():
  return render_template('about.html')

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

@app.route('/plasmarequest',methods = ['POST', 'GET'])
def plasmarequest():
  if request.method == 'POST':

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    bloodgroup = request.form['bloodgroup']
    date = request.form['date']
    address = request.form['address']
    district = request.form['district']
    state = request.form['state']
    age = request.form['age']

    insert_sql = "INSERT INTO plasmarequest VALUES (?,?,?,?,?,?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, name)
    ibm_db.bind_param(prep_stmt, 2, email)
    ibm_db.bind_param(prep_stmt, 3, phone)
    ibm_db.bind_param(prep_stmt, 4, bloodgroup)
    ibm_db.bind_param(prep_stmt, 5, date)
    ibm_db.bind_param(prep_stmt, 6, address)
    ibm_db.bind_param(prep_stmt, 7, district)
    ibm_db.bind_param(prep_stmt, 8, state)
    ibm_db.bind_param(prep_stmt, 9, age)
    ibm_db.execute(prep_stmt)
    
    return render_template('home.html', msg="Data saved successfuly")


@app.route('/donorform',methods = ['POST', 'GET'])
def donorform():
  if request.method == 'POST':

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    bloodgroup = request.form['bloodgroup']
    date = request.form['date']
    address = request.form['address']
    district = request.form['district']
    state = request.form['state']
    age = request.form['age']

    insert_sql = "INSERT INTO donorform VALUES (?,?,?,?,?,?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, name)
    ibm_db.bind_param(prep_stmt, 2, email)
    ibm_db.bind_param(prep_stmt, 3, phone)
    ibm_db.bind_param(prep_stmt, 4, bloodgroup)
    ibm_db.bind_param(prep_stmt, 5, date)
    ibm_db.bind_param(prep_stmt, 6, address)
    ibm_db.bind_param(prep_stmt, 7, district)
    ibm_db.bind_param(prep_stmt, 8, state)
    ibm_db.bind_param(prep_stmt, 9, age)
    ibm_db.execute(prep_stmt)
    
    return render_template('home.html', msg="Data saved successfuly")

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

if __name__=="__main__":
  app.run("0.0.0.0",port=5000)