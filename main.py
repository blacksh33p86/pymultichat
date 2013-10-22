import threading
import Queue


class printer(threading.Thread):
	printer= ""
	

	def __init__(self, job,answer): 
		threading.Thread.__init__(self) 
		self.printer = job
		self.answer = answer
		self.alive = threading.Event()
		self.alive.set()
 
	def run(self): 
		while self.alive.isSet():
			try:
                # Queue.get with timeout to allow checking self.alive
				cmd = self.printer.get(True, 0.1)
				print(cmd)
				if cmd=="exit":
					self.alive.clear()
			except Queue.Empty as e:
				continue
		self.answer.put("Thread exiting")

q = Queue.Queue()
a = Queue.Queue()

t = printer(q,a).start()

input =""

while input !="exit":
	input = raw_input("cmd: ");
	q.put(input)
print a.get()