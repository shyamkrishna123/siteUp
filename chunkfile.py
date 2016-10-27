import pickle
class chunkfile():
	"""docstring for chunkfile"""
	def __init__(self):
		hostlistfile = 'hostlist.data'
		self.chunkfile = []
		f = open(hostlistfile, 'rb')
# Load the object from the file
		self.hosts = pickle.load(f)
	def chunkIt(self, num):
		avg = len(self.hosts) / float(num)
		out = []
		last = 0.0
		while last < len(self.hosts):
			out.append(self.hosts[int(last):int(last + avg)])
			last += avg
		return out
	def hostQue(self):
		chunk = self.chunkIt(5)
		self.chunkfile = chunk
		return self.chunkfile
