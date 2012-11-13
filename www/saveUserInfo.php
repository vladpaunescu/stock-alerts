<?php 
$DB_CONNECTION = mysql_connect('localhost','root',''); 
if (!$DB_CONNECTION) { 
	die(`Could not connect to MySQL: ` . mysql_error()); 
} 

if ( !(array_key_exists('id', $_POST) && array_key_exists('user', $_POST) &&  array_key_exists('pass', $_POST)) )
	{
	 die('Parametrii !');
	}
$id = $_POST['id'];
$user = $_POST['user'];
$pass = $_POST['pass'];


mysql_select_db("bursa", $DB_CONNECTION) or die(mysql_error());


mysql_query("update user set `username` = '$user', `password` = '$pass'
		where `id` = $id;") or die(mysql_error());
mysql_close($DB_CONNECTION); 
echo 'OK';
?> 


