$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    },  
});
$(document).on('click','.expand',function(e){
    //không chuyển sang trang form luôn 
    console.warn('warin')
    $('.menu-profile').toggleClass('hidden');
})
.on('click','.js-submit',function(e){
    const title = $('.js-post-title').val().trim();
    const text =  $('.js-post-text').val().trim();
    const time = $('.js-post-time').val();
    const $btn = $(this);
    if(!title.length){
        return false;
    }
    $btn.prop("disabled",true).text("Posting!")
    $.ajax(
        {
            type:'POST',
            url:  $('.js-post-text').data("post-url"),    
            data:{
                title:title,
                text:text,
                time:time,
            },
            success:(dataHtml) =>{
                $("#posts-container").prepend(dataHtml)
                $btn.prop('disabled',false).text("New Post");
                $(".js-post-title").val('')
                $(".js-post-text").val('')
                window.location.href = '/';
            },
            error: (error)=>{
                console.warn(error)
                $btn.prop("disabled",'false').text("Error")
            }
        }
    )
})
.on('click','.toggle-model',function (e) {
    window.location.href = '/';
})