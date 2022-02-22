class Message:
    """
    Represents a Message, a name that sent it and the time it was sent
    """
    def __init__(self, name, time_sent):
        self.time_sent = time_sent
        self.name = name


    def __repr__(self):
        return f"Message({self.name}, {self.time_sent})"