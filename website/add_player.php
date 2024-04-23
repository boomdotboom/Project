<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Player</title>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/substyles.css">
</head>
<body>
    <div class="options-box">
        <h1>Add Player</h1>
        <form id="addPlayerForm" action="add_player.php" method="POST" onsubmit="return validateForm()">
            <div class="form-group">
                <label for="playerID">Player ID:</label>
                <input type="text" id="playerID" name="playerID" required>
            </div>
            <div class="form-group">
                <label for="teamName">Team Name:</label>
                <input type="text" id="teamName" name="teamName" required>
            </div>
            <div class="form-group">
                <label for="playerName">Player Name:</label>
                <input type="text" id="playerName" name="playerName" required>
            </div>
            <div class="form-group">
                <label for="position">Position:</label>
                <input type="text" id="position" name="position" required>
            </div>
            <button name="submit" type="submit" >
        </form>    
    </div>

    <br><br>
    <a href="home.html">Home</a>

    <script>
        function validateForm() {
            var form = document.getElementById("addPlayerForm");
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
// Checking if the form has been submitted
if (isset($_POST['playerID']) && isset($_POST['teamName']) && isset($_POST['playerName']) && isset($_POST['position'])) 
{
    // replace ' ' with '\ ' in the strings so they are treated as single command line args
    $playerID = escapeshellarg($_POST['playerID']);
    $teamName = escapeshellarg($_POST['teamName']);
    $playerName = escapeshellarg($_POST['playerName']);
    $position = escapeshellarg($_POST['position']);

    $command = 'python3 add_game.py ' . $playerID . ' ' . $teamName . ' ' . $playerName. ' ' . $position;

    // remove dangerous characters from command to protect web server
    $escaped_command = escapeshellcmd($command);
    // Wrapping echoed message in a div with centering class
    echo '<div class="centered"><p>command: ' . $command . '</p></div>'; 
    // run insert_new_item.py
    system($escaped_command);          
}
?>