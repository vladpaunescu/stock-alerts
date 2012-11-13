<?php 
/* gets the data from a URL */
function get_data($url) {
  $ch = curl_init();
  $timeout = 50;
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
  curl_setopt($ch,CURLOPT_TIMEOUT, $timeout);
  $data = curl_exec($ch);
  echo 'Curl error: ' . curl_error($ch);
  curl_close($ch);
  return $data;
}

$ret = get_data('news.google.com/news/section?pz=1&cf=all&q=Stock+market&ict=ln');




?> 

http://uauim-nzebd.businesscatalyst.com