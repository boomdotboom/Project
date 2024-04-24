<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/substyles.css">
    <title>Insert Team Information into Database</title>
</head>
<body>
    <div class="options-box">
        <h1>Insert Teams into Database</h1>
        <form action="create_db.php" method="post">
            <button type="submit">Submit</button>
        </form>
    </div>
    <a href="home.html">Home</a>
</body>
</html>


<?php
if (isset($_POST['submit'])) 
{
    // build the linux command that you want executed;  
    $command = 'python3 create_db.py ';

    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
 
    // echo then run the command
    echo "<p>command: $command <p>";
    system($command);           
}
?>