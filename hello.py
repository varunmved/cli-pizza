from flask import Flask, request, redirect,flash, render_template
from flask.ext.wtf import Form
from twilio.rest import TwilioRestClient
import twilio.twiml
from wtforms import TextField
from wtforms.validators import Required, Length, ValidationError
import os
app = Flask(__name__)

@app.route('/text')
def text():
    # put your own credentials here 
     pizza_emoji = (emoji.emojize(':slice_of_pizza:'))
     account_sid = 'AC1cc3d40a4dca1cd0ff1af031ff1b14ca'
     auth_token  = '5011a96781ef26d63904ca3b8e3ccb35'
     client = TwilioRestClient(account_sid,auth_token) 
     client.messages.create(
            to="+19167516308", 
            fromNum="19164762325",
            body = 'ayy lmao' + pizza_emoji
            )

@app.route('/')
def hello():
    return 'Hello World!'
