
function CustomFileBrowser(field_name, url, type, win) {
    tinyMCE.activeEditor.windowManager.open({
        file: window.__filebrowser_url + '?pop=2&type=' + type,
        width: 820,  // Your dimensions may differ - toy around with them!
        height: 500,
        resizable: "yes",
        scrollbars: "yes",
        inline: "yes",  // This parameter only has an effect if you use the inlinepopups plugin!
        close_previous: "no"
    }, {
        window: win,
        input: field_name,
        editor_id: tinyMCE.selectedInstance.editorId
    });
    return false;
}

jQuery(function($) {

    if (typeof tinyMCE != 'undefined') {

        tinyMCE.init({
            // main settings
            mode : "specific_textareas",
            editor_selector : "mceEditor",
            theme: "advanced",
            language: "en",
            dialog_type: "window",
            editor_deselector : "mceNoEditor",
            skin: "thebigreason",

            // general settings
            width: '500px',
            height: '300px',
            indentation : '10px',
            fix_list_elements : true,
            remove_script_host : true,
            accessibility_warnings : false,
            object_resizing: false,
            //cleanup: false, // SETTING THIS TO FALSE WILL BREAK EMBEDDING YOUTUBE VIDEOS
            forced_root_block: "p",
            remove_trailing_nbsp: true,
            
            external_link_list_url: '/displayable_links.js',
            relative_urls: false,
            convert_urls: false,

            // callbackss
            file_browser_callback: "CustomFileBrowser",

            // theme_advanced
            theme_advanced_toolbar_location: "top",
            theme_advanced_toolbar_align: "left",
            theme_advanced_statusbar_location: "bottom",
            theme_advanced_buttons1: "bold,italic, underline,strikethrough,|,bullist,numlist,blockquote,|,undo,redo,search,replace,|,justifyleft,justifycenter,justifyright,justifyfull,|,fullscreen,|,phone,",
            theme_advanced_buttons2: "fontsizeselect,formatselect,styleselect,customformat,|,link,unlink,|,image,|,media,charmap,|,code,|,table,bootstrap_col_6,bootstrap_col_12,new_line,mylistbox,",
            theme_advanced_buttons3: "",
            theme_advanced_path: true,
            theme_advanced_blockformats: "p,h1,h2,h3,h4,pre",
            theme_advanced_text_colors : "",
            theme_advanced_font_sizes :  "6px=.s1,8px=.s2,10px=.s3,12px=.s4,14px=.s5,16px=.s6,18px=.s7,20px=.s8,22px=.s9,24px=.s10,26px=.s11,,28px=.s12,30px=.s13,70px=.s14,90px=.s15",
            theme_advanced_styles: "[all] clearfix=clearfix;[p] small=small;[img] Image left-aligned=img_left;[img] Image left-aligned (nospace)=img_left_nospacetop;[img] Image right-aligned=img_right;[img] Image right-aligned (nospace)=img_right_nospacetop;[img] Image Block=img_block;[img] Image Block (nospace)=img_block_nospacetop;[div] column span-2=column span-2;[div] column span-4=column span-4;[div] column span-8=column span-8",
            theme_advanced_resizing : true,
            theme_advanced_resize_horizontal : false,
            theme_advanced_resizing_use_cookie : true,
            theme_advanced_styles: "Image left-aligned=img_left;Image left-aligned (nospace)=img_left_nospacetop;Image right-aligned=img_right;Image right-aligned (nospace)=img_right_nospacetop;Image Block=img_block",
            advlink_styles: "intern=internal;extern=external",
            
            // Style formats
            style_formats : [
                {title : 'Default Color', inline : 'span', classes : 'default_color', styles : {color : '#6d6d6d'}},
                {title : 'White', inline : 'span', classes : 'white', styles : {color : '#000000'}},
                {title : 'Orange', inline : 'span', classes : 'orange', styles : {color : '#ff7300'}},
                {title : 'Silver', inline : 'span', classes : 'silver', styles : {color : '#C0C0C0'}},
                {title : 'Gray', inline : 'span', classes : 'gray', styles : {color : '#808080'}},
                {title : 'Red', inline : 'span', classes : 'red', styles : {color : '#FF0000'}},
                {title : 'Lime', inline : 'span', classes : 'lime', styles : {color : '#00FF00'}},
                {title : 'Blue', inline : 'span', classes : 'blue', styles : {color : '##0000FF'}},
                {title : 'Green', inline : 'span', classes : 'green', styles : {color : '#008000'}},
                {title : 'Aqua', inline : 'span', classes : 'aqua', styles : {color : '#00FFFF'}},
                {title : 'Black', inline : 'span', classes : 'black', styles : {color : '#FFFFFF'}},
                {title : 'Fuschia', inline : 'span', classes : 'fuschia', styles : {color : '#FF00FF'}},
                {title : 'Yellow', inline : 'span', classes : 'yellow', styles : {color : '#FFFF00'}},
                {title : 'Maroon', inline : 'span', classes : 'maroon', styles : {color : '#800000'}},
            ],

            formats : {
                    alignleft : {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'left'},
                    aligncenter : {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'center'},
                    alignright : {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'right'},
                    alignfull : {selector : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', classes : 'full'},
                    bold : {inline : 'span', 'classes' : 'bold'},
                    italic : {inline : 'span', 'classes' : 'italic'},
                    underline : {inline : 'span', 'classes' : 'underline', exact : true},
                    strikethrough : {inline : 'del'},
            },
            
            setup : function(ed) {
                ed.addButton('bootstrap_col_6', {
                    title : 'Insert half page Bootstrap column',
                    image : '/static/img/tinymce/columns.png',
                    onclick : function() {
                        ed.focus();
                        if(ed.selection.getNode().className != 'col-sm-6 col-md-6'){
                            ed.selection.setContent('<div class="col-sm-6 col-md-6 tiny-border">'+ed.selection.getContent()+'</div>');
                        }
                    }
                });
                ed.addButton('bootstrap_col_12', {
                    title : 'Insert full page Bootstrap column',
                    image : '/static/img/tinymce/column.png',
                    onclick : function() {
                        ed.focus();
                        ed.dom.removeClass(ed.dom.select('div'), 'col-sm-6');
                        ed.dom.removeClass(ed.dom.select('div'), 'col-md-6');
                        ed.dom.removeClass(ed.dom.select('div'), 'tiny-border');
                    }
                });
                ed.addButton('new_line', {
                    title : 'Insert empty line',
                    image : '/static/img/tinymce/new_line.png',
                    onclick : function() {
                        ed.focus();
                        if(ed.selection.getNode().className != 'new_line'){
                            ed.selection.setContent('<br>'+ed.selection.getContent());
                        }
                    }
                });
                ed.addButton('phone', {
                    title : 'Insert mobile phone call',
                    image : '/static/img/tinymce/phone.png',
                    onclick : function() {
                        ed.focus();
                        if(ed.selection.getNode().className != 'phone'){
							var phone = ed.selection.getContent().split(' ').join('-');
                            ed.selection.setContent('<a class="phone">'+ed.selection.getContent()+'</a>');
                        }
                    }
                });
            },

            // plugins
            plugins: "inlinepopups,contextmenu,tabfocus,searchreplace,fullscreen,advimage,advlink,paste,media,table,",
            advimage_update_dimensions_onchange: true,

            // remove MS Word's inline styles when copying and pasting.
            paste_remove_spans: true,
            paste_auto_cleanup_on_paste : true,
            paste_remove_styles: true,
            paste_remove_styles_if_webkit: true,
            paste_strip_class_attributes: true,
            

            // don't strip anything since this is handled by bleach
            valid_elements: "+*[*]",
            valid_children: "+button[a]",
            //~ extended_valid_elements : "a[class|name|href|target|title|onclick],img[style|class|src|border=0|alt|title|hspace|vspace|width|height|align|onmouseover|onmouseout|name],hr[class|width|size|noshade],font[face|size|color|style],span[class|align|style]",
            //~ plugins : "fullpage",
            //~ content_css: window.__tinymce_css,
            content_css : "/static/css/project/content.css",
            


    	});

    }

});
