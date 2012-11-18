<?php
require_once('config.php');

$DB_CONNECTION = mysql_connect($DB_HOST, $DB_USERNAME, $DB_PASSWORD);

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


mysql_select_db($DB_DEFAULT_DATABASE, $DB_CONNECTION) or die(mysql_error());


mysql_query("update users set `username` = '$user', `password` = '$pass'
		where `user_id` = $id;") or die(mysql_error());
mysql_close($DB_CONNECTION); 
echo 'OK';
?> 


