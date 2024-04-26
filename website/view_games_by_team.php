<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../assets/substyles.css">
    <title>View Games By Team</title>
</head>
<body>
    <h1>Games By Team</h1>
    <div class="options-box">
        <label for="teamSelect">Select a Team:</label>
        <select id="teamSelect" name="team" onchange="updateSelectedTeam()">
            <option value="" disabled selected>Select a team</option>
            <option value="49ers">San Francisco 49ers</option>
            <option value="Bears">Chicago Bears</option>
            <option value="Bengals">Cincinnati Bengals</option>
            <option value="Bills">Buffalo Bills</option>
            <option value="Broncos">Denver Broncos</option>
            <option value="Browns">Cleveland Browns</option>
            <option value="Buccaneers">Tampa Bay Buccaneers</option>
            <option value="Cardinals">Arizona Cardinals</option>
            <option value="Chargers">Los Angeles Chargers</option>
            <option value="Chiefs">Kansas City Chiefs</option>
            <option value="Colts">Indianapolis Colts</option>
            <option value="Cowboys">Dallas Cowboys</option>
            <option value="Dolphins">Miami Dolphins</option>
            <option value="Eagles">Philadelphia Eagles</option>
            <option value="Falcons">Atlanta Falcons</option>
            <option value="Giants">New York Giants</option>
            <option value="Jaguars">Jacksonville Jaguars</option>
            <option value="Jets">New York Jets</option>
            <option value="Lions">Detroit Lions</option>
            <option value="Packers">Green Bay Packers</option>
            <option value="Panthers">Carolina Panthers</option>
            <option value="Patriots">New England Patriots</option>
            <option value="Raiders">Las Vegas Raiders</option>
            <option value="Rams">Los Angeles Rams</option>
            <option value="Ravens">Baltimore Ravens</option>
            <option value="Redskins">Washington Football Team</option>
            <option value="Saints">New Orleans Saints</option>
            <option value="Seahawks">Seattle Seahawks</option>
            <option value="Steelers">Pittsburgh Steelers</option>
            <option value="Texans">Houston Texans</option>
            <option value="Titans">Tennessee Titans</option>
            <option value="Vikings">Minnesota Vikings</option>
        </select>    

        <button type="submit" form="playersForm">View Games</button>
    </div>

    <form id="playersForm" action="view_games_by_team.php" method="POST">
        <input type="hidden" name="submit" value="1"> <!-- Adding a hidden input field named "submit" -->
        <input type="hidden" name="team_id1" id="selectedTeam">
    </form>

    <button onclick="location.href='home.html';" class="back-btn">Home</button>

    <script>
        function updateSelectedTeam() {
            var teamSelect = document.getElementById("teamSelect");
            var selectedTeam = teamSelect.options[teamSelect.selectedIndex].value;
            document.getElementById("selectedTeam").value = selectedTeam;
        }
    </script>
</body>
</html>

<?php
if (isset($_POST['submit'])) 
{
    // add ' ' around multiple strings so they are treated as single command line args
    $data = escapeshellarg($_POST['team_id1']); #data

    // build the linux command that you want executed;  
    $command = 'python3 view_games_by_team.py ' . $data;

    // remove dangerous characters from command to protect web server
    $command = escapeshellcmd($command);
 
    // echo then run the command
    //echo "command: $command <br>";
    system($command);           
}
?>
