$('.app_description').each(function () {
    this.style.height = ""+(this.scrollHeight)+"px";
});

$('.io_current_day').change(function () {
    location.href = '/applications/'+this.value;
})

$('.div_td').click(function () {
    location.href = '/append_in_hos_tech/'+this.id;

})