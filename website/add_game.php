<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/substyles.css">
    <title>Add a Game</title>
</head>
<body>
<h3>Enter Game into the Database:</h3>

<form action="add_game.php" method="post">
    GameID: <input type="text" name="game_id"><br>
    TeamID1: <input type="text" name="team_id1"><br>
    TeamID2: <input type="text" name="team_id2"><br>
    Score1: <input type="text" name="score_1"><br>
    Score2: <input type="text" name="score_2"><br>
    Date: <input type="date" name="date"><br>
    <input name="submit" type="submit" >
</form>
<br><br>
    <a href="home.html">Home</a>
</body>
</html>

<?php
if (isset($_POST['submit']))
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $game_id = escapeshellarg($_POST['game_id'])
    $team_id1 = escapeshellarg($_POST['team_id1']);
    $team_id2 = escapeshellarg($_POST['team_id2']);
    $score_1 = escapeshellarg($_POST['score_1']);
    $score_2 = escapeshellarg($_POST['score_2']);
    $date = escapeshellarg($_POST['date']);

    $command = 'python3 add_game.py ' . $game_id . ' ' . $team_id1 . ' ' . $team_id2. ' ' . $score_1 . ' ' .$score_2. ' '  .$date;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    echo "<p>command: $command <p>";
    // run insert_new_item.py
    system($escaped_command);          
}
?>