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
        <form action="bonus.php" method="post">
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
    $data = escapeshellarg($_POST['gameID']); #data

    // build the linux command that you want executed;  
    $command = 'python3 bonus.py ' . $data;

    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
 
    // echo then run the command
    echo "<br> command: $command <br>";
    system($command);           
}
?>


