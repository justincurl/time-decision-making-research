(function () {
    jQuery(".next-button").hide();
    jQuery(".waiting").show();
    jQuery(".consent-choice").click(function () {
        jQuery(".next-button").show();
        jQuery(".waiting").hide();
    });
    jQuery(".next-button").click(function () {
        var answersInput = jQuery('#consent__answer');
        if (!answersInput.length) {
            throw new Error('cannot find answers input #consent__answer');
        }
        if (jQuery("#yes-consent").is(":checked"))
            answersInput.val(JSON.stringify(1));
        else
            answersInput.val(JSON.stringify(0));
    });

}());
