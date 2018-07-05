var apply = $('#apply');
var that = $("ul.list-unstyled.toggle");
var icon = that.find('i.fa');
setTimeout(function() {
    apply.animate({bottom: 0}, 1000);
    icon.removeClass('fa-arrow-circle-up');
    icon.addClass('fa-arrow-circle-down');
    showApply = true;
}, 1000);

