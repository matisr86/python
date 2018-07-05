$(document).ready(function()
{
	var currentDate = new Date();
	
	$('.progress-bar').each(function()
	{
		var that = $(this);
		var parent = that.parent();
		var startDate = new Date(parent.data('start'));
		var stopDate = new Date(parent.data('stop'));
		var valueMax = daysCounter(startDate, stopDate);
		var valueNow = daysCounter(startDate, currentDate);
		
		if (valueNow >= valueMax)
		{
			valueNow = valueMax;
			that.addClass('progress-bar-danger');
			that.text(completed);
		}
		else
		{
			that.addClass('progress-bar-success');
			that.text(during);
		}
		
		if (valueNow == 0)
			that.text(not_started).css('color', '#666');
		
		that.attr('aria-valuemax', valueMax);
		that.attr('aria-valuenow', valueNow);
		that.css('width', (valueNow / valueMax * 100) + '%');
	});
	
	function daysCounter(firstDate, secondDate)
	{
		var count = Math.floor((secondDate - firstDate) / (1000 * 60 * 60 * 24));
		if (count < 0) count = 0;
		return count;
	}
});
