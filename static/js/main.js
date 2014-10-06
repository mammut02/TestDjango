/**
 * Created by rod on 06/10/14.
 */

function post_delete(id, url) {
    $.ajax({
        type: 'POST',
        url: url,
        data: {post: id},
        dataType: 'json',
        success: post_delete_confirm,
        error: function(){
            alert('AJAX Error');
        }
    });
}

function post_delete_confirm(response){
    post_id = JSON.parse(response);
    if(post_id > 0){
        $('#post_' + post_id).remove();
    }
    else
    {
        alert('Error');
    }
}