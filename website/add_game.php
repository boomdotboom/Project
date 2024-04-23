<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Game</title>
    <link rel="stylesheet" type="text/css" href="../style/add_game.css"> 
    <link rel="stylesheet" type="text/css" href="../style/carousel.css"> 
</head>
<body>
    <h3>Enter information about a game to add to the database:</h3>

    <form action="add_game.php" method="post">
        GameID: <input type="text" name="gameID"><br>
        Date: <input type="date" name="date"><br>
        TeamId1: <input type="text" name="team1"><br>
        Score1: <input type="text" name="score1"><br>
        TeamId2: <input type="text" name="team2"><br>
        Score2: <input type="text" name="score2"><br>
        
        <input name="submit" type="submit" >
    </form>
</body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $gameID = escapeshellarg($_POST['gameID']);
    $date = escapeshellarg($_POST['date']);
    $team1 = escapeshellarg($_POST['team1']);
    $score1 = escapeshellarg($_POST['score1']);
    $team2 = escapeshellarg($_POST['team2']);
    $score2 = escapeshellarg($_POST['score2']);

    $command = 'python3 add_game.py ' . $gameID . ' ' . $date . ' ' . $team1 . ' ' . $score1. ' '  . $team2. ' '  . $score2;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>"; 
    // run insert_new_item.py
    system($escaped_command);           
}
?>