(function () {
    /*
        We use an IIFE to properly encapsulate all JavaScript code and prevent
        leaking anything into global scope.
     */
    var answersInput = jQuery('#timepref__answers');
    if (!answersInput.length) {
        throw new Error('cannot find answers input #timepref__answers');
    }

    // Block index and state are read from existing DOM elements
    var plotIndex = parseInt(answersInput.attr('data-plot-index')) - 1;
    var state = JSON.parse(answersInput.val() || '[]');

    jQuery('.timepref__plot-choices').each(function () {
        /*
            We parse every existing choice row and register proper listeners to handle user selection
            of choices.
         */
        var choiceRow = jQuery(this);
        var plotIndex = parseInt(choiceRow.attr('data-plot-index'));
        var plotRow = jQuery('.timepref__plot-index-' + plotIndex);

        choiceRow.find('.timepref__plot-choice').on('click', function (e) {
            if (jQuery(e.target).is('input')) {
                return;
            }
            jQuery(this).find('input').click();
        });

        choiceRow.find('input[type=radio]').on('change', function () {
            choiceRow
                .find('.timepref__plot-choice-selected')
                .removeClass('timepref__plot-choice-selected');
            if (choiceRow.find('input:checked').length) {
                plotRow.removeClass('timepref__plot-unanswered');
                choiceRow.find('input:checked')
                    .closest('.timepref__plot-choice')
                    .addClass('timepref__plot-choice-selected');
            } else {
                plotRow.addClass('timepref__plot-unanswered');
            }
            checkAllPlots();
            updateState();
        });

    });

    checkAllPlots();
    updateState();

    /**
     * Serializes the current user selection and updates the current state of Plot answers
     */
    function updateState() {
        var pageState = [];
        jQuery('.timepref__plot-choices').each(function () {
            var choiceRow = jQuery(this);
            var selected = choiceRow.find('input:checked');
            if (selected.length) {
                pageState.push(parseInt(selected.val()));
            } else {
                var range = choiceRow.find('input[type=range]');
                if (range.length) {
                    pageState.push(parseInt(range.val()));
                } else {
                    pageState.push(-1);
                }
            }
        });
        state[pageIndex] = pageState;
        answersInput.val(JSON.stringify(state));
    }

    /**
     * Checks whether all questions have yet been answered by the user, i.e. a choice has been selected
     */
    function checkAllPlots() {
        if (jQuery('.timepref__plot-unanswered').length) {
            jQuery('.timepref__next-button').hide();
            jQuery('.timepref__waiting').show();
        } else {
            jQuery('.timepref__next-button').show();
            jQuery('.timepref__waiting').hide();
        }
    }

}());
