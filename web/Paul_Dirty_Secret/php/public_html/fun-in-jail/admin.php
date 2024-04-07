<?php
/* FLAG 1
polycyber{SQLi_To_LFI_but_where_is_the_hidden_site?}
 */


session_start();
if (!isset($_SESSION["username"])){
	header('Location: http://fun-in-jail.ctf:897/login.php');
	exit;
}

?>

<?php include("head.php");?>


<header class="pagehead">
	<div class="masthead-subheading">Administration page</div>
</header>

<h1> Vos notes </h1>

<?php
if (isset($_POST["filename"])){
	print(@file_get_contents("notes/".$_POST["filename"]));
}
else {
	echo <<<EOL
		<form action="admin.php" method="post">
    <label for="selectFile">Sélectionnez un fichier :</label>
    <select name="filename" id="selectFile">
      <option value="fichier1.txt">Fichier 1</option>
      <option value="fichier2.txt">Fichier 2</option>
      <option value="fichier3.txt">Fichier 3</option>
    </select>
    <br><br>
    <input type="submit" value="Envoyer">
  </form>
EOL;
}
?>



<?php include("foot.php") ?>
