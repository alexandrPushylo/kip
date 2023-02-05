const count_vehicles = $('.select_input_tech').length;

for (let i=1;i<=count_vehicles;i++){
    let input_tech = '#input_tech_'+i;
    let input_driver = '#input_driver_'+i;
    const io_tech = "#io_tech_"+i;
    const io_driver = "#io_driver_"+i;

    const v_tech = $(io_tech).val();
    const v_drv = $(io_driver).val();

    const curr_vehicle = $(input_tech);
    const curr_driver = $(input_driver);

    // $(input_driver +'> option[value="None"]').attr('hidden',true);

    $(input_tech+'> option[value="'+ v_tech +'"]').prop('selected',true);
    $(input_driver +'> option[veh="'+ v_tech+'"]').attr('hidden',false);
    if(v_drv === ''){
        $(input_driver +" > option:checked").val('').text('---');
    }else {
        $(input_driver+'> option[value="'+ v_drv +'"]').prop('selected',true);
    }

    curr_vehicle.change(function () {
        $(input_driver +'> option').attr('hidden',true);
        $(input_driver +"> option[selected]").attr('hidden',true);
        const checked_tech = this.value;

        $(input_driver +'> option[veh="'+ checked_tech+'"]').attr('hidden',false);



        if ($(input_driver +" option[hidden!='hidden']").length < 2){
        $(input_driver +" option[hidden!='hidden']:last").prop('selected', true);
        }
        else {
            $(input_driver +" option[hidden!='hidden']:first").prop('selected', true);
        // $(input_driver +" > option:checked").val('').text('---');
        }
    });
};
$("#input_driver_add > option:checked").val('').text('---');//////////
$("#input_tech_add").change(function (){
    $("#input_driver_add > option").attr('hidden',true);
    $("#input_driver_add > option[selected]").attr('hidden',false);
    const checked_tech = this.value;
    $("#input_driver_add > option").filter(function (){
        if(checked_tech===this.value){return this;}
    }).attr('hidden',false);

    if ($("#input_driver_add option[hidden!='hidden']").length === 1){
        $("#input_driver_add option[hidden!='hidden']:last").prop('selected', true);
    }
    else {
        $("#input_driver_add option[hidden!='hidden']:first").prop('selected', true);
        // $("#input_driver_add > option:checked").val('').text('---');
    }
});

$('#add_vehicle_btn').click(function () {
    const checked_driver = $("#input_driver_add > option:checked").text();
    const checked_tech = $("#input_tech_add > option:checked").val();
    const descr_app = $('#description_app_add').val();
    if(checked_tech==='---'){return false;}
    $('#vehicle_list').append('<div class="row mb-3"></div>');
    const vehicle_div = $('#vehicle_list > div:last-child');
    vehicle_div.append('<input class="col-4" type="text" name="vehicle_list" value="'+checked_tech +'">');
    if (checked_driver === '---'){
        vehicle_div.append('<input class="col-4" type="text" name="driver_list" value="">');
    }else {
        vehicle_div.append('<input class="col-4" type="text" name="driver_list" value="'+checked_driver +'">');
    }

    vehicle_div.append('<button role="button" class="btn btn-danger btn-sm col-1">X</button>');
    vehicle_div.append('<textarea class="form-control mt-2 app_description" name="description_app_list" rows="1">'+descr_app+'</textarea>');
    const btn_remove = $('#vehicle_list > div:last-child button');
    btn_remove.css('margin-left','15px');
    btn_remove.click(function () {
        this.parentElement.remove();
        return false;
    });
    $('#input_tech_add option:first').prop('selected',true);
    $('#input_driver_add option').prop('hidden',true);
    $('#input_driver_add option:first').prop('selected',true);
    $('#description_app_add').val('');
    $('.app_description').each(function () {
    this.style.height = ""+(this.scrollHeight)+"px";
    });
    return false;
});

$('.app_description').each(function () {
    this.style.height = ""+(this.scrollHeight)+"px";
});


