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

$result = mysql_query("select * from user where id = '$id';") or die(mysql_error());;
$row = mysql_fetch_row($result);
$comma_separated = implode(",", $row);

echo $comma_separated;

mysql_close($DB_CONNECTION); 
?>