// Update dev when click name or update

$('#tabledev tr td:nth-child(3) a, #tabledev tr td button:nth-child(1)').click(function(e) {
    e.preventDefault();
    var rowValue = [];
    let row = $(this).closest("tr");
    let tdLength = $(this).closest("tr").children("td").length;
    for (let i = 0; i < tdLength - 1; i++) {
        rowValue.push(row.find(`td:eq(${i})`).text());
    }
    var dev_id = rowValue[1];
    $.ajax({
        url: "/form/update/dev/",
        data: {
            dev_id: dev_id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

        },
        success: function(result) {
            $("#createForm").html(result);
            autocompleteUpdateDev()
            projectDetail()
            createFormButton();
            validFormDev();
            createDevSubmit("/form/update/dev/", dev_id, 'Updated');
        }
    });
});

//load project detail
function projectDetail() {
    $('#project-link a').click(function(e) {
        //console.log($(this).text());
        //alert($(this).DataTable().row(this).data())
        e.preventDefault();
        var project_id = $(this).attr('value');
        $.ajax({
            url: "/form/detail/project/",
            type: "GET",
            data: {
                project_id: project_id,

            },
            success: function(result) {
                $(".loginPopup").append(result);
                autocompleteUpdateDev()
                $('#popupForm').hide()
                $(`#detailForm`).show();
                $(".canceldetail").click(function() {
                    $(`#detailForm`).remove()
                    $('#popupForm').show()
                })
                validFormDev()

                // $('#detailForm input').prop('disabled', true);

            }
        });


    });
}

// Search Dev name
$('#search-dev').autocomplete({
    source: function(request, response) {
        $.ajax({
            url: "/search/dev/name/",
            data: {
                term: $('#search-dev').val(),
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
        dev_id = ui.item.value.split(' - ')[0];
        text = ui.item.value.split(' - ')[1];
        $.ajax({
            url: "/form/update/dev/",
            data: {
                dev_id: dev_id,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()

            },
            success: function(result) {
                $("#createForm").html(result);
                //autocomplete Project Field
                autocompleteUpdateDev()
                    //Load project detail
                projectDetail()
                    //Show Form
                createFormButton();
                //Valid
                validFormProject();
                //Submit
                createDevSubmit("/form/update/dev/", dev_id, 'Updated');
            }
        });



    }
})

// Remove Dev
$('#tabledev tr td button:nth-child(2)').click(function(e) {
    $('#delete-modal').show()
    let row = $(this).closest("tr");
    var dev_id = row.find(`td:eq(${1})`).text()
    $('#remove-btn').click(function() {
        $.ajax({
            url: '/form/remove/dev/',
            type: "POST",
            data: {
                dev_id: dev_id,
                csrfmiddlewaretoken: getCookie('csrftoken'),
            },

            cache: false,
            success: function(dataResult) {
                if (dataResult.statusCode == 200) {
                    $("#success").show();
                    $('#success').html(dataResult.messages);
                    $('#modelRemove').modal('hide');
                    setTimeout(function() {
                        $("#success").hide();
                    }, 2000);
                    location.reload();
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



})


// Autocomplete Project in Dev form
function autocompleteUpdateDev() {
    $(`#autocomplete-project`).autocomplete({
        source: function(request, response) {
            $.ajax({
                url: `/form/projectautocomplete/`,
                data: {
                    term: $(`#autocomplete-project`).val(),
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
            id = ui.item.value.split(' - ')[0];
            text = ui.item.value.split(' - ')[1];
            var add = true;
            $(`.projectsId`).each(function() {
                var valueA = String($(this).attr('value'));
                if (valueA == String(id)) {
                    add = false
                }
            });
            $(`#autocomplete-project`).val('');
            if (add == true) {
                html = `<a href='new' class=projectsId value='` + id + "'>" + text + "</a>";
                html += "<span class='ti-close'></span>";
                $(`#project-link`).append(html);

                projectDetail()
            }
            $(`#project-link span`).click(function(e) {
                e.preventDefault();
                $(this).prev().remove();
                $(this).remove();
            });
        }
    })
}