(function() {

    var isOpen = true;

    $(document).ready(function() {
        $('.control-fa').on('click', toggleHeader);
    });


    function toggleHeader() {
        if (isOpen) {
            $('.header-button').animate({ opacity: 0 }, 300, function() {
                $(this).addClass('hide');
                $('.edit-header').animate({ width: 64 }, 300);
            });
            
            isOpen = false;
        } else {
            $('.edit-header').animate({ width: '100%' }, 300);
            $('.header-button').removeClass('hide').animate({ opacity: 1 }, 300);
            isOpen = true;
        }
    }

})();