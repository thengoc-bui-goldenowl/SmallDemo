//Load Form Project

$(".createProject").click(function() {
    $.ajax({
        url: "form/create/project/",
        success: function(result) {
            $("#createForm").html(result);
            createFormButton();
            validFormProject();
            $("#id_start_date, #id_end_date").datepicker({
                dateFormat: 'yy-mm-dd'
            });

            createProjectSubmit();
        }
    });
});




// Load Form Dev
$(".createDev").click(function() {
    $.ajax({
        url: "form/create/dev/",
        success: function(result) {
            $("#createForm").html(result);
            createFormButton()
            validFormDev()
            $('#id_active').click(function() {
                document.getElementById('id_project').disabled = !this.checked;
            })
            createDevSubmit()
        }
    });

});


// Show Form
function createFormButton() {
    $("#popupForm").show();
    $(".cancel").click(function() {
        $("#popupForm").hide()
    })
}


//Submit form

function createDevSubmit() {
    $('#createDevForm').submit(function(e) {
        e.preventDefault();
        if (!$(this).valid()) return false;
        $(".createDevSubmit").attr("disabled", "disabled");
        var first_name = $('#id_first_name').val();
        var last_name = $('#id_last_name').val();
        var active = $('#id_active').prop('checked');
        var project = $('#id_project').val();
        var language = $('#id_language').val();
        console.log(active)
        $.ajax({
            url: "form/create/dev/",
            type: "POST",
            data: {
                first_name: first_name,
                last_name: last_name,
                active: active,
                project: project,
                language: language,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },

            cache: false,
            success: function(dataResult) {
                if (dataResult.statusCode == 200) {
                    $(".createDevSubmit").removeAttr("disabled");
                    $("#success").show();
                    $('#success').html('New Dev Added');
                    $("#popupForm").hide();
                    setTimeout(function() {
                        $("#success").hide();
                    }, 2000);
                } else {
                    $("#error").show();
                    $('#error').html('ERROR!');
                    setTimeout(function() {
                        $("#error").hide();
                    }, 2000);
                }

            }
        });

    });


}


//Submit Form Project

function createProjectSubmit() {
    $('#createProjectForm').submit(function(e) {
        e.preventDefault();
        if (!$(this).valid()) return false;
        $(".createProjectSubmit").attr("disabled", "disabled");
        var name = $('#id_name').val();
        var des = $('#id_des').val();
        var start_date = $('#id_start_date').val();
        var end_date = $('#id_end_date').val();
        var cost = $('#id_cost').val();
        var dev = $('#id_dev').val();

        $.ajax({
            url: "form/create/project/",
            type: "POST",
            data: {
                name: name,
                des: des,
                start_date: start_date,
                end_date: end_date,
                dev: dev,
                cost: cost,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },

            cache: false,
            success: function(dataResult) {
                if (dataResult.statusCode == 200) {
                    $(".createDevSubmit").removeAttr("disabled");
                    $("#success").show();
                    $('#success').html('New Project Added');
                    $("#popupForm").hide();
                    setTimeout(function() {
                        $("#success").hide();
                    }, 2000);
                } else {
                    $("#error").show();
                    $('#error').html('ERROR!');
                    setTimeout(function() {
                        $("#error").hide();
                    }, 2000);
                }

            }
        });


    });


}


// Valid name function
function validFormDev() {
    $(document).ready(function() {
        $.validator.addMethod("validName", function(value, element) {
            // allow any non-whitespace characters as the host part
            return this.optional(element) || /^[a-zA-Z ]{3,16}$/.test(value);
            // /^[a-zA-Z ]{3,16}$/.test(value);
        }, 'Please enter a valid name.');
        $("#createDevForm").validate({
            errorClass: 'form-dev-error',
            rules: {
                "first_name": {
                    validName: true
                },
                "last_name": {
                    validName: true
                },
            },
            messages: {
                "first_name": {
                    validName: 'Please enter a valid name.'
                },
                "password": {
                    validName: 'Please enter a valid name.'
                },
            }
        });
    })
}


function validFormProject() {
    $(document).ready(function() {
        $.validator.addMethod("isdateafter", function(value, element, params) {
            var startdatevalue = $('#id_start_date').val();
            if (!value || !startdatevalue)
                return true;

            return this.optional(element) || Date.parse(startdatevalue) <= Date.parse(value);
        });
        $.validator.addMethod('validCost', function(value) {
            return Number(value) > 0;
        }, 'Enter a positive number.');
        $("#createProjectForm").validate({

            errorClass: 'form-dev-error',
            rules: {
                "name": {
                    maxlength: 50,
                    minlength: 3
                },
                "des": {
                    maxlength: 200,
                    minlength: 5
                },
                "start_date": {
                    date: true,
                    //dateFormat: true,
                },
                "end_date": {
                    date: true,
                    isdateafter: true
                },
                "cost": {
                    validCost: true,

                },
                "dev": {
                    required: true,

                }
            },
            messages: {
                "name": {
                    maxlength: "Must be 3 to 20 characters",
                    minlength: "Must be 3 to 20 characters"
                },
                "des": {
                    maxlength: "Must be 5 to 200 characters",
                    minlength: "Must be 5 to 200 characters"
                },
                "start_date": {
                    date: "Enter a valid Date",

                },
                "end_date": {
                    date: "Enter a valid Date",
                    isdateafter: "Enter a valid End Date"

                },
                "cost": {
                    validCost: "Enter a positive value",

                },
                "dev": {
                    required: "Select a project",
                },
            }
        });
    })
}