<?php 
require_once('config.php');
$DB_CONNECTION = mysql_connect($DB_HOST, $DB_USERNAME, $DB_PASSWORD); 
if (!$DB_CONNECTION) { 
	die(`Could not connect to MySQL: ` . mysql_error()); 
} 
if ( !(array_key_exists('user', $_POST) ) )
	{
	 die('No user parameter! ');
	}
if ( !(array_key_exists('pass', $_POST)) )
	{
	 die('No pass parameter! ');
	}
$user = $_POST['user'];
$pass = $_POST['pass'];
mysql_select_db($DB_DEFAULT_DATABASE, $DB_CONNECTION) or die(mysql_error());
$result = mysql_query("select * from user where
		username = '$user' and password = '$pass';") or die(mysql_error());
$row = mysql_fetch_array($result);
echo $row['id'];

mysql_close($DB_CONNECTION); 
?>
