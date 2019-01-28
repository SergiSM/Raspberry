<?php 
header("Content-Type: application/json; charset=UTF-8");

/*$json = file_get_contents("http://xxxxx/verreservas_sala.asp?sala=0000000025&fecha=2019/01/31");
$obj = json_decode($json, true);
$json_echo = "";
foreach($obj as $key => $value) {
    if (gettype($value) == "array") {   
        //echo var_dump($value)."<br><br><br>"; 
        foreach ($value as $key => $value) {
            if (gettype($value) == "array") {   
                foreach ($value as $key => $value) {
                    $json_echo .= '{"dia_'.$value["id"].'": "';
                    foreach ($value["tramos"] as $key => $value) {
                        $json_echo .= $value;
                    }
                    $json_echo .= '"},';
                }
            }
        }   
    }
}
echo substr($json_echo, 0, -1);*/

//echo '[{"dia_1":"010"},{"dia_2":"110"}]';  //NO

if ($_POST["fecha"] == "1")
    echo '{"dia_1":"010", "dia_2":"110"}';

if ($_POST["fecha"] == "2")
    echo '{"dia_1":"111", "dia_2":"000"}';

?>
