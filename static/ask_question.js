var editor = new EpicEditor().load();

$("#btn-post").click(function() {
    var tags = $("#tags").val();
    if (!tags) {
        $("#alert-tags").modal()
        return;
    }

    tags = tags.split(",");
    data = {
        "title": $("#title").val(),
        "content": editor.getElement('previewer').body.innerHTML,
        "tags": tags,
    }

    $.post("", data);
});
