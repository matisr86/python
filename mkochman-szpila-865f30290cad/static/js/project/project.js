$(document).ready (function ()
{	
    
	$(".phone").each(function() {
		var phone = $(this).html().split(' ').join('');
		if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
			$(this).attr("href", "tel:"+phone+"")
		}
		//~ else {
			//~ $(this).attr("href", "callon:"+phone+"")
		//~ }
	});

	/*========================================
	Bugfix parallax scrolling in iPhone and iPad
	==========================================*/
	if (navigator.userAgent.match(/iPhone/i) || navigator.userAgent.match(/iPad/i) || navigator.userAgent.match(/iPod/i))
	{
		$('.header').css('background-attachment', 'scroll');
	}

	/* Navigate by href */
	var temp = '';
	$('a[href*=#]:not([href=#]):not([href=#carousel])').click(function()
	{
		//~ if (temp == '')
		//~ {
			//~ $(this).parent().find('.triangle').css({display:'block'});
			//~ temp = $(this).parent();
		//~ }
		//~ else
		//~ {
			//~ temp.find('.triangle').css({display:'none'});
			//~ $(this).parent().find('.triangle').css({display:'block'});
			//~ temp = $(this).parent();
		//~ }
		
		if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') || location.hostname == this.hostname)
		{
			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
			if (target.length)
			{
				$('html,body').animate({
					scrollTop: target.offset().top - 90
				}, 1000);
				return false;
			}
		}
	});
});
$(document).on("scroll", onScroll);

function onScroll(event){
    var scrollPos = $(document).scrollTop() + 95;
    $('#nav a').each(function () {
        var currLink = $(this);
        var refElement = $(currLink.attr("href"));
        if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
            $('#nav ul li a').parent().find('.triangle').css({display:'none'});
            currLink.parent().find('.triangle').css({display:'block'});
        }
        else{
            currLink.parent().find('.triangle').css({display:'none'});
        }
    });
}
