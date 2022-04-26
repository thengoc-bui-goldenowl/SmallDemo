//Search project name

$('#search-project').autocomplete({
    source: function(request, response) {
        $.ajax({
            url: "/search/project/name/",
            data: {
                term: $('#search-project').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            dataType: "json",
            type: "GET",
            success: function(data) {
                response(data);
            }
        });
    },
    select: function(event, ui) {
        project_id = ui.item.value.split(' - ')[0];
        text = ui.item.value.split(' - ')[1];
        $.ajax({
            url: "/form/update/project/",
            data: {
                project_id: project_id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

            },
            success: function(result) {
                $("#createForm").html(result);
                //autocomplete Dev Filed in Project Form
                autocompleteUpdate()
                    //Load Dev detail
                devDetail()
                    //Show form
                createFormButton();
                //Valid
                validFormProject();

                $("#id_start_date, #id_end_date").datepicker({
                    dateFormat: 'yy-mm-dd'
                });
                //Submit
                createProjectSubmit("/form/update/project/", project_id, 'Updated');
            }
        });


    }
})



// Search Date
$('#btnSearchDate').click(function() {
    if ($('#startDate').val() != "" && $('#endDate').val() != "") {
        var dataSearchDate = [];
        var startDate = $('#startDate').val();
        var endDate = $('#endDate').val();
        var url = "/search/project/date/?startDate=" + String(startDate) + "&endDate=" + String(endDate)
        window.location.replace(url)

    } else {
        alert("Start Date and End Date is not none!")
    }

});