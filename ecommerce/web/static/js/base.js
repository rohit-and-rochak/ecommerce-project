function ajax_request(method, url, data, token)
{
    return $.ajax({
        type: method,
        url: url,
        headers: {'X-CSRFToken': token},
        data: data,
        dataType: 'json'
    });

}