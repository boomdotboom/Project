<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/substyles.css">
    <title>Add a Game</title>
</head>
<body>
    <div class="options-box">
        <h1>Add a Game</h1>
        <form action="add_game.php" method="post">
            <div class="form-group">
                <label for="teamID1">Team 1 ID:</label>
                <input type="text" id="teamID1" name="teamID1" required><br><br>
            </div>
            <div class="form-group">
                <label for="teamID2">Team 2 ID:</label>
                <input type="text" id="teamID2" name="teamID2" required><br><br>
            </div>
            <div class="form-group">
                <label for="date">Date:</label>
                <input type="date" id="date" name="date" required><br><br>
            </div>
            <div class="form-group">
                <label for="score1">Score Team 1:</label>
                <input type="text" id="score1" name="score1" required><br><br>
            </div>
            <div class="form-group">
                <label for="score2">Score Team 2:</label>
                <input type="text" id="score2" name="score2" required><br><br>
            </div>
            <div class="form-group">
                <label for="gameID">Game ID:</label>
                <input type="text" id="gameID" name="gameID" required><br><br>
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>
    <a href="home.html">Home</a>
</body>
</html>


<?php
if (isset($_POST['submit'])) 
{
    // add ' ' around multiple strings so they are treated as single command line args
    $data = escapeshellarg($_POST['teamID1''teamID2''date''score1''score2''gameID']); #data

    // build the linux command that you want executed;  
    $command = 'python3 Sports.py ' . $data;

    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
 
    // echo then run the command
    echo "command: $command <br>";
    system($command);           
}
?>


