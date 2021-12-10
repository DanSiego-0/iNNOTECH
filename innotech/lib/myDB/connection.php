<?php
try{
    $connection = new PDO('mysql:host=34.124.202.8,dbname = innotech','root','password');
    $connection -> setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    echo "Connected";

}catch(PDOException $exc){
    echo $exc -> getMessage();
    die("Could not connect");
}





?>