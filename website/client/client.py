import threading
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time


class Client:
    """
    for communication with server
    """
    # Global constants
    HOST = "localhost"
    PORT = 4000
    ADDR = (HOST, PORT)
    BUFSIZ = 512

    def __init__(self, name):
        """
        Init object and send name to server
        :param name: str


        """
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages = []
        self.send_message(name)
        self.lock = threading.Lock()
        receive_thread = Thread(target=self.receive_messages)
        receive_thread.start()

    def receive_messages(self):
        """
        receive messages from server
        :return: None
        """
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZ).decode()
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
            except Exception as e:
                print("[Exception]", e)
                break

    def send_message(self, msg):
        """
        send messages to the server
        :param msg: str
        :return: None
        """
        self.client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            self.client_socket.close()

    def get_messages(self):
        """
        :returns a list of str messages
        :return: list[str]
        """
        # make sure memory is safe to access

        messages_copy = self.messages[:]

        # make memory safe to read
        self.lock.acquire()
        self.messages = []
        self.lock.release()
        return messages_copy

    def disconnect(self):
        self.send_message("{quit}")
