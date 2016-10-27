from flask import Flask
from uptimemain import uptimeMain
from uptimecheck import uptimecheck
from host import hosts
from queue import Queue
from flask import request
from threading import Thread
import requests
from time import sleep
import threading
import os
from suyatiuptime import sms
import pickle
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
app = Flask(__name__)


@app.route('/insert/<host>')
def insert(host):
    hostlistfile = 'hostlist.data'
    f= open(hostlistfile,'rb')
    hostlist = pickle.load(f)
    hostlist.append(host)
    f.close
    f= open(hostlistfile,'wb')
    pickle.dump(hostlist, f)
    f.close
    hosts = hostlist
    del hostlist
    return format(str(hosts))


@app.route("/")
def hello():
    return "The queue has {0} packets!".format(str(10))

@app.route('/enqueue/<machine>')
def enqueue(machine):
    app.queue1.enqueue(machine)
    return "New ip address added to queue {0}".format(machine)


@app.route('/inqueue/<machine>')
def inqueue(machine):
  print(machine)
  mac = str(machine)
  app.queue1.inqueue(mac)

@app.route('/dequeue')
def dequeue():
    return app.queue1.dequeue()
  #else :
   # return "empty"
    
@app.route('/lqueue')
def lqueue():
    items = app.queue1.lqueue()
    return format(str(items))


@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
@app.route('/start')
def start():
  main = uptimeMain()
  Thread(target = main.repeat()).start()
  pass
  return 'done'
if __name__ == "__main__":
   uptm = uptimecheck()
   main = uptimeMain()
   app.queue1 = Queue()
   Thread(target = app.run()).start() 
