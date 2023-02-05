console.log("signup")

const io_post = $('#io_post');
const select_post = $('#post_select');
const io_foreman = $('#io_foreman');
const select_foreman = $('#foreman_select');

const hidden_div = $('.cl_foreman').attr('hidden',true);
select_post.change(function (){
    if (this.value === 'Мастер'){
        hidden_div.attr('hidden',false);
    }else {hidden_div.attr('hidden',true);}

    if(this.value === 'Прораб'){
        io_foreman.val('self');
    }

})
select_foreman.change(function () {
    io_foreman.val(this.value);

})

