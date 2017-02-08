import threading
import zmq
import time

context = zmq.Context()
n=2
m=10
#  Socket to talk to server
def Two_Test():
 
 name = context.socket(zmq.SUB)
 name.connect("tcp://172.17.0.2:5555")
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
for i in range(20):
        name=str(i)
        thread = threading.Thread( target = Two_Test, args = () )
        thread.start()
