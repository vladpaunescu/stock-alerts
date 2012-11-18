<?php
require_once('config.php');

$DB_CONNECTION = mysql_connect($DB_HOST, $DB_USERNAME, $DB_PASSWORD);

if (!$DB_CONNECTION) { 
	die(`Could not connect to MySQL: ` . mysql_error()); 
} 

if ( !(array_key_exists('id', $_POST) ) )
	{
	 die('Parametrii !');
	}
$id = $_POST['id'];

mysql_select_db($DB_DEFAULT_DATABASE, $DB_CONNECTION) or die(mysql_error());

$limit = 4;

$result = mysql_query("select symbol, value from stocks s, watchlist w where
		w.user_id = '$id' and w.stock_id = s.stock_id limit $limit;") or die(mysql_error());;

	
while ( $row = mysql_fetch_array($result) ) 
{
echo $row['symbol'];
echo ',';
echo $row['value'];
echo ',';
}	

echo ',OK';	

mysql_close($DB_CONNECTION); 
?>
