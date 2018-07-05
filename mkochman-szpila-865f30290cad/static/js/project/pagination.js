$(document).ready(function()
{
    var news = $("#news");
    var articles = $("#articles");

    /* News pagination */
    $('#news-paginator').bootpag(
    {
        total: Math.ceil(news.children().length / 2),
        maxVisible: 8
    }).on("page", function(event, num)
    {
        var first = news.children().eq((num*2)-2);
        news.children().hide();
        first.show().next().show();
    });

    /* Articles pagination */
    $('#articles-paginator').bootpag(
    {
        total: Math.ceil(articles.children().length / 4),
        maxVisible: 4
    }).on("page", function(event, num)
    {
        var first = articles.children().eq((num*4)-4);
        articles.children().hide();
        first.show().next().show().next().show().next().show();
    });   
});
