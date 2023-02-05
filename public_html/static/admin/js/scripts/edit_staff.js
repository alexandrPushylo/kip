const chg_pass_btn = $('#change_pass');
const new_pass = $('#new_pass');
const old_pass = $('#old_pass');

const io_post = $('#io_post');
const select_post = $('#post_select');
const io_foreman = $('#io_foreman');
const select_foreman = $('#foreman_select');

chg_pass_btn.click(function () {
    new_pass.attr('hidden',false);
    old_pass.attr('hidden',true);
    return false;
});

$('#post_select> option[value="'+ io_post.val() +'"]').prop('selected', true);

const hidden_div = $('.cl_foreman').attr('hidden',true);
if (io_post.val() === 'Мастер'){
        hidden_div.attr('hidden',false);
    }else {hidden_div.attr('hidden',true);}

select_post.change(function (){
    if (this.value === 'Мастер'){
        hidden_div.attr('hidden',false);
    }else {hidden_div.attr('hidden',true);}

    if(this.value === 'Прораб'){
        io_foreman.val('self');
    }
})

$('#foreman_select> option[value="'+ io_foreman.val() +'"]').prop('selected', true);
select_foreman.change(function () {
    io_foreman.val(this.value);

})
