jQuery(function($) {
    
    /* 
     * Overwriting of js editable from core
    */
    
    /* Uncomment to start edit */
    $(window.__toolbar_html).appendTo('body');
    var links = $('.editable-link');

    $.each($('.editable-original'), function(i, editable) {
        editable = $(editable);
        var link = editable.next('.editable-link');
        link.offset({
            top: editable.offset().top,
            left: editable.offset().left - link.outerWidth() - 5
            
            //top: editable.offset().top + link.outerWidth(),
            //left: editable.offset().left
            
        }).overlay({
            expose: {color: '#333', loadSpeed: 200, opacity: 0.9},
            closeOnClick: true, close: ':button',
            left: 'center', top: 'center'
        });
        link.next('.editable-highlight').css({
            width: editable.width(),
            height: editable.height()
        }).offset({
            top: editable.offset().top, left: editable.offset().left
        });
    });

    links.hover(function(e) {
        //$(this).next('.editable-highlight').css('visibility', 'visible');
        $(this).next('.editable-highlight').css('visibility', 'hidden');
    }, function(e) {
        $(this).next('.editable-highlight').css('visibility', 'hidden');
    });
    /**/

});
