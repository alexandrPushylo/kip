$('.app_description').each(function () {
    this.style.height = ""+(this.scrollHeight)+"px";
});

$(".btn_driver_panel").click(function () {
    $('.driver_panel').toggle()
    return false
})