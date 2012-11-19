<?php 
$DB_CONNECTION = mysql_connect('localhost','root',''); 
if (!$DB_CONNECTION) { 
	die(`Could not connect to MySQL: ` . mysql_error()); 
} 

if ( !(array_key_exists('id', $_POST) ) )
	{
	 die('No id parameter! ');
	}
	if ( !(array_key_exists('type', $_POST) ) )
	{
	 die('No type parameter! ');
	}
		if ( !(array_key_exists('change', $_POST) ) )
	{
	 die('No change parameter! ');
	}
	if ( !(array_key_exists('stockid', $_POST) ) )
	{
	 die('No stockid parameter! ');
	}
	

	$user_id = $_POST['id'];
	$stock_id = $_POST['stockid'];
	$type = $_POST['type'];
	$value = $_POST['change'];
	
mysql_select_db("bursa", $DB_CONNECTION) or die(mysql_error());

$result = mysql_query("INSERT INTO `bursa`.`alerts` (`id`, `user_id`, `stock_id`, `date_added`, `value`, `type`, `target_value`, `date_completed`, `viewed`) 
VALUES (NULL, '$user_id', '$stock_id', now(), (select value from realtime_quotes where stock_id='$stock_id' order by `date_added` desc limit 1), '$type', '$value', NULL, NULL);") or die(mysql_error());;
mysql_close($DB_CONNECTION); 
echo 'OK';
?>