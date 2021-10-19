$(document).ready(function () {
    // set step size
    var earlier_max = {{ earlier_max }};
    var later_max = {{ later_max }};
    document.getElementById("id_slider_one").step = earlier_max/10;
    document.getElementById("id_slider_two").step = later_max/10;

    // hide slider thumb until initial click
    $('input[name=slider_one]').on('input change', function () {
        $('input[name=slider_one]').addClass('slider_one_thumb');
        $('input[name=slider_two]').addClass('slider_two_thumb');
        var slider_one_val = earlier_max - $(this).val();
        var slider_two_val = $(this).val()*later_max/earlier_max;
        document.getElementById("id_slider_two").value = $(this).val()*later_max/earlier_max;
        updateLabel(slider_one_val, slider_two_val);
    });

    // handle changes in slider value
    $('input[name=slider_one]').on('input', function() {
        var slider_one_val = earlier_max - $(this).val();
        var slider_two_val = $(this).val()*later_max/earlier_max;
        document.getElementById("id_slider_two").value = slider_two_val; // links the two slider values together
        updateLabel(slider_one_val, slider_two_val);
        $('#check_slider_one').val(1);
        $('#check_slider_two').val(1);
    });

    // functions for slider 2

    // hide slider thumb until initial click
    $('input[name=slider_two]').on('input change', function () {
        $('input[name=slider_one]').addClass('slider_one_thumb');
        $('input[name=slider_two]').addClass('slider_two_thumb');
        var slider_two_val = $(this).val();
        var slider_one_actual_val = slider_two_val*earlier_max/later_max;
        var slider_one_display_val = earlier_max - slider_one_actual_val;
        updateLabel(slider_one_display_val, slider_two_val);
        document.getElementById("id_slider_one").value = slider_one_actual_val;
    });

    // handle changes in slider value
    $('input[name=slider_two]').on('input', function() {
        var slider_two_val = $(this).val();
        var slider_one_actual_val = slider_two_val*earlier_max/later_max;
        var slider_one_display_val = earlier_max - slider_one_actual_val;
        document.getElementById("id_slider_one").value = slider_one_actual_val;
        updateLabel(slider_one_display_val, slider_two_val);
        $('#check_slider_one').val(1);
        $('#check_slider_two').val(1);
    });

    function updateLabel(slider_one_val, slider_two_val) {
        var f1 = document.getElementById("feedback_one");
        var f2 = document.getElementById("feedback_two");
        var fc = document.getElementById("feedback_center");
        var ft = document.getElementById("feedback_text");
        slider_one_norm = slider_one_val/earlier_max;
        f1.style.top = (-315 + slider_one_norm*400)+"px";
        f2.style.top = (-315 + slider_one_norm*400)+"px";
        fc.style.top = (-215 + slider_one_norm*400)+"px";
        f1.style.visibility = "visible";
        f2.style.visibility = "visible";
        fc.style.visibility = "visible";
        f1.innerHTML = "$"+slider_one_val;
        f2.innerHTML = "$"+slider_two_val;
        ft.innerHTML = 'You will receive <strong>$'+slider_one_val+'</strong> {{earlier_time}} and <br>$<strong>'+slider_two_val+'</strong> {{later_time}}';
    }
});   