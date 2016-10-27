#!/usr/bin/env python
import os
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
hostname = "192.168.68.194"
numbers = [  '+91974660221', '+918138909396', '+919946125423' ]
def check_ping(hostname):

    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = 1
        print pingstatus
    else:
        pingstatus = 2

    return pingstatus

pstatus = check_ping(hostname)
if pstatus == 2:
   for index in range(len(numbers)):
# Find these values at https://twilio.com/user/account
     account_sid = "AC82216c7d7d8be141a887022ea512f3ab"
     auth_token = "cbbd4c374fee6fe17d1cdada7c2dce3d"
     client = TwilioRestClient(account_sid, auth_token)
     message = client.messages.create(body="test Server id down",
       to=numbers[index],    # Replace with your phone number
       from_="+12012583501") # Replace with your Twilio number

     print(message.sid)
