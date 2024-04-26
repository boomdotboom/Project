<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/substyles.css">
    <title>View Players By Position</title>
</head>
<body>
    <h1>Players on NFL Team</h1>

    <label for="positionSelect">Select a Position:</label>
    <select id="positionSelect" name="position" onchange="updateSelectedPosition()">
        <option value="" disabled selected>Select a position</option>
        <option value="Quarterback">Quarterback</option>
        <option value="Running back">Running Back</option>
        <option value="Wide reciever">Wide Receiver</option>
        <option value="Tight end">Tight End</option>
        <option value="Offensive line">Offensive Lineman</option>
        <option value="Defensive line">Defensive Lineman</option>
        <option value="Linebacker">Linebacker</option>
        <option value="Defensive back">Defensive Back</option>
        <option value="Kicker">Kicker</option>
        <option value="Punter">Punter</option>
        <option value="Kick returner">Kick Returner</option>
        <option value="Punt Returner">Punt Returner</option>
        <option value="Safety">Safety</option>
    </select>

    <button type="submit" form="playersForm">View Positions</button>

    <form id="playersForm" action="view_players_by_position.php" method="POST">
        <input type="hidden" name="submit" value="1"> <!-- Adding a hidden input field named "submit" -->
        <input type="hidden" name="position" id="selectedPosition">
    </form>

    <button onclick="location.href='home.html';" class="back-btn">Home</button>

    <script>
        function updateSelectedPosition() {
            var positionSelect = document.getElementById("positionSelect");
            var selectedPosition = positionSelect.options[positionSelect.selectedIndex].value;
            document.getElementById("selectedPosition").value = selectedPosition;
        }
    </script>
</body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // add ' ' around multiple strings so they are treated as single command line args
    $data = escapeshellarg($_POST['position']); #data

    // build the linux command that you want executed;  
    $command = 'python3 view_players_by_position.py ' . $data;

    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
 
    // echo then run the command
    #echo "command: $command <br>";
    system($command);           
}
?>