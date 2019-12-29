var a = 100
var q = 1
category_list =  {"General":9 , "Science":17 , "Sports":21};
chosen_category = "";
var questions = ""

$("#game").hide();

$(document).ready(function () {

    $('div.card.category').click(function (e) {
        console.log(e.currentTarget.id);
        chosen_category = e.currentTarget.id;
        $("#selected_category").html(chosen_category);
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
    show_questions();

};

function show_questions()
{
    quest = questions[q]["question"];
    ans = questions[q]["incorrect_answers"] ;
    ans[ans.length] = questions[q]["correct_answer"];
    shuffle(ans);
    correct = questions[q]["correct_answer"];





}

function shuffle(a) {
    for (let i = a.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
}