<?php

require_once('config.php');

$DB_CONNECTION = mysql_connect($DB_HOST, $DB_USERNAME, $DB_PASSWORD);
if (!$DB_CONNECTION) { 
	die('Could not connect to MySQL: ' . mysql_error()); 
} 
echo 'Connection OK';
echo "<br />";
mysql_select_db("test", $DB_CONNECTION);

$result = mysql_query("SELECT * FROM testtable");

while($row = mysql_fetch_array($result))
  {
  echo $row['id'];
  echo "<br />";
  }


mysql_close($DB_CONNECTION); 
?> 


