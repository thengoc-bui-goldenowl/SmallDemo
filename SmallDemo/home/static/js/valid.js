// Valid name function
function validFormDev() {
    $(document).ready(function() {
        $.validator.addMethod("validName", function(value, element) {
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
                "language": {
                    required: true
                },
            },
            messages: {
                "first_name": {
                    validName: gettext('Please enter a valid name.'),
                    required: gettext("This field is required."),
                },
                "last_name": {
                    validName: gettext('Please enter a valid name.'),
                    required: gettext("This field is required."),
                },
                "language": {
                    required: gettext("This field is required.")
                },
            }
        });
    })
}

// Valid project Form
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
                    required: false,

                }
            },
            messages: {
                "name": {
                    maxlength: gettext("Must be 3 to 20 characters"),
                    required: gettext("This field is required."),
                    minlength: gettext("Must be 3 to 20 characters")
                },
                "des": {
                    maxlength: gettext("Must be 5 to 200 characters"),
                    required: gettext("This field is required."),
                    minlength: gettext("Must be 5 to 200 characters")
                },
                "start_date": {
                    date: gettext("Enter a valid Date"),
                    required: gettext("This field is required."),

                },
                "end_date": {
                    date: gettext("Enter a valid Date"),
                    required: gettext("This field is required."),
                    isdateafter: gettext("Enter a valid End Date")

                },
                "cost": {
                    validCost: gettext("Enter a positive value"),
                    required: gettext("This field is required."),

                },
                "dev": {
                    required: gettext("Select a project"),
                },
            }
        });
    })
}