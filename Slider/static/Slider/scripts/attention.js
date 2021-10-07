(function () {

    // figure out how to allow me to select the entire box
    jQuery(".next-button").hide();
    jQuery(".waiting").show();
    jQuery(".attention-check-choice").click(function () {
        jQuery(".next-button").show();
        jQuery(".waiting").hide();
    });
    jQuery(".next-button").click(function () {
        var answersInput = jQuery('#attention__check');
        if (!answersInput.length) {
            throw new Error('cannot find answers input #attention__check');
        }
        var values = []
        for (i = 1; i < 10; i++) {
            str = "#attention-check-" + String(i)
            if (jQuery(str).is(":checked"))
                values.push(i)
        }
        answersInput.val(JSON.stringify(values));
    });
}());
