var category_list =  {"General":9 , "Science":17 , "Sports":21};
var chosen_category , chosen_category_id , score , downloadTimer  ;
var answers = [ '#ans1' , '#ans2' , '#ans3' , '#ans4' ];
var given_time = 30 ;
var given_mistakes = 3 ;
var mistakes = 0 ;



// Get api Token
$.ajax({
    type: "get",
    url: 'https://opentdb.com/api_token.php?command=request' ,
    success: function (response) {
        token = response['token'];
    }});




$(document).ready(function () {

    //hide unnecessary
    $("#start , #game , #summary").hide();

    //Select category
    $('div.card.category').click(function (e) {
        $("#categories , #promo").hide(1000);
        $("#start").show(1000);
        chosen_category = e.currentTarget.id;
        chosen_category_id = category_list[chosen_category];
        $(".selected_category").html('category : ' + chosen_category);
    });
});

//start game
$("#start-btn").click(function (e) {
    e.preventDefault();
    $("#start").hide(1000);
    $("#game").show(2000);
    score = 0 ;
    $('#score').html(score);

    get_and_show_question(chosen_category_id);
});

function get_and_show_question(id)
{
    URL ="https://opentdb.com/api.php?amount=1&category=" + id + "&type=multiple" + "&token=" + token;

    $.ajax({
        type: "get",
        url: URL,
        success: function (response) {
            //build question and answer list
            question_data = response.results[0];
            quest = question_data['question'];
            ans_list = question_data["incorrect_answers"] ;
            ans_list[ans_list.length] = question_data['correct_answer'];

            shuffle(ans_list); // shuffle answer list

            // make question and answers apper
            $('#the_question').html(quest);
            $('#ans1').html(ans_list[0]);
            $('#ans2').html(ans_list[1]);
            $('#ans3').html(ans_list[2]);
            $('#ans4').html(ans_list[3]);
            $('#the_question , #Answers').fadeTo( 300 , 1 );
            start_count_down(given_time);
        }});
};

// user chooses an answer 
$( ".answer" ).click(function(e) {
    clearInterval(downloadTimer);
    pick = e.target.innerText;
    $('#'+e.target.id).css('border' , '2px solid black');

    if ( pick == question_data['correct_answer'])
        {
        $('#'+e.target.id).css('background-color' , 'green');
        score_addition =  5 * (question_data['difficulty'] =="easy") + 10 * (question_data['difficulty'] =="medium") + 15 * (question_data['difficulty'] =="hard");
        $('#score_add').html("+" + score_addition).fadeIn(200).fadeOut(1200)
        score += score_addition;
        $('#score').fadeOut(500 , function() {$('#score').html(score).fadeIn(200); }  );
        } else
        {
        $('#'+e.target.id).css('background-color' , 'red');
        mistakes += 1 ;
        answers.forEach(check_if_correct);
        };

    $('.answer').attr("disabled", true);
    setTimeout(next_question, 2000);
    $('#Answers , #the_question').fadeTo( 2200, 0 );
  });

function next_question()
{
$('.answer').removeAttr( 'style disabled border' );
$('#mistakes').html(mistakes);

// if mistakes < given_mistakes got to next question, else end game
if ( mistakes < given_mistakes )
    {
    get_and_show_question(chosen_category_id);
    }
    else
    {
    $("#game").hide();
    $("#summary").show();
    $('#final_score').html(score);
    show_scoreboard();
    };
};

function start_count_down (time)
{
downloadTimer = setInterval(function(){
    $('#clock').html(time);
    $('.progress-bar').width((time/given_time ) * 100 + "%");
    if(time <= 0){
        clearInterval(downloadTimer);
        $('#clock').html('expired');
        mistakes += 1 ;
        answers.forEach(check_if_correct);
        setTimeout(next_question, 2000);
    }
    time -= 1;
    }, 1000);

};

//get scoreboard from flask and show it
function show_scoreboard()
{
    $.ajax({
        type: "post",
        url: '/get_scoreboard' ,
        success: function (response) {
            scoreboard = response
            $('#table_outer_div').remove() //remove table if it exists to avoid showing it twice

            //create and append table container div
            var table_outer_div = $("<div id='table_outer_div' class='justify-content-center row'> </div>");
            $('#summary').append(table_outer_div);

            //create and append table
            var table_div = $("<table id='table_div' class='centered col-6 table text-center'> </table>");
            $('#table_outer_div').append(table_div);

            //create table head
            var content = "<thead class='thead-dark'> <tr> <th scope='col'>" + '#' + "</th> <th scope='col'>" + 'name' + "</th> <th scope='col'>" +  'score' + '</th></tr></tr></thead>';

            //create var = content and with table body
            content += "<tbody>";

            //iterate via scoreboard to add scores into content
            for(i=0; i<scoreboard.length; i++){
                place = i + 1; // # place
                content += "<tr><th scope='row'>" + place + "</th> <th scope='row'>" +  scoreboard[i]['name'] + "</th> <td>" +  scoreboard[i]['score'] + '</td>';
            }
            content += "</tbody>";

            $('#table_div').append(content);
        }});

};

// add user to scoreboard
$('#submit_scoreboard').click(function (e) {
    e.preventDefault();
    name_to_submit = $('#your_name').val();

    $('#submit_scoreboard , #your_name').prop('disabled', true);

    $.ajax({
        type: "post",
        url: '/submit_to_scoreboard' ,
        data: { 'name' : name_to_submit , 'score' : score } ,
        success: function (response) { show_scoreboard() } });
});

$.getScript("/static/js/utils.js", function (script, textStatus, jqXHR) { console.log("import scss"); });