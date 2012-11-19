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


$result = mysql_query("select s.stock_id, symbol, w.value oldVal, (select q.value from realtime_quotes q where q.stock_id = s.stock_id order by date_added desc limit 1) newVal   from stocks s, watchlist w where w.stock_id = s.stock_id and w.user_id = '$id' ;") or die(mysql_error());


while ( $row = mysql_fetch_array($result) ) 
{
 echo $row['stock_id'];
 echo ',';
 echo $row['symbol'];
 echo ',';
 echo $row['oldVal'];
 echo ',';
 echo $row['newVal'];
 echo ',';
 
}	


mysql_close($DB_CONNECTION); 
?>