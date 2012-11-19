<?php 
$DB_CONNECTION = mysql_connect('localhost','root',''); 
if (!$DB_CONNECTION) { 
	die(`Could not connect to MySQL: ` . mysql_error()); 
} 

if ( !(array_key_exists('id', $_POST) ) )
	{
	 die('No id parameter! ');
	}

	$id = $_POST['id'];
mysql_select_db("bursa", $DB_CONNECTION) or die(mysql_error());
$result = mysql_query("UPDATE `alerts` SET `viewed` = 1 where
									(`viewed` = 0 or `viewed` is null ) and `date_completed` is not null and `user_id` = '$id'") or die(mysql_error());;

mysql_close($DB_CONNECTION); 
?>