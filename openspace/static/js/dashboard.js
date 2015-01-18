$(document).ready(function() {

    $(window).on('resize', renderCoverSize);

    renderCoverSize();
});

function renderCoverSize() {
    var height = $(window).height();
    $('.cover').css({ height: height - 100 });
}