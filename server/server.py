from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from chatuser import ChatUser

# Global constants
HOST = 'localhost'
PORT = 3000
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
BUFSIZ = 1024

# Global Variables
chat_users = []
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def broadcast(msg, name):
    """
    Send new message to all clients
    :param msg: bytes["utf8"]
    :param name: str
    :return:
    """
    for chat_user in chat_users:
        client = chat_user.client
        try:
            client.send(bytes(name, "utf8") + msg)
        except Exception as e:
            print("[Exception]", e)


def client_communication(chat_user):
    """
    Thread to handle all messages from client
    :param chat_user: ChatUser
    :return: None
    """
    client = chat_user.client
    # getting users name
    name = client.recv(BUFSIZ).decode("utf8")
    chat_user.set_name(name)

    msg = bytes(f"{name} has joined the chat", "utf8")
    broadcast(msg, "")
    run = True
    while run:
        try:
            message = client.recv(BUFSIZ)
            if message == bytes("{quite}", "utf8"):
                client.close()
                chat_users.remove(chat_user)
                broadcast(bytes(f"{name} has left the chat...", "utf8"), "")
                print(f"[DISCONNECTED] {name} disconnected")
                break
            else:
                broadcast(message, name+": ")
        except Exception as e:
            print(f"[Exception]", e)
            break


def wait_for_connection():
    """
    Wait for connection from new clients, start new thread once connected
    :param
    :return: none
    """
    run = True
    while run:
        try:
            client, address = SERVER.accept()
            chat_user = ChatUser(address, client)
            chat_users.append(chat_user)
            print(f"[Connection] {address} connected to sever at {time.time()}")
            Thread(target=client_communication, args=(chat_user,)).start()
        except Exception as e:
            print("[Exception]", e)
            break


if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS)  # listening for connection
    print("[Started] Waiting for server connection")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()