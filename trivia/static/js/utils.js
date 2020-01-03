// get html id of answers, if answer is correct - change its color to green
function check_if_correct(answer_id, index)
{
    if ( $(answer_id).html() == question_data['correct_answer'] )
    {
    $(answer_id).css('background-color' , 'green');
    }
};

// shuffle a list
function shuffle(a) {
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
};

// google translate
function googleTranslateElementInit() {
    new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element'); };
