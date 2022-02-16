import time
from client import Client
from threading import Thread

c1 = Client("John")
c2 = Client("Bill")


def update_messages():
    msgs = []
    run = True
    while run:
        time.sleep(0.1) # update every 1/10 of a second
        new_messages = c1.get_messages() # get any new messages from client
        msgs.extend(new_messages) # adding to local list of messages
        for msg in new_messages: # display new messages
            print(msg)
            if msg == '{quit}':
                run = False
                break


Thread(target=update_messages).start()

c2.send_message("hello")
time.sleep(5)
c1.send_message("whats up")
time.sleep(5)
c2.send_message("nothing much, hbu")
time.sleep(5)
c1.send_message("Boring")
time.sleep(5)
c1.disconnect()
time.sleep(5)
c2.disconnect()
