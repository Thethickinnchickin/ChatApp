class ChatUser:
    """
    Represents a Chat User, has name, socket client, and IP address
    """
    def __init__(self, addr, client):
        self.addr = addr
        self.client = client
        self.name = None

    def set_name(self, name):
        self.name = name

    def __repr__(self):
        return f"ChatUser({self.addr}, {self.name})"



