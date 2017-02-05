import zmq
import time

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server")
socket = context.socket(zmq.SUB)
socket.connect("tcp://172.17.0.8:5555")
socket.setsockopt(zmq.SUBSCRIBE, "")
#  Do 10 requests, waiting each time for a response
#for request in range(10):
    #socket.send(b"Hello")
    #  Get the reply.
while True:
 data = socket.recv()
 millis = int(round(time.time() * 1000))
 print millis
 print data
