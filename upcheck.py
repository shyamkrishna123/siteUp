from flask import request
from threading import Thread
import requests
from time import sleep
import threading
import os

def ifUp():
  result = requests.get('http://127.0.0.1:5000/dequeue')

  print(result.text)
  #status =pingagain(item)
  #if status == 1:

   #  msg = item + " host is up"
    # sms(msg)
  #else :
   #  print("no update")
    # requests.get('http://127.0.0.1:5000/enqueue/'+item)

def pingagain(item):

     response = os.system("ping -c 1 " + item)
    # and then check the response...
     if response == 0:
        pingstatus = 1
     else:
        pingstatus = 2
        #dh = open('dhost.py','w+')
        #dh.write(str(hostname))

     return pingstatus
def uprepeat():
   threading.Timer(10.0, uprepeat).start()
   Thread(target = ifUp()).start()

if __name__ == '__main__':
 uprepeat()
