document.addEventListener('DOMContentLoaded', function() {
    const assign=document.querySelector("#assign");
    assign.addEventListener('click', function(e) {
        if(!confirm("Please Download Calendar before assigning events. Are you sure you want to continue?"))
        {
            e.stopImmediatePropagation();
            e.preventDefault();
        }
    })
})