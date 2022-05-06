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
            url: `/${langCode}/project/${project_id}/`,
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
                createProjectSubmit(`/project/${project_id}/`, project_id, 'Updated', method = "PATCH");
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
        var url = `/${langCode}/search/project/date/${String(startDate)}/${String(endDate)}`
        window.location.replace(url)

    } else {
        alert(gettext("Start Date and End Date is not none!"))
    }

});

$(".vnd, .usd").click(function(e) {
    lang = $.trim($(this).text().toLowerCase())
    e.preventDefault();
    console.log(lang)
    $.ajax({
        url: `/language/${lang}/`,
        type: "GET",
        success: function(dataResult) {
            if (dataResult.statusCode == 200) {
                $("#success").show();
                $('#success').html(dataResult.messages);
                $('#modelRemove').modal('hide');
                setTimeout(function() {
                    $("#success").hide();
                }, 2000);
                if (dataResult.messages == "Changing") {
                    location.reload();
                }
            } else {
                $("#error").show();
                $('#error').html('ERROR!');
                setTimeout(function() {
                    $("#error").hide();

                }, 2000);
            }

        }
    });
})

$('.language-change, .other').hover(function() {
        // over
        $('.other').show()
    },
    function() {
        $('.language ul .other').hide()
    }
);


$('#count').change(function() {
    var row = $(this).children("option:selected").val();
    $.ajax({
        url: `/paginateby/${row}/`,
        type: "GET",
        success: function(dataResult) {
            if (dataResult.statusCode == 200) {
                location.reload();
                window.location.href = window.location.href.split('?')[0];

            }

        }
    });

})