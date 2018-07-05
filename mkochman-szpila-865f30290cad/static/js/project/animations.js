$(document).ready (function ()
{	
    /*========================================
                Animations (func, init)
    ==========================================*/  

            /*More or less text*/
    $(".show-more").append('<a href="#" class="c-orange">'+$('#more p').html()+'</a>');
    $(".show-more a").on("click", function() {
        var $link = $(this);
        var $content = $link.parent().prev("div.text-content");
        var linkText = $link.text();
        
        switchClasses($content);

        $link.text(getShowLinkText(linkText));
        
        return false;
    });
});

function switchClasses($content){
	if($content.hasClass("short-text")){  
		$content.switchClass("short-text", "full-text", 600);
	} else {
		$content.switchClass("full-text", "short-text", 600);
	}
    }

function getShowLinkText(currentText){
	var newText = '';
	if (currentText.toUpperCase() === "WIĘCEJ" || currentText.toUpperCase() === "MORE") {
        newText = $('#less p').html();
    } else {
        newText = $('#more p').html();
    }
    
	return newText;
}
