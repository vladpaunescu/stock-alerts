<?php 
$DB_CONNECTION = mysql_connect('localhost','root',''); 
if (!$DB_CONNECTION) { 
	die(`Could not connect to MySQL: ` . mysql_error()); 
} 

if ( !(array_key_exists('id', $_POST)
	&& array_key_exists('user', $_POST)
	&& array_key_exists('pass', $_POST)
	&& array_key_exists('fname', $_POST)
	&& array_key_exists('lname', $_POST)
	&& array_key_exists('age', $_POST)
	&& array_key_exists('sex', $_POST)
	&&  array_key_exists('job', $_POST)
	&& array_key_exists('email', $_POST)
	&& array_key_exists('tel', $_POST))
	)
	{
	 die('Parametrii !');
	}
$id = $_POST['id'];
$user = $_POST['user'];
$pass = $_POST['pass'];
$email = $_POST['email'];
$fname = $_POST['fname'];
$lname = $_POST['lname'];
$age = $_POST['age'];
$sex = $_POST['sex'];
$job = $_POST['job'];
$tel = $_POST['tel'];

mysql_select_db("bursa", $DB_CONNECTION) or die(mysql_error());


mysql_query("update users set `username` = '$user', `password` = '$pass', email = '$email', first_name='$fname', last_name='$lname', birthday='$age', sex='$sex', job='$job', phone='$tel' where `user_id` = $id;") or die(mysql_error());
mysql_close($DB_CONNECTION); 
echo 'OK';
?> 
