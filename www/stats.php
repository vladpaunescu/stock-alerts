<?php 
$DB_CONNECTION = mysql_connect('localhost','root',''); 
if (!$DB_CONNECTION) { 
	die(`Could not connect to MySQL: ` . mysql_error()); 
} 

mysql_select_db("bursa", $DB_CONNECTION) or die(mysql_error());
$result = mysql_query("SELECT symbol, url FROM `stocks`") or die("Error");
while ( $row = mysql_fetch_array($result) ) 
{
 echo $row['symbol'];
 echo ',';
 echo $row['url'];
 echo ',';
 
}	


mysql_close($DB_CONNECTION); 
?>