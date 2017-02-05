import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("epgm://224.0.55.55:1055")
socket.setsockopt(zmq.SUBSCRIBE, "")
#socket.setsockopt(zmq.SUBSCRIBE, 'test')
#socket.setsockopt(zmq.SUBSCRIBE, 'topic_1')
#print "hello"
while True:
 data = socket.recv()
 millis = int(round(time.time() * 1000))
 print millis
 print data
