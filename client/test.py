from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time

# Global constants
HOST = "localhost"
PORT = 3000
ADDR = (HOST, PORT)
BUFSIZ = 512

# Global variables
messages = []
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


def receive_messages():
    """
    receive messages from server
    :return: None
    """
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode()
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("[Exception]", e)
            break

def send_message(msg):
    """
    send messages to the server
    :param msg: str
    :return: None
    """
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()



recieve_thread = Thread(target=receive_messages)
recieve_thread.start()

send_message("joe")
time.sleep(10)
send_message("Hello")
send_message("{quite}")
