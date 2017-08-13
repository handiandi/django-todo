 //Add ned to-do 
 $( document ).ready(
    function() {
        addTodo();
    });


$( document ).ready(
    function() {
        checkTodo();
    });


 function addTodo() {
     $('#add_btn').click(function() {    
        $.ajax({
            //url: "",
            method: 'POST', // or another (GET), whatever you need
            data: {
                title: $('#title').val(), // data you need to pass to your function
                description: $('#descr').val(),
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
                add: true
            },
            dataType: "json",
            success: function (data) { 
                title = data[0].fields.title;
                descr = data[0].fields.description;
                html = " <div class=\"container\" name=\"to-do-container\">\
                            <div class=\"row align-middle\">\
                                <div class=\"col-sm align-middle\" style=\"background-color: #f0f0f0; height: 50px;\">" + title + "</div>\
                                <div class=\"col-sm align-middle\" style=\"background-color: #f0f0f0; height: 50px;\">" + descr + "</div>\
                                <div class=\"col-sm align-middle\" style=\"background-color: #f0f0f0; height: 50px;\"><input type=\"checkbox\" id=" + title + " name=\"undone\"></div>\
                            </div>\
                        </div>";
                //$(html).insertAfter($('[name="to-do-container"]').last());
                $('[name="p no todos"]' ).remove();
                $(html).appendTo($('[name="undone-to-do-container"]'));
            }
        });
    });
 }


function checkTodo() {
     $('#check_btn').click(function() { 
        titlesValues = $("input[name='undone']:checkbox:checked").map(function(){
            return $(this).attr('id');
        }).get();
        csrftoken = Cookies.get('csrftoken');
        $.ajax({
            //url: "",
            method: 'POST', // or another (GET), whatever you need
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            data: {
                titles: titlesValues, // data you need to pass to your function
                check: true
            },

            //dataType: "json",
            success: function (data) {
                location.reload(); 
            }
        });
    });
 }


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}