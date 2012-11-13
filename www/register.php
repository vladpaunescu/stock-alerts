<?php 
$DB_CONNECTION = mysql_connect('localhost','root',''); 
if (!$DB_CONNECTION) { 
	die(`Could not connect to MySQL: ` . mysql_error()); 
} 

if ( !(array_key_exists('user', $_POST) && array_key_exists('pass', $_POST)) )
	{
	 die('Parametrii !');
	}
$user = $_POST['user'];
$pass = $_POST['pass'];
$sex = $_POST['sex'];

mysql_select_db("bursa", $DB_CONNECTION) or die(mysql_error());


mysql_query("INSERT INTO user (`username`, `password`, `sex`) 
		VALUES ('$user', '$pass', '$sex')") or die(mysql_error());;

mysql_close($DB_CONNECTION); 

echo $user;

?> 


