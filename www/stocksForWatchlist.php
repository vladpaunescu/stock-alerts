<?php 
$DB_CONNECTION = mysql_connect('localhost','root',''); 
if (!$DB_CONNECTION) { 
	die(`Could not connect to MySQL: ` . mysql_error()); 
} 

if ( !(array_key_exists('id', $_POST) ) )
	{
	 die('Parametrii !');
	}
$id = $_POST['id'];

mysql_select_db("bursa", $DB_CONNECTION) or die(mysql_error());


$result = mysql_query("select stock_id, symbol from stocks s where not exists( select 1 from watchlist w where w.stock_id=s.stock_id and user_id = '$id') ;") or die(mysql_error());;

while ( $row = mysql_fetch_array($result) ) 
{
 echo $row['stock_id'];
 echo ',';
 echo $row['symbol'];
 echo ',';
 
}	


mysql_close($DB_CONNECTION); 
?>