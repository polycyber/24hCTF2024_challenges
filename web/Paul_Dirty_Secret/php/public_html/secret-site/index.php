<!DOCTYPE html>
<?php /* Flag 1
polycyber{SQLi_To_LFI_but_where_is_the_hidden_site?}
 */ ?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            padding: 0;
            background-image: url('barbapapa.jpg');
            background-repeat: repeat;
            height: 100vh;
            font-family: Arial, sans-serif;
        }

        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        form {
            background-color: #f2f2f2;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }

        h1 {
            color: red; /* Changement de la couleur en rouge */
            text-align: center;
            padding: 20px;
            margin: 0;
        }
    </style>
    <title>Barbapapa's Secret</title>
</head>
<body>
<?php

if ($_SERVER['REQUEST_METHOD'] !== 'POST' || !isset($_POST['password'])) {
    include("password_request.php");
} else {
    $conn = new mysqli("mysql","challuser","ThisIsADumbPassword","barbadb");
    if ($conn->connect_error) {
	die("Connection failed: " . $conn-connect_error);
    }

    $password = sha1($_POST['password']);

    $sql = "SELECT secret FROM Secret LIMIT 1;";
    $result = $conn->query($sql);
    $row = $result->fetch_assoc();

    if ($row["secret"] == $password) {
	    $conn = new mysqli("mysql","flaguser","ThisIsADumbPasswordAGAIN","barbadb");
	    if ($conn->connect_error) {
	    	die("Connection failed: " . $conn-connect_error);
	    }
	    $result = $conn->query("SELECT secret_flag FROM Flag LIMIT 1;");
	    $row = $result->fetch_assoc();
	    echo "<h1>Well done, the flag is: " . $row['secret_flag'] . "</h1>";
    }
	
   else {
       include("password_request.php");
   }   
}
?>
</body>
</html>

