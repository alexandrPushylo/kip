$('.app_description').each(function () {
    this.style.height = ""+(this.scrollHeight)+"px";
});

$(".btn_driver_panel").click(function () {
    if($('.driver_panel').is(':hidden')){
        $('.driver_panel').prop('hidden',false)
    }else {
        $('.driver_panel').prop('hidden',true)
    }
    return false
})