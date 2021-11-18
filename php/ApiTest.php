<?php
header("Content-Type: application/json; charset=UTF-8");
if (isset($_GET["TEST"])){
	if ($_GET["TEST"] == "OK"){
		$t["a1"] = "a1";
		$t["a2"] = "a2";
		http_response_code(200);
		echo json_encode($t);
	}
	
}else{
		http_response_code(404);
		$message["message"] = "not found";
		echo json_encode($message);
		exit(1);
	}	


?>
