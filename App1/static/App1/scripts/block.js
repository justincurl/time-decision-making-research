(function () {
    jQuery('.timepref__question-choices').each(function () {
        /*
            We parse every existing choice row and register proper listeners to handle user selection
            of choices.
         */
        var choiceRow = jQuery(this);
        var questionIndex = parseInt(choiceRow.attr('data-question-index'));
        var questionRow = jQuery('.timepref__question-index-' + questionIndex);

        choiceRow.find('.timepref__question-choice').on('click', function (e) {
            if (jQuery(e.target).is('input')) {
                return;
            }
            jQuery(this).find('input').click();
            jQuery('.timepref__next-button').show();
            jQuery('.timepref__waiting').hide();
        });

        choiceRow.find('input[type=radio]').on('change', function () {
            choiceRow
                .find('.timepref__question-choice-selected')
                .removeClass('timepref__question-choice-selected');
            if (choiceRow.find('input:checked').length) {
                questionRow.removeClass('timepref__question-unanswered');
                choiceRow.find('input:checked')
                    .closest('.timepref__question-choice')
                    .addClass('timepref__question-choice-selected');
            } else {
                questionRow.addClass('timepref__question-unanswered');
            }
            document.getElementById('timepref__answer').value = choiceRow.find('.timepref__question-choice-selected')[0].cellIndex;
            jQuery('.timepref__next-button').show();
            jQuery('.timepref__waiting').hide();
        });
    });
}());
