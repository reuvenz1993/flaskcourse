var a = 100
var q = 1
category_list =  {"General":9 , "Science":17 , "Sports":21};
chosen_category = "";
var chosen_category_id = ""
var question = ""

$("#game").hide();

$(document).ready(function () {

    $('div.card.category').click(function (e) {
        console.log(e.currentTarget.id);
        chosen_category = e.currentTarget.id;
        $("#selected_category").html(chosen_category);
        chosen_category_id = category_list[chosen_category];
        console.log("id : " + chosen_category_id);
        $("#game").show();
        $("#categories").hide();
        $("#promo").hide();
        $("#selected_category").html('category :' + chosen_category);
        start_trivia(chosen_category_id);

    });

});

function start_trivia(id)
{
    console.log("start trivia func");
    URL ="https://opentdb.com/api.php?amount=1&category=" + id + "&type=multiple";
    console.log(URL)
    $.ajax({
        type: "get",
        url: URL,
        success: function (response) {
            question_data = response.results[0];
            quest = question_data['question'];
            ans_list = question_data["incorrect_answers"] ;
            ans_list[ans_list.length] = question_data['correct_answer'];
            shuffle(ans_list);
            $('#the_question').html(quest);
            $('#ans1').html(ans_list[0]);
            $('#ans2').html(ans_list[1]);
            $('#ans3').html(ans_list[2]);
            $('#ans4').html(ans_list[3]);

        }
    });

    console.log(question_data);

};


function shuffle(a) {
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
};


$( ".btn" ).click(function(e) {
    console.log(e.target.innerText);
    pick = e.target.innerText;
    if ( pick == question_data['correct_answer'])
    {
        correct = true;
        $('#'+e.target.id).css('background-color', 'green');
        console.log('this is the right ans');
    } else {$('#'+e.target.id).css('background-color', 'red'); };

    setTimeout(next_question, 2000);
  });

  function next_question()
  {
    $('#ans1').css('background-color', '#eaf2f9');
    $('#ans2').css('background-color', '#eaf2f9');
    $('#ans3').css('background-color', '#eaf2f9');
    $('#ans4').css('background-color', '#eaf2f9');
    start_trivia(chosen_category_id);
  };