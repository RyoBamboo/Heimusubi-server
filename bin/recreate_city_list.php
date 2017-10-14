<?php
$city_list = array();

ini_set('memory_limit', '2560M');

$json_url = 'city.list.json';
$json = file_get_contents($json_url);
$json = mb_convert_encoding($json, 'UTF8', 'ASCII,JIS,UTF-8,EUC-JP,SJIS-WIN');
$obj = json_decode($json,true);

$fp = fopen('./city_list.txt', 'w');
foreach ($obj as $key=>$value) {
	if ($value['country'] == 'JP') {
		$data = $value['id'] . ',' . $value['name'] . "\n";
		fwrite($fp, $data);
	}
}


exit;
