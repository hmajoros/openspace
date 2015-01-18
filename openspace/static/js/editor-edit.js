(function() {

    var isOpen = true;

    $(document).ready(function() {
        $('.control-fa').on('click', toggleHeader);
        
        $('#save').bind('click', saveToDB);
        $('#preview').bind('click', previewPage);
        $('#change').bind('click', changePage);
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

    function saveToDB() {
        var css = $('template_css').text(),
            js = $('template_js').text(),
            html = $('template_html').text();

        $.ajax({
            type: 'POST',
            url: '/editor/save',
            data: {
                html: html,
                css: css,
                js: js,
                page_id: QueryString().page_id
            }
        });
    }

    function previewPage() {
        console.warn(QueryString().page_id);
    }

    function changePage() {
        console.warn('change page');
    }

    // HAIL SATAN
    function QueryString() {
      // This function is anonymous, is executed immediately and 
      // the return value is assigned to QueryString!
      var query_string = {};
      var query = window.location.search.substring(1);
      var vars = query.split("&");
      for (var i=0;i<vars.length;i++) {
        var pair = vars[i].split("=");
            // If first entry with this name
        if (typeof query_string[pair[0]] === "undefined") {
          query_string[pair[0]] = pair[1];
            // If second entry with this name
        } else if (typeof query_string[pair[0]] === "string") {
          var arr = [ query_string[pair[0]], pair[1] ];
          query_string[pair[0]] = arr;
            // If third or later entry with this name
        } else {
          query_string[pair[0]].push(pair[1]);
        }
      } 
        return query_string;
    }

})();