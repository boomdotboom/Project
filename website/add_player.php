<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/substyles.css">
    <title>Add a Player</title>
</head>
<body>
<h3>Enter Player into Database:</h3>

<form action="add_player.php" method="post">
    Name: <input type="text" name="name"><br>
    Position: <input type="text" name="position"><br>
    PlayerID: <input type="text" name="playerID"><br>
    TeamID: <input type="text" name="teamID"><br>
</form>
<br><br>
    <a href="home.html">Home</a>
</body>
</html>

<?php
if (isset($_POST['submit']))
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $name = escapeshellarg($_POST['name'])
    $position = escapeshellarg($_POST['position']);
    $playerID = escapeshellarg($_POST['playerID']);
    $teamID = escapeshellarg($_POST['teamID']);

    $command = 'python3 add_game.py ' . $name . ' ' . $position . ' ' . $playerID. ' ' . $teamID;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>";
    // run insert_new_item.py
    system($escaped_command);          
}
?>


