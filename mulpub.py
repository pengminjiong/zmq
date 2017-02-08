import zmq
import time
import datetime
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.setsockopt(zmq.LINGER, 0)    # discard unsent messages on close
#socket.connect('epgm://239.192.1.1:5000')
socket.connect("epgm://eth0;224.0.55.55:1055")
while True:
    msg = raw_input('> ')
    if msg == 'quit':
        break
    else:
        millis=datetime.datetime.now()
        #millis = int(round(time.time() * 1000))
        print millis
        socket.send(msg)

socket.close()
