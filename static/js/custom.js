$(document).ready(function() {
    
    $('.increment-btn').click(function (e) { 
        e.preventDefault();

        var inc_value = $(this).closest('.car_data').find('.qty-input').val();
        var value = parseInt(inc_value,10)
        value = isNaN(value) ? 0 : value;
        if(value < 10)
        {
            value++
            var inc_value = $(this).closest('.car_data').find('.qty-input').val(value);
        }
        
    });

    $('.decrement-btn').click(function (e) { 
        e.preventDefault();

        var dec_value = $(this).closest('.car_data').find('.qty-input').val();
        var value = parseInt(dec_value,10)
        value = isNaN(value) ? 0 : value;
        if(value > 1)
        {
            value--
            var inc_value = $(this).closest('.car_data').find('.qty-input').val(value);
        }
        
    });

    $('.addToBook').click(function (e) { 
        e.preventDefault();

        var c_id = $(this).closest('.car_data').find('.car_id').val();
        var car_day = $(this).closest('.car_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/addToBook",
            data: {
                'c_id':c_id,
                'car_day':car_day,
                csrfmiddlewaretoken: token
            },
            dataType: "dataType",
            success: function (response) {
                console.log(response)
                alertify.success(response.status)
            }
        });
        
    });
}); 