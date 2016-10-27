from queue import Queue
import os
from twilio.rest import TwilioRestClient
import requests
q = Queue()

class uptimecheck:
  ucount = 0
  def __init__(self):
    
    self.numbers = [ '+919746660221' ]
    self.sleep = 30
    self.timer = 60
    uptimecheck.ucount += 1

    
  def hostPing(self,hostname):
    #import dhost
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:

      pingstatus = 1
      status = q.inqueue(hostname)
      if status is 1:
        print("no init")
      else :
        self.ifUp(hostname)
      print(pingstatus)
      print("status up")
    else:
      pingstatus = 2
      print("status is down")
      msg = hostname + " host is down"
      #dh = open('dhost.py','w+')
      #dh.write(str(hostname))
      status = q.inqueue(hostname)
      if status is 1:
        print("no init")
        print('________________________________________%s________________________________',status)

        self.sms(msg)
        requests.get('http://127.0.0.1:5000/enqueue/'+hostname)
        q.enqueue(hostname)
      else:
        print("init")


        #Thread(target = down(hostname)).start()
  def ifUp(self,item):
    q.deque(item)
    #if item != 0
    #print(item)
    #status =pingagain(item)
    #if status == 1:
    msg = item + " host is up"
    self.sms(msg)
    #else :
    # print("no update")
    #q.enqueue(item)
    #else: 
      # print("emptyque")      
  def sms(self,msg):
    print("____________________________________DOWN DOWN DOWN___________________________________________________"+msg)
    for index in range(len(self.numbers)):
       # Find these values at https://twilio.com/user/account
       account_sid = "AC82216c7d7d8be141a887022ea512f3ab"
       auth_token = "cbbd4c374fee6fe17d1cdada7c2dce3d"
       client = TwilioRestClient(account_sid, auth_token)
       message = client.messages.create(body= msg ,
         to=self.numbers[index],    # Replace with your phone number
         from_="+12012583501") # Replace with your Twilio number
