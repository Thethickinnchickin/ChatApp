$(function() {
    $('#sendBtn').bind('click', function() {
        var value = document.getElementById("message").value
        $.getJSON('/send_message',
        {value: value},
        function(data) {

        });

        fetch('/get_messages')
        .then(function (response) {
            return response.text();
        }).then(function (text) {
            console.log(text);
        })
        return false;
    });
});


function validate(name) {
    if(name.length >= 2) {
        return true;
    }
    return false;
}