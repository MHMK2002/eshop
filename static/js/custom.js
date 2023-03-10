function setParentId(parentId) {
    $('#parent-id').val(parentId);
    document.getElementById('comment-box').scrollIntoView({behavior: "smooth"})
}


function addComment(blogId){
    var comment = $('#comment-text').val();
    var parentId = $('#parent-id').val();
    $.get("/blog/add-comment", {
        comment_text: comment,
        blog_id: blogId,
        replay_id: parentId
    }).then(res => {
        console.log(res)
    });
    document.getElementById('comment-area').scrollIntoView({behavior: "smooth"});
}