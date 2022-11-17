import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import datetime
import requests
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
    # todays_fed_rate = random.randrange(20000,30000)
    # now =datetime.datetime.now()
    # now2 = now.strftime("%Y-%m-%d")
    # def sendgrid_emails():
    #     message = Mail(from_email='ravisaravanan209@gmail.com',
    #                   to_emails=email,
    #                   subject='You Applied for Plasma Donation !!!' + now2,
    #                   html_content="Thanks for Blood donating<br/>"\
    #                      "Hi "+name+"<br><br><br>"
    #                       "Your Reference number " + str(todays_fed_rate) +"<br><br><br>"\
    #                       "Your Details are send to the Nearest plasma Donor centre From Your Location. For Furthur deatails You may contact the Plasma Donation Centre.<br>and the details provided in the website.<br><br><br><br>"\
    #                         " Thanks!<br>"\
    #                         "Plasma Donor Service")
    #     sg = SendGridAPIClient("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")
    #     response = sg.send(message)
    #     print(response.status_code, response.body)


    # sendgrid_emails()
    if district=='chennai' or district =='vellore' or district == 'thiruvallur' or district=='kanchipuram':
      return render_template('North.html', msg="Data saved successfuly")
    elif district=='cuddalore' or district =='villupuram' or district == 'trichy' or district=='mayiladudurai' or district=='thanjavure':
      return render_template('East.html', msg="Data saved successfuly")
    elif district=='erode' or district =='coimbatore' or district == 'thruppur' or district=='karur' or district=='theni':
      return render_template('West.html', msg="Data saved successfuly")
    elif district=='madurai' or district =='kanyakumari' or district == 'thoothukudi' or district=='ramanathapuram' or district=='dindugal':
      return render_template('South.html', msg="Data saved successfuly")
    else:
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
    now =datetime.datetime.now()
    now2 = now.strftime("%Y-%m-%d")
    todays_fed_rate = random.randrange(20000,30000)
    
    def sendgrid_email():
      message = Mail(from_email='ravisaravanan209@gmail.com',
                      to_emails='ravisaravanan209@gmail.com',
                      subject='You Applied for Plasma Donation !!!' + now2,
                      html_content="Thanks for Blood donating<br/>"\
                         "Hi "+name+"<br><br><br>"
                          "Your Reference number " + str(todays_fed_rate) +"<br>"\
                          "Your Details are send to the Nearest plasma Donor centre From Your Location.<br><br><br><br>"\
                            " Thanks!<br>"\
                            "Plasma Donor Service")
      sg = SendGridAPIClient("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")
      response = sg.send(message)
      print(response.status_code, response.body)
    sendgrid_email()
    if district=='chennai' or district =='vellore' or district == 'thiruvallur' or district=='kanchipuram':
      return render_template('North.html', msg="Data saved successfuly")
    elif district=='cuddalore' or district =='villupuram' or district == 'trichy' or district=='mayiladudurai' or district=='thanjavure':
      return render_template('East.html', msg="Data saved successfuly")
    elif district=='erode' or district =='coimbatore' or district == 'thruppur' or district=='karur' or district=='theni':
      return render_template('West.html', msg="Data saved successfuly")
    elif district=='madurai' or district =='kanyakumari' or district == 'thoothukudi' or district=='ramanathapuram' or district=='dindugal':
      return render_template('South.html', msg="Data saved successfuly")
    else:
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