var a = 100
var q = 1
category_list =  {"General":9 , "Science":17 , "Sports":21};
var chosen_category = "";
var chosen_category_id = ""
var question = ""
var answers = [ '#ans1' , '#ans2' , '#ans3' , '#ans4' ];
var score ;

$("#start").hide();
$("#game").hide();

$(document).ready(function () {

    $('div.card.category').click(function (e) {
        $("#categories").hide(1000);
        $("#promo").hide(1000);
        $("#start").show(1000);
        console.log(e.currentTarget.id);
        chosen_category = e.currentTarget.id;
        chosen_category_id = category_list[chosen_category];
        $(".selected_category").html('category : ' + chosen_category);
        console.log("id : " + chosen_category_id);

    });


});

$("#start-btn").click(function (e) {
    e.preventDefault();
    $("#categories").hide();
    $("#promo").hide();
    $("#start").hide(1000);
    $("#game").show(2000);
    score = 0 ;
    $('#score').html(score);

    start_trivia(chosen_category_id);
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
            $('#the_question').fadeTo( 300 , 1 );
            $('#Answers').fadeTo( 300 , 1 );

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


$( ".answer" ).click(function(e) {
    console.log(e.target.innerText);
    pick = e.target.innerText;
    
    if ( pick == question_data['correct_answer'])
    {
        correct = true;
        $('#'+e.target.id).css('background-color' , 'green');
        console.log('this is the right ans');
        score += 5 * (question_data['difficulty'] =="easy") + 10 * (question_data['difficulty'] =="medium") + 15 * (question_data['difficulty'] =="hard");
        $('#score').fadeOut(500 , function() {$('#score').html(score).fadeIn(500); }  );
    } else
    {
        $('#'+e.target.id).css('background-color' , 'red');
        answers.forEach(check_if_correct);
    };

    $('.answer').attr("disabled", true);
    setTimeout(next_question, 2000);
    $('#Answers').fadeTo( 2200, 0 );
    $('#the_question').fadeTo( 2200 , 0 );
  });

  function next_question()
  {
    $('.answer').removeAttr( 'style' );
    $('.answer').removeAttr( 'disabled' );
    start_trivia(chosen_category_id);
  };

  function check_if_correct(item, index)
  {
      if ( $(item).html() == question_data['correct_answer'] )
      {
          $(item).css('background-color' , 'green');
      }
  };
