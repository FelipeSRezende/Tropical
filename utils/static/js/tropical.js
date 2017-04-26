/**
 * Created by maique on 20/04/17.
 */

function server_format_date(datestring) {
    if (datestring) {
        var splitText = datestring.split("/");
        return splitText[2] + "-" + splitText[1] + "-" + splitText[0];
    }

    return null;
}

function get(url, context, callback) {
    $.ajax({
        url: url,
        data: context,
        dataType: 'json',
        success: function (data) {
            callback(data)
        }
    })
}

function post(url, context, callback) {
    var csrftoken = Cookies.get('csrftoken');
    $.ajax({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        url: url,
        data: context,
        type: 'post',
        dataType: 'json',
        success: function (data) {
            callback(data)
        }
    })
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function alerta(message) {

    bootbox.dialog({
        message:'<div class="text-center">'+message+'</div>',
        onEscape:true,
        show:true,
        backdrop: true
    });
}

function confirma(titulo,message,callback){
    bootbox.confirm({
    title: titulo,
    message: message,
    buttons: {
        cancel: {
            label: '<i class="fa fa-times"></i> Cancel'
        },
        confirm: {
            label: '<i class="fa fa-check"></i> Confirm'
        }
    },
    callback: callback
});
}