<?php 
include("./header.html");
include("./Question.php");
include("./user.php");
$mainUser = new user();

class main {
    public function readQuestion() {
        //Read input from JSON file
        $json_input = file_get_contents("./QuestionBank.json");
        $array = json_decode($json_input, true);
        if(is_array($array)) {
            foreach($array["questions"] as $question) {
                $temp = new Question($question["content"], $question["options"], $question["weightDist"]);
                array_push($array, $temp);

            }

        }
        return $array;

    }

}

//Initialize Question bank
$QBank = main::readQuestion();
$test = $QBank[0]->content;

?> 

<!--
<div id="commToJS" style="display: none;">
    <?php /*
    $stop = False;
    $i = 0;
    while( ) {
        if($stop == False) {
            $question = $QBank[$i]->content;
            $option1 = QBank[$i]::options[0];
            $option2 = QBank[$i]::options[1];
            $option3 = QBank[$i]::options[2];
            $point1 = QBank[$i]::weightDist[0];
            $point2 = QBank[$i]::weightDist[1];
            $point3 = QBank[$i]::weightDist[2];
            if
            $i += 1;

        }

    }
*/
    ?>


</div>

<div id="commToPHP" style="display: none;">




</div>
-->

<p>
    <h1>Tell-us</h1>
</p>
    <blockquote id="question">
        <p><em>You are not alone</em></p>
    </blockquote>

    <div class = "center">
        <button class="optionButton" id="op1" value="" > Option 1 </button><br> 
        <button class="optionButton" id="op2" value=""> Option 2 </button><br>
        <button class="optionButton" id="op3" value=""> Option 3 </button><br>

    </div>

    <button class="button button-outline" id="gotQuestion"> Got Question ? We are here to help </button>



</body>

<footer>


</footer>
</html>
