
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import datetime
import requests

now =datetime.datetime.now()
now2 = now.strftime("%Y-%m-%d")




todays_fed_rate = "Welcome donor"
yest_fed_rate = "Hi"


    
def sendgrid_email():
    message = Mail(from_email='ravisaravanan209@gmail.com',
                   to_emails='ravisaravanan209@gmail.com',
                   subject='Thanks For the Plasma Donation' + now2,
                   html_content='Plasma Donor Service Your Request was send to Plasma Donation Centre near your Location !!!!'\
                    'Your Referance Number :'\ 
                    'The Plasma Donation centre Tell the next procedure of donation process.'\
                    'Thank You,'\
                    'plasma donor service.')
    sg = SendGridAPIClient("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")
    response = sg.send(message)
    print(response.status_code, response.body)


sendgrid_email()