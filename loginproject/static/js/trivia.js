a = 100

category_list =  {"General":9 , "Science":17 , "Sports":21};
chosen_category = "";
var questions = ""

$("#game").hide();

$(document).ready(function () {

    $('div.card.category').click(function (e) {
        console.log(e.currentTarget.id);
        chosen_category = e.currentTarget.id;
        chosen_category_id = category_list[chosen_category];
        console.log("id : " + chosen_category_id);
        start_trivia(chosen_category_id);

    });

});

function start_trivia(id)
{
    console.log("start trivia func");
    URL ="https://opentdb.com/api.php?amount=50&category=" + id + "&type=multiple";
    console.log(URL)
    $.ajax({
        type: "get",
        url: URL,
        success: function (response) {
            questions = response.results;
        }
    });
    console.log(questions);
    $("#game").show();
};