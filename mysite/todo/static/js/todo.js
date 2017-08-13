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
                                <div class=\"col-sm align-middle\" style=\"background-color: #f0f0f0; height: 50px;\"><input type=\"checkbox\" id=" + title + "></div>\
                            </div>\
                        </div>";
                $(html).insertAfter($('[name="to-do-container"]').last());
            }
        });
    });
 }


function checkTodo() {
     $('#check_btn').click(function() { 
        titlesValues = $("input[name='undone']:checkbox:checked").map(function(){
            return $(this).attr('id');
        }).get();

        alert(titlesValues.length); //$("input[name='undone']:checkbox:checked").length);

        alert($("[name='csrfmiddlewaretoken']").val());

        $.ajax({
            //url: "",
            method: 'PUT', // or another (GET), whatever you need
            data: {
                titles: titlesValues, // data you need to pass to your function
                //csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
                check: true
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
                $(html).insertAfter($('[name="to-do-container"]').last());
            }
        });
    });
 }


