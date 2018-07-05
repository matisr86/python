/*========================================
            Cookies
==========================================*/
if ($.cookie('cookies_politics_accept') != '1') {
    var font = 'Arial';
    var fontSize = 12;
    var padding	= '10px 5px 10px 5px';
    var bgColor	= '#E7E7E7';
    var textColor = '#2d2d2d';
    var labelColor = '#595959';
    var textStyle = 'normal';
    var text = $('#cookie_text p').html();
    var label = $('#cookie_label p').html();
    var buttonText = $('#cookie_button p').html();
    var linkName = '';
    var linkUrl	= '';
    var position = 'bottom';
    var buttonOkBg = '#ff7300';
    var buttonOkColor = '#ffffff';
    var buttonOkShadowColor	= '#ff7300';
    var buttonOkBorderColor	= '2px solid #ff7300';
    var buttonOkBorderRadius	= '10px';
    var opacity = 0.9;
    var borderColor	= '#d0cfcf';
    var opacityIe = opacity*100;
    var border = position == 'bottom'?'top':'bottom';
    
    if(position == 'top')
    {
        position = 'top:0px;';
    }
    else {
        position = 'bottom:0px;';
    }

$('#cookies').append(
'<div id="cookies-politics" style="line-height:18px;font-family:'+font+';font-size:'+fontSize+'px;width:100%;background: '+bgColor+';opacity:'+opacity+';filter: alpha(opacity = '+opacityIe+'); border-'+border+': 1px solid '+borderColor+'; color: '+textColor+'; font-weight: '+textStyle+'; z-index: 10000; text-align: left; position: fixed;'+position+'left:0px; padding:'+padding+';">'
    +'<div id="cookies-inside" style="max-width:960px;margin:0px auto;position:relative;">'
        +'<div id="cookies-inside-left" style="width:75%;float:left;margin-right:5%;">'+text+'<br />'+label
            +'<a href="'+linkUrl+'" target="_blank" style="color:'+textColor+';text-decoration:underline;">'+linkName+'</a>'
        +'</div>'
        +'<div id="cookies-inside-right" style="width:20%;float:left;">'
            +'<a href="" onclick="return false" style="border:'+buttonOkBorderColor+';border-radius:'+buttonOkBorderRadius+';display:block;text-align:center;text-shadow: 0 1px 1px '+buttonOkShadowColor+';text-decoration:none;padding:5px;padding-left:10px;padding-right:10px;color:'+buttonOkColor+';background:'+buttonOkBg+';" id="cookies-politics-accept">'+buttonText+'</a>'
        +'</div>'
    +'</div>'
+'</div>'
)
}

$( "#cookies-politics-accept" ).click(function() {
    $('#cookies').fadeOut(2000);
    $.cookie('cookies_politics_accept', '1', { expires: 356, path: '/'});
}); 
