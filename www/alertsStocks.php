<?php

require_once('config.php');

$DB_CONNECTION = mysql_connect($DB_HOST, $DB_USERNAME, $DB_PASSWORD);

if (!$DB_CONNECTION) { 
	die(`Could not connect to MySQL: ` . mysql_error()); 
} 

mysql_select_db($DB_DEFAULT_DATABASE, $DB_CONNECTION) or die(mysql_error());

$result = mysql_query("SELECT symbol, stock_id FROM `stocks`") or die("Error");
while ( $row = mysql_fetch_array($result) ) 
{
 echo $row['symbol'];
 echo ',';
 echo $row['stock_id'];
 echo ',';
 
}	

mysql_close($DB_CONNECTION); 
?>