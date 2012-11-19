<?php 
$DB_CONNECTION = mysql_connect('localhost','root',''); 
if (!$DB_CONNECTION) { 
	die(`Could not connect to MySQL: ` . mysql_error()); 
} 

if ( !(array_key_exists('user', $_POST) && array_key_exists('pass', $_POST)  
	&& array_key_exists('pass', $_POST) 
	&& array_key_exists('firstName', $_POST) 
	&& array_key_exists('lastName', $_POST) 
	&& array_key_exists('birthday', $_POST) 
	&& array_key_exists('pass', $_POST) 
	&& array_key_exists('sex', $_POST) 
	&& array_key_exists('job', $_POST) 
	&& array_key_exists('phone', $_POST) 
	&& array_key_exists('email', $_POST) 
	) )
	{
	 die('Error !');
	}
$user = $_POST['user'];
$pass = $_POST['pass'];
$firstName = $_POST['firstName'];
$lastName = $_POST['lastName'];
$birthday = $_POST['birthday'];
$pass = $_POST['pass'];
$sex = $_POST['sex'];
$job = $_POST['job'];
$email = $_POST['email'];
$phone = $_POST['phone'];

mysql_select_db("bursa", $DB_CONNECTION) or die(mysql_error());


mysql_query("INSERT INTO users (`username`, `password`,`email`,`first_name`, `last_name`, `birthday`, `sex`, `job`, `phone`) 
		VALUES ('$user', '$pass', '$email', '$firstName', '$lastName' ,'$birthday' ,'$sex', '$job', '$phone')")  or   die(mysql_error()) ;

mysql_close($DB_CONNECTION); 

echo $user;

?> 


