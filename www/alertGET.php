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

	$id = $_POST['id'];

mysql_select_db($DB_DEFAULT_DATABASE, $DB_CONNECTION) or die(mysql_error());

$result = mysql_query("SELECT id, symbol , date_added, value, type, target_value, date_completed, viewed
                                   FROM `alerts` a, stocks s  where user_id=$id and s.stock_id = a.stock_id;") or die(mysql_error());;

while ( $row = mysql_fetch_array($result) ) 
{
 echo $row['id'];
 echo ','; 
 echo $row['symbol'];
 echo ','; 
 echo $row['date_added'];
 echo ','; 
 echo $row['value'];
 echo ','; 
 echo $row['type'];
 echo ','; 
 echo $row['target_value'];
 echo ',';
 echo $row['date_completed'];
 echo ',';
 echo $row['viewed'];
 echo ',';
}	


mysql_close($DB_CONNECTION); 
?>