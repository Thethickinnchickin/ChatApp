from flask import Flask, render_template, url_for, session, redirect, request, jsonify
from client import Client
import time
from threading import Thread

NAME_KEY = 'name'
client = None
messages = []

app = Flask(__name__)
app.secret_key = "helloyoucannotguessthesecret"


def disconnect():
    """
    call this before the client disconnects
    :return:
    """


@app.route("/login", methods=["POST", "GET"])
def login():
    """
    displays main login page and handles saying name in session
    :return: None
    """
    if request.method == "POST":
        global client

        session[NAME_KEY] = request.form["name"]

        client = Client(session[NAME_KEY])

        return redirect(url_for("home"))

    return render_template("login.html", **{"session": "session"})


@app.route("/logout")
def logout():
    """
    logs user out by popping name from session
    :return None
    """
    global client

    client.disconnect()

    session.pop(NAME_KEY, None)
    return redirect(url_for("login"))


@app.route("/")
@app.route("/home")
def home():
    """
    displays home page if logged in
    :return: None
    """
    global client

    if NAME_KEY not in session:
        print("hello")
        return redirect(url_for("login"))

    client = Client(session[NAME_KEY])

    return render_template("index.html", **{"login": True, "session": session})


@app.route("/send_message")
def run():
    """
    called from jQuery to send messages
    :return:
    """
    global client

    message = request.values['value']
    if client != None:
        client.send_message(message)
        update_messages()

    return "none"


@app.route("/get_messages")
def get_messages():
    update_messages()
    return jsonify({"messages": messages})

@app.route("/get_name")
def get_name():
    try:
        name = client.get_name()
        return jsonify({"name": name})
    except Exception as e:
        print(e)

def update_messages():
    """
    updates local list of messages
    :return:
    """
    global messages

    run = True
    while run:
        time.sleep(0.1)  # update every 1/10 of a second
        if not client: continue
        new_messages = client.get_messages()  # get any new messages from client
        for msg in new_messages:  # display new messages
            messages.append(msg)
            if msg == '{quit}':
                run = False
                break
        return messages


if __name__ == "__main__":
    app.run(debug=True)
