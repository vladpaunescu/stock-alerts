<?php

require_once('config.php');

$DB_CONNECTION = mysql_connect($DB_HOST, $DB_USERNAME, $DB_PASSWORD);
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
	
mysql_select_db($DB_DEFAULT_DATABASE, $DB_CONNECTION) or die(mysql_error());

$result = mysql_query("INSERT INTO `bursa`.`alerts` (`id`, `user_id`, `stock_id`, `date_added`, `value`, `type`, `target_value`, `date_completed`, `viewed`) 
VALUES (NULL, '$user_id', '$stock_id', now(), (select value from daily_quotes where stock_id='$stock_id'), '$type', '$value', NULL, NULL);") or die(mysql_error());;
mysql_close($DB_CONNECTION); 
echo 'OK';
?>