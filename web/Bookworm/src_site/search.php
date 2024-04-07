<!DOCTYPE html>
<html lang="fr">
<head>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <meta charset="UTF-8">
    <title data-localize="pageTitle">Bibliothèque</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

<div id="logo-container">
    <img id="logo" src="logo.webp" alt="Logo de la bibliothèque">
    <h1 data-localize="headerTitle">Recherche de livres - Pénitencier de HiveHex</h1>
</div>

<div id="search-container">
    <form action="search.php" method="get">
        <input type="text" name="query" data-localize="searchPlaceholder" placeholder="Recherchez un livre...">
        <input type="submit" data-localize="searchButton" value="Rechercher">
    </form>
</div>

<?php
$mysqli = new mysqli("127.0.0.1", "ctf_user", "hHd86KcneHU92HUhd", "library");
if ($mysqli->connect_error) {
    error_log('Connect Error (' . $mysqli->connect_errno . ') ' . $mysqli->connect_error);
    exit;
}

$query = $_GET['query'];

$result = $mysqli->query("SELECT Title, Author FROM Books WHERE Title LIKE '%$query%' OR Author LIKE '%$query%'");
if (trim($query) == '') $result = "";
$defaultLang = 'en';
$lang = isset($_COOKIE['language']) ? $_COOKIE['language'] : $defaultLang;

$translations = [
    'en' => [
        'searchResults' => 'Search results for',
        'queryError' => 'Erreur lors de l\'exécution de la requête.',
        'bruteforceDetected' => 'You have exceeded the maximum number of allowed requests in a short period of time. A brute-force attempt has been detected.',
        'bruteforceRetry'=> 'Please retry in ',
        'bruteforceRetry2'=> ' minutes and ',
        'bruteforceRetry3'=> ' seconds.',

    ],
    'fr' => [
        'searchResults' => 'Résultats de recherche pour',
        'queryError' => 'Error while executing the query.',
        'bruteforceDetected'=> 'Vous avez dépassé le nombre maximal de requêtes autorisées dans un court laps de temps. Une tentative de brute-force a été détectée.',
        'bruteforceRetry'=> 'Veuillez réessayer dans ',
        'bruteforceRetry2'=> ' minutes et ',
        'bruteforceRetry3'=> ' secondes.',
    ]
];

// Chemin du fichier de log
$logFile = "/var/www/html/request_logs_8idfJwio2.txt";

// Seuil de requêtes pour détecter une attaque (50 requêtes en 10 secondes)
$maxRequests = 30;
$timeFrame = 5; // 10 secondes

// Durée du blocage en secondes (3 minutes)
$blockDuration = 3600;

// Récupère l'adresse IP du visiteur
$ipAddress = $_SERVER['REMOTE_ADDR'];

// Lire les données du fichier de log
$requestData = file_exists($logFile) ? json_decode(file_get_contents($logFile), true) : [];

$currentTime = time();

// Nettoyer les anciennes entrées et vérifier si l'IP est actuellement bloquée
$blocked = false;
foreach ($requestData as $ip => $data) {
    $times = $data['times'];
    $times = array_filter($times, function($time) use ($currentTime, $timeFrame) {
        return ($currentTime - $time) < $timeFrame;
    });

    // Vérifier si cette IP est bloquée
    if ($ip == $ipAddress && isset($data['blockedUntil']) && $currentTime < $data['blockedUntil']) {
        $blocked = true;
    }

    $requestData[$ip]['times'] = $times;
}

if ($blocked) {
    // Calculer le temps restant (en secondes) jusqu'au déblocage
    $remainingTime = $requestData[$ipAddress]['blockedUntil'] - $currentTime;
    $remainingMinutes = floor($remainingTime / 60);
    $remainingSeconds = $remainingTime % 60;

    // Afficher le message d'erreur avec le temps restant
    echo "<div class='error-box'>";
    echo htmlspecialchars($translations[$lang]['bruteforceDetected'], ENT_QUOTES, 'UTF-8') . "<br />";
    echo htmlspecialchars($translations[$lang]['bruteforceRetry'], ENT_QUOTES, 'UTF-8') . $remainingMinutes . htmlspecialchars($translations[$lang]['bruteforceRetry2'], ENT_QUOTES, 'UTF-8') . $remainingSeconds . htmlspecialchars($translations[$lang]['bruteforceRetry3'], ENT_QUOTES, 'UTF-8');
    echo "</div>";

    // Fermeture de la connexion à la base de données
    $mysqli->close();
    $result= "Erreur";
}

// Vérifier le nombre de requêtes pour cette IP
if (isset($requestData[$ipAddress]) && count($requestData[$ipAddress]['times']) >= $maxRequests) {
    // Blocage de l'IP pendant la durée spécifiée
    $requestData[$ipAddress]['blockedUntil'] = $currentTime + $blockDuration;
} else {
    // Enregistrer la requête actuelle
    $requestData[$ipAddress]['times'][] = $currentTime;
}

// Sauvegarder les données dans le fichier
file_put_contents($logFile, json_encode($requestData));


if ($result === false) {
    // Query failed
    echo "<h2>" . htmlspecialchars($translations[$lang]['queryError'], ENT_QUOTES, 'UTF-8') . "</h2>";
    error_log('MySQL Error: ' . $mysqli->error);
}

echo "<h2>" . htmlspecialchars($translations[$lang]['searchResults'], ENT_QUOTES, 'UTF-8') . " '$query'</h2>";
echo "<ul>";

while ($row = $result->fetch_assoc()) {
    echo "<li>" . htmlspecialchars($row['Title'], ENT_QUOTES, 'UTF-8') . " - " . htmlspecialchars($row['Author'], ENT_QUOTES, 'UTF-8') . "</li>";
}

echo "</ul>";

$mysqli->close();
?>

<!-- The upload page is disabled during maintenance. -->
<!-- <a href="upload.php" data-localize="uploadLink">Add a book</a> -->

<!-- Language selection buttons -->
<br />
<div id="language-selector">
    <button onclick="changeLanguage('en')">EN</button>
    <button onclick="changeLanguage('fr')">FR</button>
</div>

<script src="language.js"></script>
</body>
</html>