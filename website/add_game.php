<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Game</title>
    <link rel="stylesheet" type="text/css" href="../style/add_game.css"> 
    <link rel="stylesheet" type="text/css" href="../style/carousel.css"> 
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/substyles.css">
</head>
<body>
    <div class="options-box">
        <h1>Add Game:</h1>
        <form action="add_game.php" method="post">
            <div class="form-group">
                <label for="gameID">Game ID:</label>
                <input type="text" id="gameID" name="gameID" required>
            </div>
            <div class="form-group">
                <label for="date">Date:</label>
                <input type="date" id="date" name="date" required>
            </div>
            <div class="form-group">
                <label for="location">Location:</label>
                <input type="text" id="location" name="location" required>
            </div>
            <div class="form-group">
                <label for="team1">Team 1 ID:</label>
                <input type="text" id="team1" name="team1" required>
            </div>
            <div class="form-group">
                <label for="score1">Team 1 Score:</label>
                <input type="text" id="score1" name="score1" required>
            </div>
            <div class="form-group">
                <label for="team2">Team 2 ID:</label>
                <input type="text" id="team2" name="team2" required>
            </div>
            <div class="form-group">
                <label for="score2">Team 2 Score:</label>
                <input type="text" id="score2" name="score2" required>
            </div>
            
            <button name="submit" type="submit" >
        </form>
    </div>

    <br><br>
    <a href="home.html">Home</a>

    <script>
        function validateForm() {
            var form = document.getElementById("addGameForm");
            var inputs = form.getElementsByTagName("input");
            for (var i = 0; i < inputs.length; i++) {
                if (inputs[i].value.trim() === "") {
                    alert("Please fill out all the fields.");
                    return false;
                }
            }
            return true;
        }
    </script>
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