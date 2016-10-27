from chunkfile import chunkfile
from threading import Thread
import threading
from uptimecheck import uptimecheck
from time import sleep
class uptimeMain:
	def __init__(self):
		chunks = chunkfile()
		self.data = chunks.hostQue()
                self.uptm = uptimecheck()
	def hostQfetch(self,n,data):
  		print("\n\n",data)
		print(n,data[n])
		for i in xrange(len(data[n])):
			ndata = data[n][i]
			print(ndata)   
      #Thread(target = hostPing(ndata)).start()
 			self.uptm.hostPing(ndata)
	def repeat(self):
		threading.Timer(30, self.repeat).start()
		for i in range(5):
			Thread(target = self.hostQfetch(i,self.data)).start()

    #sleep(30)
    
#def uprepeat():
 #  threading.Timer(10.0, uprepeat).start()
  # Thread(target = ifUp()).start()

#if __name__ == '__main__'
#	uptm = uptimecheck()
#	main = uptimeMain()
#	main.repeat()		
    #sleep(30)
    
