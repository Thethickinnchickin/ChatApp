$(function() {
    $('a#test').bind('click', function() {
        $.getJSON('/run',
            function(data) {
                console.log("hello")
            });
            return false;
    });
});

function validate(name) {
    if(name.length >= 2) {
        return true;
    }
    return false;
}