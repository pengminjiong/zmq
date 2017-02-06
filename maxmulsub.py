import threading
import zmq
import time

context = zmq.Context()

#  Socket to talk to server
def Two_Test():
 
 name = context.socket(zmq.SUB)
 name.connect("epgm://eth0;224.0.55.55:1055")
 name.setsockopt(zmq.SUBSCRIBE, "")
#  Do 10 requests, waiting each time for a response
#for request in range(10):
    #socket.send(b"Hello")
    #  Get the reply.
 
 while True:
   data = name.recv()
   millis = int(round(time.time() * 1000))
   print millis
   print data
for i in range(10):
        name=str(i)
        thread = threading.Thread( target = Two_Test, args = () )
        thread.start()
