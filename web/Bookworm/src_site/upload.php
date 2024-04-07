<?php
session_start();

$defaultLang = 'en';
$lang = isset($_COOKIE['language']) ? $_COOKIE['language'] : $defaultLang;

$translations = [
    'en' => [
        'loginError' => 'Incorrect credentials.',
        'fileUploadErrorPhpNotAllowed' => 'Error: Uploading .php files is not allowed.',
        'fileUploadSuccess' => 'File uploaded successfully. Path:',
    ],
    'fr' => [
        'loginError' => 'Identifiants incorrects.',
        'fileUploadErrorPhpNotAllowed' => 'Erreur : L\'upload de fichiers .php n\'est pas autorisé.',
        'fileUploadSuccess' => 'Fichier uploadé avec succès. Chemin :',
    ]
];

$errorMessage = '';
$successMessage = '';

// Vérification de l'authentification
if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = strtolower($_POST['username']);
    $password = $_POST['password'];

    // Ici, ajouter la logique pour vérifier les identifiants
    // Pour l'exemple, on utilise des valeurs codées en dur
    if ($username == "librarian" && $password == "R3ad-2-3scap3!") {
        $_SESSION['logged_in'] = true;
    } else {
        $errorMessage = $translations[$lang]['loginError'];
    }
}

$loggedIn = isset($_SESSION['logged_in']) && $_SESSION['logged_in'] == true;

if ($loggedIn && isset($_FILES['uploaded_file'])) {
    $fileExtension = pathinfo($_FILES['uploaded_file']['name'], PATHINFO_EXTENSION);
    
    // Générer un nom de fichier aléatoire et conserver l'extension originale
    $randomFileName = bin2hex(random_bytes(8)) . '.' . strtolower($fileExtension);

    // Chemin de destination avec le nom de fichier aléatoire
    $destination = '/var/www/html/uploads/' . $randomFileName;

    // Vérifier si le fichier se termine par '.php'
    if (strtolower($fileExtension) === 'php') {
        $errorMessage = $translations[$lang]['fileUploadErrorPhpNotAllowed'];
    } else {
        // Déplacer le fichier téléchargé vers le dossier 'uploads'
        if (move_uploaded_file($_FILES['uploaded_file']['tmp_name'], $destination)) {
            // Afficher uniquement le chemin du fichier uploadé, pas le chemin complet du système de fichiers
            $successMessage = $translations[$lang]['fileUploadSuccess'] . " /uploads/" . htmlspecialchars($randomFileName, ENT_QUOTES, 'UTF-8');
        } else {
            $errorMessage = $translations[$lang]['fileUploadError'];
        }
    }
}
?>
<!DOCTYPE html>
<html lang="fr">
<head>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <meta charset="UTF-8">
    <title data-localize="pageTitle">Administration - Pénitencier de HiveHex</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

<div id="logo-container">
    <img id="logo" src="logo.webp" alt="Logo de la bibliothèque">
    <h3 data-localize="greeting"><?php echo $loggedIn ? "Bonjour M. Bellick" : "Se connecter"; ?></h3>
    <h1 data-localize="adminTitle">Administration - Pénitencier de HiveHex</h1>
</div>

<?php if ($errorMessage): ?>
    <div class="message-box error-box">
        <?php echo $errorMessage; ?>
    </div>
<?php elseif ($successMessage): ?>
    <div class="message-box success-box">
        <?php echo $successMessage; ?>
    </div>
<?php endif; ?>

<?php if ($loggedIn): ?>
    <!-- Formulaire d'upload si authentifié -->
    <h2 data-localize="addBook">Ajouter un livre</h2>
    <form action="upload.php" method="POST" enctype="multipart/form-data">
        <input type="file" name="uploaded_file">
        <input type="submit" data-localize="uploadButton" value="Upload">
    </form>
<?php else: ?>
    <!-- Formulaire de connexion -->
    <div id="login-container">
        <form action="upload.php" method="POST">
            <label data-localize="usernameLabel">Username:</label> <input type="text" name="username"><br>
            <label data-localize="passwordLabel">Password:</label> <input type="password" name="password"><br>
            <input type="submit" data-localize="loginButton" value="Login">
        </form>
    </div>
<?php endif; ?>

<div id="language-selector">
    <button onclick="changeLanguage('en')">EN</button>
    <button onclick="changeLanguage('fr')">FR</button>
</div>

<script src="language.js"></script>
</body>
</html>
