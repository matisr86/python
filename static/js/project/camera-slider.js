/*========================================
            Slider - Camera
==========================================*/                                
$('#camera_wrap_1').each(function(){
    var t = jQuery(this);
    t.camera({ 
        
        thumbnails: true,
        loader: 'pie',
        fx: 'scrollLeft',
    });
});

/*$('#camera_wrap_4').camera({
    height: 'auto',
    loader: 'bar',
    pagination: false,
    thumbnails: true,
    hover: false,
    opacityOnGrid: false,
            
        });*/
