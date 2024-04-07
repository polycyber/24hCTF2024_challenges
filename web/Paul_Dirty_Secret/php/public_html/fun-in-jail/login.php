<?php session_start();
// FLAG 1
//polycyber{SQLi_To_LFI_but_where_is_the_hidden_site?}

$host = 'mysql';
$user = 'challuser';
$pass = 'ThisIsADumbPassword';
$db = 'barbadb';

try {
$pdo = new PDO("mysql:host=$host;dbname=$db",$user,$pass);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e){
	die("Connection error : " . $e->getMessage());
}

if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $sql = "SELECT username as nb FROM Users WHERE username = '" . $username . "' AND passwd = '" . $password . "';";

    try {
	$result = $pdo->query($sql)->fetchAll();
    } catch (PDOException $e) {
    	die("ERROR");
    }
    	

    if (count($result) === 1) {
	    $output = "Authentication successful as : " . $username;
	    $_SESSION["username"] = $username;
    } else {
        $output =  "Incorrect login or password.";
    }
}

if (isset($_SESSION["username"])) {
	header('Location: http://fun-in-jail.ctf:897/admin.php');
	echo $output;
	exit;
}
echo $output;
?>



<?php include("head.php"); ?>
<header class="pagehead">
	<div class="masthead-subheading">Who are you ?</div>
</header>

<div class="login-container">
  <h2>Connexion</h2>


  <form class="login-form" action="login.php" method="post">
    <div>
      <label for="username">Nom d'utilisateur :</label>
      <input type="text" id="username" name="username" required>
    </div>
    <div>
      <label for="password">Mot de passe :</label>
      <input type="password" id="password" name="password" required>
    </div>
    <div>
      <input type="submit" value="Se connecter">
    </div>
  </form>

</div>



<?php include("foot.php") ?>


<?php
// FLAG 1
//polycyber{SQLi_To_LFI_but_where_is_the_hidden_site?}
?>
