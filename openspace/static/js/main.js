// nothing to see here
// delete these later - DONT TELL ME WHAT TO DO

$(document).ready(function() {

    $(window).on('resize', renderCoverSize);

    renderCoverSize();
});

var signUpButton = document.getElementById('signUpButton');

signUpButton.onclick = function() {
	window.location.href="/signup/";
}

function renderCoverSize() {
    var height = $(window).height();
    $('.cover').css({ height: height - 100 });
}