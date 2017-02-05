import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://172.17.0.8:5555")

while True:
    msg = raw_input('> ')
    if msg == 'quit':
        break
    else:
        millis = int(round(time.time() * 1000))
        print millis
        socket.send(msg)

socket.close()
