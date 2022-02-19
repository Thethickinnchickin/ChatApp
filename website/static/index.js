$(function() {
    $('#sendBtn').bind('click', function() {
        var value = document.getElementById("message").value
        $.getJSON('/send_message',
        {value: value},
        function(data) {

        });
    });
});


window.addEventListener("load", function(){
    var update_loop = setInterval(update, 100);
    update()
});


function update() {
    fetch('/get_messages')
    .then(function (response) {
        return response.json();
    }).then(function (text) {
        console.log(text.messages)

        var content = ''

        for (let i=0; i < text.messages.length; i++) {
            content += '<li class="list-group-item">' + text.messages[i] + '</li>'
        }

        document.getElementById("messages").innerHTML = content;
    })
    return false;
}


function validate(name) {
    if(name.length >= 2) {
        return true;
    }
    return false;
}