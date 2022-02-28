var dt = new Date();
var hours = ((dt.getHours() + 11) % 12 + 1);
var time = hours + ":" + dt.getMinutes()


$(function() {
    $('#sendBtn').bind('click', function() {
        var value = document.getElementById("message-area").value
        $.getJSON('/send_message',
        {value: value},
        function(data) {

        });

    $('#message-area').val('');
    });
});


window.addEventListener("load", function(){
    var update_loop = setInterval(update, 100);
    update()
});


async function update() {
    var client_name = await load_name();
    var message_content = ''
    var user_content = ''
    var users = await load_users();



    fetch('/get_messages')
    .then(function (response) {
        return response.json();
    }).then(function (text) {

        for (let value of text["messages"]) {
            console.log(value)
            if (value.name != client_name) {
                message_content += '<li class="you"><div class="entete"><span class="status green"></span><h2>'+ value.name +'</h2><h3></h3></div><div class="triangle"></div><div class="message">' + value.message + '</div></li>'
            } else {
                message_content += '<li class="me"><div class="entete"><h3></h3><h2>'+ value.name +'</h2><span class="status blue"></span></div><div class="triangle"></div><div class="message">' + value.message + '</div></li>'
            }
        }

        document.getElementById("chat").innerHTML = message_content;

    })





    for (let user of users) {
        console.log(user)
         user_content += '<li><img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/1940306/chat_avatar_01.jpg" alt=""><div><h2>'+ user +'</h2><h3><span class="status orange"></span>online</h3></div></li>'
    }
    document.getElementById("users-online").innerHTML = user_content;
    return false;
}

async function load_name() {
  return await fetch("/get_name")
    .then(async function (response) {
      return await response.json();
    })
    .then(function (text) {
      return text["name"];
    });
}

async function load_users() {
    return fetch("/get_users")
        .then(async function (response) {
            return await response.json();
        })
        .then(function (text) {
            console.log(text)
            return text[1]
        })
}



function validate(name) {
    if(name.length >= 2) {
        return true;
    }
    return false;
}