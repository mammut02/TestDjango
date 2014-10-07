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

function vote(id, vote, url) {
    $.ajax({
        type: 'POST',
        url: url,
        data: {post: id, vote: vote},
        dataType: 'json',
        success: vote_confirm,
        error: function(){
            alert('AJAX Error');
        }
    });
}

function vote_confirm(response){
    total_vote = JSON.parse(response);
    if(total_vote > 0){
        $('#post-vote').text(total_vote);
    }
    else
    {
        $('#post-vote').text("0");
    }
}