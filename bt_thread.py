import time
import threading
import Queue
from bt_comm import *

__author__ = 'Rohit'

class BTThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.bt_api = AndroidAPI()
		self.bt_api.connect_bluetooth()

	def writeBT(self, to_bt_q):
		"""
		Invoke write_to_bt()
		"""
		print "Sending text to Andorid: "
		while True:
			if (not to_bt_q.empty()):
				send_bt_msg = to_bt_q.get()
				print "QSIZE: ", to_bt_q.qsize()
				self.bt_api.write_to_bt(send_bt_msg)
				# if len(send_bt_msg) == 0 or send_bt_msg == 'q':
				# 	# Send message in anycase and then quit
				# 	print "quitting..."
				# 	break
				print "Writing to BT: %s" % send_bt_msg
			time.sleep(2)
		
		# print "quit writeBT"
		# return True
		# return send_bt_msg

	# Takes two Qs as arguments and writes (put) value read
	# from BT into them depending on the header
	def readBT(self, to_pc_q): # Include "to_sr_q" in the args
		"""
		Invoke read_from_bt()
		"""
		print "readBT: to_pc_q = %s " %to_pc_q
		while True:
			read_bt_msg = self.bt_api.read_from_bt()
			# if len(read_bt_msg) == 0 or read_bt_msg == 'q':
			# 	print "quitting..."
			# 	break
			
			# Check header for Destination and strip out first char
			if (read_bt_msg[0].lower() == 'p'): # send to PC
				to_pc_q.put(read_bt_msg[1:]) 	# strip header here
				print "testing pc q: Value written = %s " % read_bt_msg[1:]
			
			elif (read_bt_msg[0].lower() == 'h'):	# send to hardware (serial)
				# to_sr_q.put(read_bt_msg[1:]) 	# strip header here
				print "testing serial q: Value written = %s " % read_bt_msg[1:]
			
			else:
				print "Incorrect header received from BT"
			
				# print "Message received from BT: %s. Put in queue" % read_bt_msg[1:]
		
			# print "quit readBT"
			# return True

	def close_all_bt_sockets(self):
		self.bt_api.close_bt_socket()

# if __name__ == "__main__":
# 	print "main"
# 	bt_thread = BTThread()

# 	#Read thread
# 	rt = threading.Thread(target = bt_thread.readBT, name = 'ReadBT')
# 	print "created rt"
# 	#Read thread
# 	wt = threading.Thread(target = bt_thread.writeBT, name = 'Write')
# 	print "created wt"

# 	rt.start()
# 	wt.start()
# 	print "start rt and wt"

# 	rt.join()
# 	wt.join()
# 	print "join rt and wt"
# 	bt_thread.close_all_bt_sockets()
# 	print "End thread"



