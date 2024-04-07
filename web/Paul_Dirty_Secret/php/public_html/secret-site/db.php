<?php
$host = 'mysql';
$user = 'challuser';
$pass = 'ThisIsADumbPassword';
$db = 'barbadb';

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
