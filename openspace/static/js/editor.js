(function() {

    $(document).ready(function() {
        renderContainer();

        $(window).on('resize', renderContainer);
        $('.page_picker').on('change', renderPage);
    });

    function renderContainer() {
        var winHeight = $(window).height(),
            winWidth = $(window).width();

        $('.content').css({
            height: winHeight - 64,
            width: winWidth
        });
    }

    function renderPage() {
        var picker = $('.page_picker');

        if (picker.val() != 'default') {
            
            window.location.replace('/editor/?page_id=' + picker.val());
        }
    }

})();