import emoji
from flask import Flask, request, redirect,flash, render_template
from flask.ext.wtf import Form
from twilio.rest import TwilioRestClient
import twilio.twiml
from wtforms import TextField
from wtforms.validators import Required, Length, ValidationError
import os

app = Flask(__name__)


'''
validators
'''

def isValid(form, phoneNumber):
  rawTextField = str(phoneNumber)
  valueDesiredString = "value="
  valueIndex = rawTextField.index(valueDesiredString) +6
  numStr = rawTextField[valueIndex:len(rawTextField)-1]
  numStr = (numStr[1:13])
  print(numStr)
  print(len(numStr))
  if len(numStr)!= 12 or numStr[0] != "+" or not str.isdigit(numStr[1:13]):
      raise ValidationError("Your phone number isn't a valid US/Canada number")

'''
classes
'''
class MyForm(Form):
  failedCall = False
  phoneNumber = TextField('phoneNumber', validators=[Required(), Length(min=12, max=12),isValid])



'''
Twilio routes
'''

@app.route('/text')
def text():
    # put your own credentials here 
     pizza_emoji = (emoji.emojize(':slice_of_pizza:'))
     account_sid = 'AC1cc3d40a4dca1cd0ff1af031ff1b14ca'
     auth_token = '' 
     client = TwilioRestClient(account_sid,auth_token) 
     client.messages.create(
            to="+19167516308", 
            from_="19164762325",
            body = 'ayy lmao' + pizza_emoji
            )
     return 'truuu'

@app.route('/')
def hello():
    return 'Hello World!'
'''
@app.route('/view')
def view():
'''

if __name__ == "__main__":
    app.run(debug=True)
