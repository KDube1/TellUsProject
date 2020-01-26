<?php
/*
Question class 
*/
class question {
    public $content, $options, $weightDist;

    //Constructor
    public function __construct($content, $options, $weightDist) {
        $this->content = $content;
        $this->options = $options;
        $this->weightDist = $weightDist;

    }

}

?>