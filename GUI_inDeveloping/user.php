<?php
class user {
    public $point;
    public $threhold = 30;
    public $result;

    public function __construct() {
        $this->point = 0;

    }

    public function updatePoint($add) {
        $this->point += $add;

    }

    public function checkPoint() {
        $done = False;
        if (this::point > $threhold) {
            $result = "Depression";
            $done = True;

        }

        return $result;

    }





}
?>