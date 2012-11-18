<?php
require_once('config.php');

$DB_CONNECTION = mysql_connect($DB_HOST, $DB_USERNAME, $DB_PASSWORD);

if (!$DB_CONNECTION) { 
	die(`Could not connect to MySQL: ` . mysql_error()); 
} 


	if ( !(array_key_exists('user_id', $_POST) ) )
	{
	 die('No user_id parameter! ');
	}
	if ( !(array_key_exists('stock_id', $_POST) ) )
	{
	 die('No stock_id parameter! ');
	}
		
	$user_id = $_POST['user_id'];
	$stock_id = $_POST['stock_id'];
	
mysql_select_db($DB_DEFAULT_DATABASE, $DB_CONNECTION) or die(mysql_error());

$result = mysql_query("INSERT INTO `bursa`.`watchlist` ( `user_id`, `stock_id`, `date_added`, `value`) 
VALUES ( '$user_id', '$stock_id', now(), (select `value` from daily_quotes where stock_id='$stock_id' order by date desc limit 1));") or die(mysql_error());
mysql_close($DB_CONNECTION); 

?>
