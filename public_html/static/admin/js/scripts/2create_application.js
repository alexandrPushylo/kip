const count_vehicles = $('.select_input_tech').length;

for (let i=1;i<=count_vehicles;i++){
    let input_tech = '#input_tech_'+i;
    let input_driver = '#input_driver_'+i;
    const io_tech = "#io_tech_"+i;
    const io_driver = "#io_driver_"+i;

    const id_app = "#hid_id_app"+i;
    const id_app_val = $(id_app).val();

    const v_tech = $(io_tech).val();
    const v_drv = $(io_driver).val();

    const curr_vehicle = $(input_tech);
    const curr_driver = $(input_driver);

    const var_tech = v_tech.replace(' ','').replace('.','');

    $(input_tech+'> option[veh="'+ var_tech +'"]').prop('selected',true);//////////
    $('#div_driver_'+i+' > .'+var_tech).prop('hidden',false);
    $('#div_driver_'+i+' > .'+var_tech+'> option[value="'+ v_drv +'"]').prop('selected',true);

    curr_vehicle.change(function () {
        let v = this.value;
        let ve = v.replace(' ','').replace('.','');
        $('#div_driver_'+i+' > .input_driver').prop('hidden',true);
        $('#div_driver_'+i+' > .'+ve).prop('hidden',false);

        $(io_tech).val(this.value);

    });

    $(input_driver+' > .'+var_tech).change(function () {
        $(io_driver).val(this.value);
    })
};
$('#add_vehicle_btn').click(function () {
    const checked_tech = $("#input_tech_add > option:checked").text();
    const inp_tech_cls = $("#input_tech_add").val()
    const checked_driver = $("."+inp_tech_cls+" > option:checked").val();
    // const checked_driver = $("#input_driver_add > option:checked").val();


    const descr_app = $('#description_app_add').val();
    console.log(checked_driver)
    if(checked_tech==='---'){return false;}

    $('#vehicle_list_ul').append('<div class="row mb-3"></div>');
    const vehicle_div = $('#vehicle_list_ul > div:last-child');

    vehicle_div.append('<input class="col-4" type="text" name="vehicle_list" value="'+checked_tech +'">');
    if (checked_driver === '---'){
        vehicle_div.append('<input class="col-4" type="text" name="driver_list" value="">');
    }else {
        vehicle_div.append('<input class="col-4" type="text" name="driver_list" value="'+checked_driver +'">');
    }
    vehicle_div.append('<button role="button" class="btn btn-danger btn-sm col-1">X</button>');
    vehicle_div.append('<textarea class="form-control mt-2 app_description" name="description_app_list" rows="1">'+descr_app+'</textarea>');
    const btn_remove = $('#vehicle_list_ul > div:last-child button');
    btn_remove.css('margin-left','15px');

    btn_remove.click(function () {
        this.parentElement.remove();
        return false;
    });

    // $('#input_tech_add option:first').prop('selected',true);
    $('.driver').prop('hidden',true);

    // $('#input_driver_add option:first').prop('selected',true);
    $('#description_app_add').val('');

    $('.app_description').each(function () {
    this.style.height = ""+(this.scrollHeight)+"px";
    });
    return false;
});

$("#input_tech_add").change(function (){
    $('.driver_add').prop('hidden',true);
    let v = this.value;
    $('.driver_add.'+v).prop('hidden',false);
    return false
});

$('.app_description').each(function () {
    this.style.height = ""+(this.scrollHeight)+"px";
});


