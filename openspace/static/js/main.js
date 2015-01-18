// nothing to see here
// delete these later - DONT TELL ME WHAT TO DO

$(document).ready(function() {

    $(window).on('resize', renderCoverSize);

    renderCoverSize();
});

function goToSignUp() {
	window.location.href="/signup/";
}

function goToDashboard() {
	window.location.href="/dashboard/";
}

function renderCoverSize() {
    var height = $(window).height();
    $('.cover').css({ height: height - 100 });
}