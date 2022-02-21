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


function update() {
    var client_name = ''
    var message_content = ''



    fetch('/get_name')
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        console.log(text.name)
        client_name = text.name
    })

    fetch('/get_messages')
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        console.log(text.messages)

        console.log("Hello")

        for (let value of text["messages"]) {

            message_content += '<li class="you"><div class="entete"><span class="status green"></span><h2>' + client_name + '</h2><h3> '+ time +'</h3></div><div class="triangle"></div><div class="message">' + value + '</div></li>'
        }
        document.getElementById("chat").innerHTML = message_content;
    })

    return false;
}


function validate(name) {
    if(name.length >= 2) {
        return true;
    }
    return false;
}