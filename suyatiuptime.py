#!/usr/bin/env python
import threading 
from queue import Queue
from threading import Thread
from host import hosts
from collections import defaultdict
import os
from time import sleep
import threading
import ast
from flask import request
from twilio.rest import TwilioRestClient
import requests
numbers = [ '+919746660221' ]
q = Queue()
def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg

  return out 



def hostQue():
  f = open( 'oldhost.py', 'r+' )
  oldhlen = f.read()
  hlen = len(hosts)
  chunk = chunkIt(hosts,5)
  chunkfile = chunk 
  s = open('chunks.py','w+')
  for item in chunkfile:
     s.write("%s\n" % item)
  f = open( 'oldhost.py', 'w+' )
  f.write(str(hlen))
  return chunkfile


def down(hostname):
  response = os.system("ping -c 1 " + hostname)
  if response == 0:
        pingstatus = 1
        print(pingstatus)
        msg = hostname + " host is up"
        sms(msg)
        print("status up")
        return 0
  else:
        pingstatus = 2
        print("status is still  down")
        sleep(120)
        down(hostname)




def hostPing(hostname):
#import dhost
 response = os.system("ping -c 1 " + hostname)
    # and then check the response...
 if response == 0:
        
        pingstatus = 1
        status = q.inqueue(hostname)
        if status is 1:
            print("no init")
        else : 
          ifUp(hostname)
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

          sms(msg)
          #requests.get('http://127.0.0.1:5000/enqueue/'+hostname

          q.enqueue(hostname)
        else:
         print("init")
        
 
        #Thread(target = down(hostname)).start()


    

def sms(msg):
 print("____________________________________DOWN DOWN DOWN___________________________________________________"+msg)
#  for index in range(len(numbers)):
# Find these values at https://twilio.com/user/account
 #    account_sid = "AC82216c7d7d8be141a887022ea512f3ab"
  #   auth_token = "cbbd4c374fee6fe17d1cdada7c2dce3d"
   #  client = TwilioRestClient(account_sid, auth_token)
    # message = client.messages.create(body= msg ,
     #  to=numbers[index],    # Replace with your phone number
      # from_="+12012583501") # Replace with your Twilio number




def ifUp(item):
  q.deque(item)
  #if item != 0
   #print(item)
   #status =pingagain(item)
   #if status == 1:
   
  msg = item + " host is up"
  sms(msg)
   #else :
    # print("no update")
     #q.enqueue(item)
  #else: 
   # print("emptyque")  

def hostQfetch(n):
  data = hostQue()
  print(data)
  for i in xrange(len(data[n])):
     ndata = data[n][i]
     print(ndata)   
     #Thread(target = hostPing(ndata)).start()
     hostPing(ndata)

def repeat():
 threading.Timer(30, repeat).start()
 for i in range(5):
   Thread(target = hostQfetch(i)).start()
   #sleep(30)
    
#def uprepeat():
 #  threading.Timer(10.0, uprepeat).start()
  # Thread(target = ifUp()).start()

if __name__ == '__main__':
 repeat() 
